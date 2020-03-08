from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from mcq.models import QuizModule
from . import serializer


class QuizListingAPI(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializer.QuizListingSerializer
    queryset = QuizModule.objects.all()
