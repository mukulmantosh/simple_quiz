from django.db import models
from django.contrib.auth.models import User
from mcq.models import TimestampModel, QuizModule, Questions, Options


class TestInformation(TimestampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(QuizModule, on_delete=models.CASCADE)
    total_questions = models.PositiveIntegerField()
    total_right_answers = models.IntegerField()


class TestDetailedInformation(TimestampModel):
    test_information = models.ForeignKey(TestInformation, on_delete=models.CASCADE)
    attempted_question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Options, on_delete=models.CASCADE)
    is_answer_correct = models.BooleanField(default=False)
