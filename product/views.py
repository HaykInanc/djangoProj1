from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def getProducts(request):
	data = {}
	data['goods'] = Good.objects.all()
	return render(request, 'product/index.html', context=data)