from django.shortcuts import render, redirect
from shahapp.models import customers
from shahapp.forms import customersform
from django import forms
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
	return render(request, 'shahapp/index.html')



def Available(request):

	return render(request, 'shahapp/AvailableStock.html')

def About(request):
	return render(request, 'shahapp/about.html')

def contact(request):
	return render(request, 'shahapp/contact.html')

@login_required(login_url='/accounts/login')
def custrep(request):
	customerdata = customers.objects.all()
	return render(request, 'shahapp/custreport.html', {'customerdata':customerdata})

def customerorder(request):
	form = customersform()
	if request.method=="POST":
		form=customersform(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')
	return render(request, 'shahapp/customerinfo.html', {'form':form})


def deletecust(request,id):
	customerdel =customers.objects.get(id=id)
	customerdel.delete()
	return redirect('/report/')


