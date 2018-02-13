"""from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
"""

from django.urls import path

from . import views

app_name = 'todolist'
urlpatterns = [
	path('', views.index, name='index'),
	path('category-detail/<int:category_id>/', views.category_detail, name='category_detail'),
	path('category-save', views.category_save, name='category_save'),
	# path('<int:category_id>/results/', views.results, name='results'),
	path('todo-detail/<int:todo_id>/', views.todo_detail, name='todo_detail'),
	#path('<int:category_id>/<int:todo_id>/dsc/', views.dsc, name='dsc'),
]