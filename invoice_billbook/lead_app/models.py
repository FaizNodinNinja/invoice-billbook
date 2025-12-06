from django.db import models

# Create your models here.


class Industry(models.Model):
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.industry

class IndustryType(models.Model):
    industrytype = models.CharField(max_length=100)

    def __str__(self):
        return self.industrytype


class Country(models.Model):
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country


class State(models.Model):
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.state

class City(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class ClientStatus(models.Model):
    clientstatus = models.CharField(max_length=100)

    def __str__(self):
        return self.clientstatus


class Lead(models.Model):
    client_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=20)
    address = models.TextField()

    industry = models.ForeignKey('Industry', on_delete=models.CASCADE, null=True)
    industrytype = models.ForeignKey('IndustryType', on_delete=models.CASCADE, null=True)

    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True)
    state = models.ForeignKey('State', on_delete=models.CASCADE, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)

    clientstatus = models.ForeignKey('ClientStatus', on_delete=models.CASCADE, null=True)

    # Token for secure editing


    def __str__(self):
        return self.client_name