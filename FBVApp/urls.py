from django.contrib import admin
from django.urls import path
from .views import courseListView,courseDetailsView


urlpatterns = [
    path('courses',courseListView),
    path('course/<int:pk>',courseDetailsView),
]
