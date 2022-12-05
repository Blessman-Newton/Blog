from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path('login/', views.login, name='login'),
	path('register/', views.register, name='register'),
	path('search/', views.search, name='search'),
	path('update/<int:pk>', views.update, name='update'),
	path('add_post/', views.add_post, name='add_post'),
	path('post/<int:pk>', views.post, name='post'),
	path('delete/<int:pk>', views.delete, name='delete'),

]