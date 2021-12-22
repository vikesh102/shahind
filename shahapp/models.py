from django.db import models

# Create your models here.



class customers(models.Model):
	first_Name=models.CharField(max_length=20)
	last_Name=models.CharField(max_length=40)
	Product_Name=models.CharField(max_length=100)
	Company_Name=models.CharField(max_length=60)
	Quantity_in_KG=models.IntegerField()
	Contact_Number=models.IntegerField()









