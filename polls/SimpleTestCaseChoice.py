from django.test import SimpleTestCase

#SimpleTestCase
class ChoiceSimpleTest(SimpleTestCase):
    class TestQuestion:
        pass
    
    class TestChoice:
        def __init__(self, question, choice_text):
            self.question = question
            self.choice_text = choice_text
            
        def __str__(self):
            return self.choice_text
            
    def test_string_choice(self):
        test_question = self.TestQuestion()
        choice = self.TestChoice(question=test_question, choice_text="The sky")
        self.assertEqual(str(choice), "The sky")