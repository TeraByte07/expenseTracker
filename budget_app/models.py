from django.db import models
from django.contrib.auth.models import User
from income_app.models import income
from expense_app.models import expense
from recurring_app.models import recurring
# Create your models here.
class budget(models.Model):
    category_choices = [
        ('groceries', 'Groceries'),
        ('utilities', 'Utilities'),
        ('entertainment','Entertainment'),
        ('vacation','Vacation'),
        ('others', 'Others'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budget")
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.CharField(max_length=255, choices=category_choices)
    description = models.TextField(max_length=255)
    recurring = models.ForeignKey(recurring,on_delete=models.CASCADE,related_name="budget", default=False, blank=True, null=True)
    expenses = models.ManyToManyField(expense, blank=True, related_name="budget")
    income = models.ManyToManyField(income, blank=True,related_name="budget")
    remaining_amount = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=2)
    
    def __str__(self):
        return f'{self.user.username} | {self.name} budget'