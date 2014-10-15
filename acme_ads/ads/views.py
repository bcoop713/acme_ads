from django.shortcuts import render


def home(request):
	return render(request, 'index.html')

def create_ad(request):
	return render(request, 'create_ad.html')