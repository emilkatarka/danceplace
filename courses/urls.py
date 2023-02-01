from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseView.as_view(), name='course-list'),

]
