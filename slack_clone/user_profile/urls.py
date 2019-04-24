from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
	path('accounts/login/', views.login_view, name='login'),
	path('profile/<int:profile_id>', views.show_profile, name='profile'),
]