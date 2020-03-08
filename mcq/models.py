from django.db import models


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class QuizModule(TimestampModel):
    test_name = models.CharField(max_length=255)

    class Meta:
        ordering = ["id"]


class Questions(TimestampModel):
    module = models.ForeignKey(QuizModule, on_delete=models.CASCADE)
    question = models.TextField(max_length=1000)

    def __str__(self):
        return f"Question - {self.id}"

    class Meta:
        ordering = ["id"]


class Options(TimestampModel):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="options")
    option = models.CharField(max_length=500)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return f"Option - {self.id}"
