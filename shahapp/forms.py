from django import forms
from shahapp.models import customers 

class customersform(forms.ModelForm):
	class Meta:
		model=customers
		fields=["first_Name","last_Name","Company_Name","Quantity_in_KG","Contact_Number","Product_Name",]