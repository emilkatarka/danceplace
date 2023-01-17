from django.urls import path

from . import views #relative import to enable future usage of home app in other projects

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact_message_view, name='contact_message_view'),
    

]
