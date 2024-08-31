from django.db import models
from django.contrib.auth.models import User

class expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('entertainment', 'Entertainment'),
        ('utilities', 'Utilities'),
        ('shopping', 'Shopping'),
        ('health', 'Health'),
        ('education', 'Education'),
        ('others', 'Others'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('credit', 'Credit Card'),
        ('bank', 'Bank'),
        ('transfer', 'Transfer'),
        ('others', 'Others'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=300)
    date = models.DateField()
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD_CHOICES)
    recurring = models.ForeignKey('recurring_app.recurring', on_delete=models.SET_NULL, null=True, blank=True, related_name="expenses")
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.category} | {self.description} by {self.user.username} on {self.date}'
