from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from scores.models import TestInformation, TestDetailedInformation
from mcq.models import QuizModule, Questions, Options
from . import serializer
from rest_framework import status


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


class InitiateTestAPI(APIView):
    serializer_class = serializer.InitiateTestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() is False:
            return Response({"status": False, "message": serializer.errors, "data": None},
                            status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        module_id = data["module"]

        # Create Test Information and pass the ID to Angular.
        # Frontend Framework will store the id in local storage.
        test_information = TestInformation.objects.create(user=self.request.user,
                                                          module_id=module_id,
                                                          total_questions=Questions.objects.filter(
                                                              module_id=module_id).count(),
                                                          total_right_answers=0)

        return Response({"status": True, "message": "Test Initiated !", "data": {"test_id": test_information.id}},
                        status=status.HTTP_201_CREATED)


class SaveUserTestInformationAPI(APIView):
    serializer_class = serializer.SaveUserTestResponseSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() is False:
            return Response({"status": False, "message": serializer.errors, "data": None},
                            status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        question_id = data["question_id"]
        option_id = data["option_id"]
        test_information_id = data["test_information_id"]

        # Check Answer
        is_answer = Options.objects.get(question_id=question_id, id=option_id).is_answer

        # TestDetailedInformation
        TestDetailedInformation.objects.create(test_information_id=test_information_id,
                                               attempted_question_id=question_id,
                                               selected_option_id=option_id,
                                               is_answer_correct=is_answer)

        total_right_answers = TestDetailedInformation.objects.filter(test_information_id=test_information_id,
                                                                     is_answer_correct=True).count()
        # Update Test Information

        TestInformation.objects.filter(id=test_information_id).update(total_right_answers=total_right_answers)

        return Response({"status": True, "message": "Saved User Input !", "data": None}, status=status.HTTP_201_CREATED)
