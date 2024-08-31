from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from report_app.models import report
from income_app.models import income
from expense_app.models import expense
from .serializers import reportSerializer
from django.db.models import Sum
from .permissions import IsReportOwner


class reportCreate(generics.CreateAPIView):
    queryset = report.objects.all()
    serializer_class = reportSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        report = serializer.save(user=self.request.user)
        # Generate report data
        report_data = self.generate_report(self.request.user, report.start_date, report.end_date)
        
        # Update the report instance with the generated data
        report.total_income = report_data['total_income']
        report.total_expenses = report_data['total_expenses']
        report.net_savings = report_data['net_savings']
        report.categories_summary = self.generate_category_summary(report)
        # Save the updated report instance
        report.save()
    def generate_report(self, user, start_date, end_date):
        # Get recurring incomes and expenses within the reporting period
        recurring_incomes = income.objects.filter(
            user=user, 
            recurring__isnull=False, 
            recurring__start_date__lte=end_date, 
            recurring__end_date__gte=start_date
        )
        recurring_expenses = expense.objects.filter(
            user=user, 
            recurring__isnull=False, 
            recurring__start_date__lte=end_date, 
            recurring__end_date__gte=start_date
        )

        # Calculate totals
        total_income = 0
        total_expenses = 0
        
        for inc in recurring_incomes:
            months = (end_date.year - start_date.year) * 12 + end_date.month - start_date.month + 1
            total_income += inc.amount * months

        for exp in recurring_expenses:
            months = (end_date.year - start_date.year) * 12 + end_date.month - start_date.month + 1
            total_expenses += exp.amount * months

        # Non-recurring income and expense sums
        non_recurring_income = income.objects.filter(user=user, recurring__isnull=True, date__range=[start_date, end_date]).aggregate(Sum('amount'))['amount__sum'] or 0
        non_recurring_expenses = expense.objects.filter(user=user, recurring__isnull=True, date__range=[start_date, end_date]).aggregate(Sum('amount'))['amount__sum'] or 0

        total_income += non_recurring_income
        total_expenses += non_recurring_expenses

        return {
            'total_income': total_income,
            'total_expenses': total_expenses,
            'net_savings': total_income - total_expenses
        }
    def generate_category_summary(self, report):
        # Initialize the summary dictionary
        summary = {}

        # Handle recurring expenses
        recurring_expenses = expense.objects.filter(
            user=report.user,
            recurring__isnull=False,
            recurring__start_date__lte=report.end_date,
            recurring__end_date__gte=report.start_date
        )

        for exp in recurring_expenses:
            # Calculate the number of months the expense should be applied
            months = (report.end_date.year - report.start_date.year) * 12 + report.end_date.month - report.start_date.month + 1
            
            category = exp.category
            if category not in summary:
                summary[category] = 0
            summary[category] += float(exp.amount) * months

        # Handle non-recurring expenses
        non_recurring_expenses = expense.objects.filter(
            user=report.user,
            recurring__isnull=True,
            date__range=[report.start_date, report.end_date]
        )

        for exp in non_recurring_expenses:
            category = exp.category
            if category not in summary:
                summary[category] = 0
            summary[category] += float(exp.amount)

        return summary


        
class reportList(generics.ListAPIView):
    serializer_class = reportSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return report.objects.filter(user=self.request.user)

class reportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = report.objects.all()
    serializer_class = reportSerializer
    permission_classes = [IsReportOwner]
    
    def perform_update(self, serializer):
        report = serializer.save(user=self.request.user)
        
        report.generate_report_data()
    