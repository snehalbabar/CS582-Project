from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Course 
# BASE VIEW CLass = VIEW

class CourseObjectMixin(object):
    model = Course
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj 