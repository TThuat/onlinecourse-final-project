from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'submit/<int:course_id>/',
        views.submit,
        name='submit'
    ),

    path(
        'exam_result/<int:course_id>/<int:submission_id>/',
        views.show_exam_result,
        name='show_exam_result'
    ),
]