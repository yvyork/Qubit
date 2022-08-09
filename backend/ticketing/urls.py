from django.urls import path
from . import views

urlpatterns = [
    path('ticket/', views.ticket_list),
    path('ticket/<int:id>', views.ticket_detail),
]