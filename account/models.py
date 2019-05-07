from django.db import models


class Account(models.Model):
    type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    value = models.PositiveIntegerField(default=0)
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class SubAccount(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class AccountType(models.Model):
    name = models.CharField(max_length=32)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Fund(models.Model):
    code = models.CharField(max_length=32, blank=True)
    name = models.CharField(max_length=64)
    total_amount = models.PositiveIntegerField(default=0)
    total_value = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Journal(models.Model):
    date = models.DateField()
    debt_account = models.ForeignKey(Account, on_delete=models.PROTECT)
    debt_subaccount = models.ForeignKey(SubAccount, on_delete=models.PROTECT)
    debt_value = models.PositiveIntegerField()
    credit_account = models.ForeignKey(Account, on_delete=models.PROTECT)
    credit_subaccount = models.ForeignKey(SubAccount, on_delete=models.PROTECT)
    credit_value = models.PositiveIntegerField()
    fee = models.IntegerField(default=0)
    foreign_tax = models.IntegerField(default=0)
    domestic_tax = models.IntegerField(default=0)
    memo = models.CharField(max_length=128, blank=True)
