from django.db import models
from django.contrib.auth.models import User
from expense_app.models import expense
from income_app.models import income

class report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="report")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_income = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    total_expenses = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    net_savings = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    categories_summary = models.JSONField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username}s\' {self.title}'

    def generate_report_data(self):
        expenses = expense.objects.filter(user=self.user, date__range=[self.start_date, self.end_date])
        total_expenses = expenses.aggregate(total=models.Sum('amount'))['total'] or 0
        total_income = sum([item.amount for item in income.objects.filter(user=self.user, date__range=[self.start_date, self.end_date])])
        net_savings = total_income - total_expenses

        categories_summary = {}
        for exp in expenses:
            category = exp.category
            if category not in categories_summary:
                categories_summary[category] = 0
                
            categories_summary[category] += float(exp.amount)  # Convert to float
                
        self.total_income = float(total_income)  # Convert to float
        self.total_expenses = float(total_expenses)  # Convert to float
        self.net_savings = float(net_savings)  # Convert to float
        self.categories_summary = categories_summary
        self.save()

    def generate_category_summary(self):
        expenses = expense.objects.filter(user=self.user, date__range=[self.start_date, self.end_date])
        summary = {}
        for exp in expenses:
            category = exp.category
            if category not in summary:
                summary[category] = 0
            summary[category] += exp.amount
        return summary