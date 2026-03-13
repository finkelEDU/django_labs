from django.test import TestCase
from django.utils import timezone
from .models import Question, Choice

#Both TestCases are in this file
class ChoiceModelTestCase(TestCase):
    def setUp(self):
        self.question = Question.objects.create(
            question_text = "This is a test question",
            pub_date=timezone.now()
        )
    
    def test_string(self):
        choice = Choice.objects.create(
            question = self.question,
            choice_test = "The sky"
        )
        self.assertEqual(str(choice), "The sky")
        
    def test_votes(self):
        choice = Choice.objects.create(
            question = self.question,
            choice_text = "The sky"
        )
        self.assertEqual(choice.votes, 0)