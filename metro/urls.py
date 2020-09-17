from django.urls import path

from . import views

urlpatterns = [
    path('verificate/', views.MetroListView.as_view()),
]