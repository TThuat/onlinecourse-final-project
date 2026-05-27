from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

def home(request):
    return HttpResponse("Online Course Home Page")

def submit(request, course_id):

    course = get_object_or_404(Course, pk=course_id)

    questions = Question.objects.filter(course=course)

    selected_choices = request.POST.getlist('choices')

    enrollment = Enrollment.objects.first()

    submission = Submission.objects.create(
        enrollment=enrollment
    )

    for choice_id in selected_choices:
        choice = Choice.objects.get(pk=choice_id)
        submission.choices.add(choice)

    context = {
        'course': course,
        'submission': submission
    }

    return render(
        request,
        'onlinecourse/exam_result.html',
        context
    )


def show_exam_result(request, course_id, submission_id):

    course = get_object_or_404(Course, pk=course_id)

    submission = Submission.objects.get(pk=submission_id)

    total = 0
    correct = 0

    questions = Question.objects.filter(course=course)

    for question in questions:

        total += question.grade

        selected_choices = submission.choices.filter(
            question=question,
            is_correct=True
        )

        correct_choices = Choice.objects.filter(
            question=question,
            is_correct=True
        )

        if set(selected_choices) == set(correct_choices):
            correct += question.grade

    grade = (correct / total) * 100

    context = {
        'course': course,
        'grade': grade,
        'submission': submission
    }

    return render(
        request,
        'onlinecourse/exam_result.html',
        context
    )