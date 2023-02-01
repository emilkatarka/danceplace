from django.views.generic import ListView

from . import models


class CourseView(ListView):
    template_name = 'courses/courses_list.html'
    model = models.Course
    context_object_name = 'courses'

