from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from mcq.models import QuizModule, Questions
from . import serializer


class QuizListingAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializer.QuizListingSerializer
    queryset = QuizModule.objects.all()


class QuestionListingAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializer.QuestionSerializer

    def get_queryset(self, **kwargs):
        try:
            module_id = self.request.query_params['module_id']
        except:
            raise ValidationError({"error": "Module Id Required !"})

        return Questions.objects.filter(module_id=module_id)
