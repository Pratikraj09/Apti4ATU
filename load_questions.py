import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinequiz.settings')
django.setup()

import csv
from quiz.models import Question

def run():
    with open('questions.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Question.objects.create(
                question_text=row['question_text'],
                option_a=row['option_a'],
                option_b=row['option_b'],
                option_c=row['option_c'],
                option_d=row['option_d'],
                correct_answer=row['correct_answer'],
                difficulty_level=row.get('difficulty_level', '')
            )
