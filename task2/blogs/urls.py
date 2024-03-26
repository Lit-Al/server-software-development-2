from . import views
from django.urls import path, include
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('users/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]