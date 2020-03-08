from rest_framework import serializers
from mcq.models import QuizModule


class QuizListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizModule
        fields = ("id", "test_name")
