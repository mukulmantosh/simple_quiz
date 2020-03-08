from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from mcq.models import QuizModule, Questions, Options


class Command(BaseCommand):
    help = 'Create Sample Questions, Options in DB.'

    def handle(self, *args, **kwargs):
        # Delete existing data stored in db.
        QuizModule.objects.filter().delete()

        # Dummy Set 1
        quiz_module = QuizModule.objects.create(test_name=f"Python Quiz - {get_random_string()}")
        question = Questions.objects.create(question="Who developed Python ?", module=quiz_module)
        Options.objects.create(question=question, option="James Gosling")
        Options.objects.create(question=question, option="Guido van Rossum", is_answer=True)
        Options.objects.create(question=question, option="Bill Gates")
        Options.objects.create(question=question, option="Larry Page")

        # Dummy Set 2
        quiz_module = QuizModule.objects.create(test_name=f"General Quiz - {get_random_string()}")
        question = Questions.objects.create(question="Who is the current prime minister of India", module=quiz_module)
        Options.objects.create(question=question, option="Narendra Modi", is_answer=True)
        Options.objects.create(question=question, option="Rahul Gandhi")
        Options.objects.create(question=question, option="Mamta Banerjee")
        Options.objects.create(question=question, option="Arvind Kejriwal")

        print("Question Bank Successfully Dumped !")