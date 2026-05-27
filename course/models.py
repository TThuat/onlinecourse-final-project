from django.db import models
from django.contrib.auth.models import User


class Instructor(models.Model):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    instructors = models.ManyToManyField(Instructor)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    content = models.TextField()

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE
    )

    choices = models.ManyToManyField(Choice)