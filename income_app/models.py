from django.db import models
from django.contrib.auth.models import User
from recurring_app.models import recurring
# Create your models here.
class income(models.Model):
    source_choices = [
        ('salary', 'Salary'),
        ('freelancing', 'Freelancing'),
        ('investment', 'Investment'),
        ('business', 'Business'),
        ('gifts', 'Gifts'),
        ('others', 'Other'),
    ]
    
    category_choices = [
        ('primary', 'Primary Income'),
        ('secondary', 'Secondary Income'),
        ('passive','Passive Income'),
        ('supplementary','Supplementary Income'),
        ('others', 'Other Income'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="income")
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    source = models.CharField(max_length=255, choices=source_choices)
    date = models.DateField()
    recurring = models.ForeignKey(recurring,on_delete=models.CASCADE,related_name="income", default=False, blank=True, null=True)
    description = models.TextField(max_length=255)
    category = models.CharField(max_length=255, choices=category_choices)
    
    def __str__(self):
        return f'{self.user.username} {self.category} income from {self.source} on {self.date}'     