from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('instructors', views.InstructorListView.as_view()),
    path('course', views.CourseListView.as_view()),
]