from django.db import models
from django.utils import timezone
import datetime
 
class Poll(models.Model):
  question = models.CharField(max_length=200)
  pub_data = models.DateTimeField('data published')

  def __unicode__(self):
    return self.question
    return '(%s, %s)' % (self.question, self.pub_data)

  def was_published_recently(self):
    now = timezone.now()
    return now > self.pub_data >= now - datetime.timedelta(days=1)

class Choice(models.Model):
  poll = models.ForeignKey(Poll)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __unicode__(self):
    return self.choice_text
    return '(%s, %s, %s)' % (self.poll, self.choice_text, self.votes)
