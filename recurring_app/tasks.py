from celery import shared_task
from .models import recurring
from expense_app.models import expense
from datetime import timedelta

@shared_task
def generate_recurring_expenses():
    recurring_patterns = recurring.objects.all()  # Adjust filter if needed
    
    for pattern in recurring_patterns:
        # Determine the next occurrence date
        last_expense = pattern.expense
        if pattern.recurring_type == 'daily':
            next_date = last_expense.date + timedelta(days=pattern.interval)
        elif pattern.recurring_type == 'weekly':
            next_date = last_expense.date + timedelta(weeks=pattern.interval)
        elif pattern.recurring_type == 'monthly':
            next_date = last_expense.date + timedelta(weeks=4 * pattern.interval)  # Approximation
        elif pattern.recurring_type == 'yearly':
            next_date = last_expense.date + timedelta(weeks=52 * pattern.interval)  # Approximation

        # Create the new expense if within the valid range
        if pattern.start_date <= next_date <= (pattern.end_date or next_date):
            expense.objects.create(
                user=last_expense.user,
                category=last_expense.category,
                amount=last_expense.amount,
                description=last_expense.description,
                date=next_date,
                payment_method=last_expense.payment_method,
                notes=last_expense.notes
            )
