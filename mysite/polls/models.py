from django.db import models # <-- Bu sətir 'models' obyektini təyin edir
from django.utils import timezone
import datetime # 'datetime' modulunu import edir

# --- Question modeli ---
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def _str_(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        # Tutorial 6-ya uyğun: 1 gündən az keçibsə və gələcək deyilsə
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
# --- Choice modeli ---
class Choice(models.Model): # <-- 'Choice' sinfinin 'C' hərfi böyük olmalıdır
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def _str_(self):
        return self.choice_text