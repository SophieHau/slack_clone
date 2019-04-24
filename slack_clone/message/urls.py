from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
	path('channels/add_message/<int:channel_id>', views.add_message, name='add_message'),
]