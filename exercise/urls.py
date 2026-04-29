from django.urls import path
from . import views

app_name = 'exercise'

urlpatterns = [
    path('',views.ExerciseLogView, name='entry'),
    path('list/',views.ExerciseListView, name='list'),
]
