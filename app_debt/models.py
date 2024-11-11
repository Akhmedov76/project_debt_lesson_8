from django.db import models

from app_users.models import UserModel
from common.models import BaseModel


class DebtModel(BaseModel):
    DEBT_TYPE_CHOICES = [
        ('borrowed', 'Borrowed'),
        ('lent', 'Lent'),
    ]
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    debt_type = models.CharField(max_length=10, choices=DEBT_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.phone_number} - {self.amount} - {self.due_date}"

    class Meta:
        verbose_name_plural = 'Debts'
        verbose_name = 'Debt'
