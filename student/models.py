# student/models.py
from django.db import models
from django.contrib.auth.models import User
from django.apps import apps  # Import to dynamically reference models

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/Student/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name

# Dynamically load the Course model from the student app
def get_course_model():
    return apps.get_model('student', 'Course')  # Use app name and model name as strings

# Dynamically load the Question model from the quiz app
def get_question_model():
    return apps.get_model('quiz', 'Question')  # Use app name and model name as strings

# Fix for circular import in Question model
class Question(models.Model):
    text = models.TextField()
    options = models.JSONField()  # Example for storing options
    correct_answer = models.CharField(max_length=255)

    # Use a string reference for reverse relationship in ForeignKey
    course = models.ForeignKey('student.Course', on_delete=models.CASCADE)  # String reference to avoid circular import

    def __str__(self):
        return self.text


# Fix for circular import in Course model, use string reference for the relationship to Question
# student/models.py
from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    question_number = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.course_name

