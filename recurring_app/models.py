from django.db import models
from expense_app.models import expense
from datetime import timedelta
from django.contrib.auth.models import User

class recurring(models.Model):
    interval_choices = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recurring_patterns")
    recurring_type = models.CharField(max_length=10, choices=interval_choices)
    interval = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    expense = models.ForeignKey(expense, on_delete=models.CASCADE, related_name="recurring_patterns", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} | {self.recurring_type} every {self.interval} interval(s)"

    def generate_next_expense(self):
        last_expense = self.expense
        next_date = None

        # Determine the next date based on the recurring interval
        if self.recurring_type == 'daily':
            next_date = last_expense.date + timedelta(days=self.interval)
        elif self.recurring_type == 'weekly':
            next_date = last_expense.date + timedelta(weeks=self.interval)
        elif self.recurring_type == 'monthly':
            next_date = last_expense.date + timedelta(weeks=4 * self.interval)
        elif self.recurring_type == 'yearly':
            next_date = last_expense.date + timedelta(weeks=52 * self.interval)

        # Check if the next date is within the start and end dates
        if self.start_date <= next_date <= (self.end_date or next_date):
            new_expense = expense.objects.create(
                user=last_expense.user,
                category=last_expense.category,
                amount=last_expense.amount,
                description=last_expense.description,
                date=next_date,
                payment_method=last_expense.payment_method,
                notes=last_expense.notes
            )
            new_expense.save()
