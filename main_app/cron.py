from django_cron import CronJobBase, Schedule
from django.utils import timezone
from .models import Quiz

class UpdateQuizStatusCronJob(CronJobBase):
    RUN_EVERY_MINS = 5  # Run every 5 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'main_app.cron.UpdateQuizStatusCronJob'    # Unique code for this cron job

    def do(self):
        now = timezone.now()
        quizzes = Quiz.objects.filter(start_date__lte=now, status='inactive')
        for quiz in quizzes:
            quiz.status = 'active'
            quiz.save()
