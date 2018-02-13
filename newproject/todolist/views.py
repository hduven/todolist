from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo, Category
from django.shortcuts import get_object_or_404, render, redirect

def index(request):
	latest_category_list = Category.objects.order_by('-created')[:5]
	context = {
		'latest_category_list': latest_category_list,
	}
	return render(request, 'index.html', context)

def category_detail(request, category_id):
	category = get_object_or_404(Category, pk=category_id)
	return render(request, 'category-detail.html', {
		'category': category,
		'title': category.name,
	})

def category_save(request):
	category = Category(name=request.POST["name"])
	category.save()
	return redirect("/")

def todo_detail(request, todo_id):
	todo = get_object_or_404(Todo, pk=todo_id)
	context = {
		'todo': todo,
		'title': todo.title,
	}
	
	return render(request, 'todo-detail.html', context)