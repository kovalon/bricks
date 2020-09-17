from django.urls import path

from . import views

urlpatterns = [
    path('building/', views.BuildingCreateView.as_view()),
    path('building/<int:id>/add-bricks/', views.BricksCreateView.as_view()),
    path('stats/', views.StatListView.as_view())
]
