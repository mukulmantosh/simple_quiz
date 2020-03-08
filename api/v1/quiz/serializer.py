from rest_framework import serializers
from mcq.models import QuizModule, Questions, Options
from scores.models import TestDetailedInformation, TestInformation


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


class InitiateTestSerializer(serializers.Serializer):
    module = serializers.IntegerField()


class SaveUserTestResponseSerializer(serializers.Serializer):
    test_information_id = serializers.IntegerField()
    question_id = serializers.IntegerField()
    option_id = serializers.IntegerField()
