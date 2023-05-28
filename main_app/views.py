from rest_framework import generics
from .models import Quiz
from .serializers import QuizSerializer
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.shortcuts import render


"""
# def quiz_view(request):  # We can continue to work on this view when we start working on front end
#     active_quiz = Quiz.active_quiz_objects.get_active_quiz()
#     return render(request, 'main_app/index.html', {'quiz': active_quiz})
"""

def documentation_view(request):  # A simple view for home page
    github_repo = "https://github.com/anankitpatne12/Main_Quiz_API.git"
    return render(request, 'main_app/index.html', { 'github_repo': github_repo})

class QuizCreateView(generics.CreateAPIView):  # create quiz
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        created_instance = serializer.instance
        serialized_data = serializer.data
        return JsonResponse(serialized_data)


class QuizActiveView(generics.RetrieveAPIView):  # get a specific active quiz
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.status != 'active':
            return JsonResponse({'error': 'Quiz is not active.'}, status=400)

        serializer = self.get_serializer(instance)
        serialized_data = serializer.data
        return JsonResponse(serialized_data)


@require_http_methods(["GET"])
def active_quizzes_view(request):   # get all the active quizzes
    current_time = timezone.now()
    active_quizzes = Quiz.objects.filter(
        start_date__lte=current_time, end_date__gte=current_time, status='active')
    quiz_data = []
    for quiz in active_quizzes:
        quiz_data.append({
            'id': quiz.id,
            'question': quiz.question,
            'options': quiz.options,
            'right_answer': quiz.right_answer,
            'start_date': quiz.start_date.isoformat(),
            'end_date': quiz.end_date.isoformat(),
            'status': quiz.status
        })
    return JsonResponse(quiz_data, safe=False)


class QuizResultView(generics.RetrieveAPIView):      # get quiz result
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # Check if 5 minutes have passed since the quiz ended
        end_time_plus_5 = instance.end_date + timezone.timedelta(minutes=5)
        current_time = timezone.now()
        if instance.status == 'active':  # check if quiz is active
            return JsonResponse({'error': 'Quiz is active. Come back once its over!'}, status=400)
        else:  # check for 5 minutes condition
            if current_time >= end_time_plus_5:
                serializer = self.get_serializer(instance)
                serialized_data = serializer.data
                return JsonResponse(serialized_data)
            else:
                return JsonResponse({'error': 'Result not available yet. Please check back after 5 minutes.'}, status=400)


class QuizAllView(generics.ListAPIView):   # get all quizzes
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):   # update quiz status
        now = timezone.now()
        Quiz.objects.filter(start_date__lte=now,
                            end_date__gte=now).update(status='active')
        Quiz.objects.filter(end_date__lt=now).update(status='finished')
        return super().get_queryset()

    def list(self, request, *args, **kwargs):  # return serialized data
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        serialized_data = serializer.data
        return JsonResponse(serialized_data, safe=False)
