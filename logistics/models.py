from django.db import models

from common.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Company(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='company/')
    address = models.CharField(max_length=255)
    inn = models.CharField(max_length=255)
    kpp = models.CharField(max_length=255)
    okpo = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    account_number1 = models.FloatField()
    account_number2 = models.FloatField()
    account_number3 = models.FloatField()
    kor_shot = models.CharField(max_length=255)
    bike = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Contract(BaseModel):
    title = models.CharField(max_length=255, default="contract_title")

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='contracts')

    akt = models.FileField(upload_to='contract/')
    invoice = models.FileField(upload_to='contract/')
    zayavka = models.FileField(upload_to='contract/')
    cmr = models.FileField(upload_to='contract/')
    contract_number = models.CharField(max_length=255)
    cost = models.FloatField()
    auto_number = models.CharField(max_length=255)

    def __str__(self):
        return self.title
