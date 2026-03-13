from django.test import TransactionTestCase
from django.utils import timezone
from .models import Question, Choice

#TransactionTestCase
class TransactionTestCaseChoice(TransactionTestCase):
    def test_question(self):
        question = Question.objects.create(
            question_text = "What am I testing?",
            pub_date = timezone.now()
        )
        
        choice = Choice.objects.create(
            question = question,
            choice_text = "Transaction Test"
        )
        
        self.assertEqual(Choice.objects.count(), 1)
        self.assertEqual(choice.votes, 0)
        self.assertEqual(str(choice), "Transaction Test")