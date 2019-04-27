from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
		path('accounts/login/', views.login_view, name='login'),
		path('accounts/signup/', views.signup_view, name='signup'),
		path('accounts/logout/', views.logout_view, name='logout'),
		path('accounts/profile/<int:profile_id>', views.show_profile, name='show_profile'),
		path('accounts/profiles', views.show_profiles, name='show_profiles'),
		path('accounts/profiles/add/<int:friend_id>', views.add_friend, name='add_friend'),
]