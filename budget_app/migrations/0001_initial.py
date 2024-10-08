# Generated by Django 4.2.4 on 2024-08-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('expense_app', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('category', models.CharField(choices=[('groceries', 'Groceries'), ('utilities', 'Utilities'), ('entertainment', 'Entertainment'), ('vacation', 'Vacation'), ('others', 'Others')], max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('remaining_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('expenses', models.ManyToManyField(blank=True, related_name='budget', to='expense_app.expense')),
            ],
        ),
    ]
