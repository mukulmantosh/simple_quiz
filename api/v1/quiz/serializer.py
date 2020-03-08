from rest_framework import serializers
from mcq.models import QuizModule, Questions, Options


class QuizListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizModule
        fields = ("id", "test_name")


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ("id", "option")


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Questions
        fields = ("id", "question", "options")
