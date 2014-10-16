from django.shortcuts import render, redirect
from .models import Newspaper


def create_newspaper(request):
	if request.method == 'POST':
		new_newspaper = Newspaper()
		new_newspaper.name = request.POST['name']
		new_newspaper.save()

		return redirect('/newspapers/%d/' % (new_newspaper.id))
	return render(request, 'create_newspaper.html')

def newspaper_detail(request, id):
	context = {}
	context['newspaper'] = Newspaper.objects.get(pk=id)

	return render(request, 'newspaper_detail.html', context)

def newspaper_list(request):
	context = {}
	context['newspaper_list'] = Newspaper.objects.all()

	return render(request, 'newspaper_list.html', context)