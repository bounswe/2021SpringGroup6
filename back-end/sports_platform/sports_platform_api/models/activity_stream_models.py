from django.db import models

class ActivityStream(models.Model):
    class Meta:
        db_table = 'activity_stream'

    type = models.CharField(max_length=30)
    actor = models.ForeignKey('User', on_delete=models.CASCADE)
    object = models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    target = models.ForeignKey('Event', null=True,on_delete=models.CASCADE)
    date = models.DateTimeField()
