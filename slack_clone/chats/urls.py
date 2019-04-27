from django.urls import path
from . import views

app_name = 'chats'

urlpatterns = [
	path('channels/search', views.search_channel, name='search_channels'),
	path('channels/', views.show_channels, name='channels'),
	path('channels/<int:channel_id>', views.show_channel, name='channel'),
	path('channels/add', views.add_channel, name='add_channel'),
]