from django.shortcuts import render, redirect
from .models import Ad
from newspapers.models import Newspaper
from django.http import Http404


def home(request):
	return render(request, 'index.html')

def create_ad(request):
	if request.method == 'POST':
		new_ad = Ad()
		new_ad.name = request.POST['name']
		new_ad.content = request.POST['content']
		new_ad.save()

		return redirect('/ads/%d/' % (new_ad.id))
	return render(request, 'create_ad.html')

def ad_detail(request, id):
	context = {}
	context['ad'] = Ad.objects.get(pk=id)

	return render(request, 'ad_detail.html', context)

def ad_list(request):
	context = {}
	context['ad_list'] = Ad.objects.all()

	return render(request, 'ad_list.html', context)

def connect_newspaper(request, id):
	if request.method == "POST": 
		newspaper = Newspaper.objects.get(id=request.POST['newspaper_id'])
		ad = Ad.objects.get(id=id)
		ad.newspapers.add(newspaper)
		ad.save()
		return render(request, 'ad_detail.html', {'ad': ad})
	else:
		raise Http404

def disconnect_newspaper(request, id):
	if request.method == "POST": 
		newspaper = Newspaper.objects.get(id=request.POST['newspaper_id'])
		ad = Ad.objects.get(id=id)
		ad.newspapers.remove(newspaper)
		ad.save()
		return render(request, 'ad_detail.html', {'ad': ad})
	else:
		raise Http404