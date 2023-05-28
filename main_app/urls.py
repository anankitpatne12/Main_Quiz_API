from django.urls import path
from main_app.views import QuizCreateView, QuizActiveView, QuizResultView, QuizAllView, active_quizzes_view, documentation_view

app_name = 'main_app'

urlpatterns = [
    path('', documentation_view, name='documentation'),
    path('quizzes/', QuizCreateView.as_view(), name='quizzes_create'),  # create quiz
    path('quizzes/active/<int:pk>/', QuizActiveView.as_view(), name='quizzes_active'),  # get specific active quiz by id
    path('quizzes/<int:pk>/result/', QuizResultView.as_view(), name='quizzes_result'),  # get quiz result
    path('quizzes/all/', QuizAllView.as_view(), name='quizzes_all'),   # get all quizzes    
    path('quizzes/active/', active_quizzes_view, name='active_quizzes'),  # get all active quizzes
    # path('quiz/', quiz_view, name='quiz'),
]
