from django.db import models
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

"""
class Campaigns(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    test_name = models.TextField()
    variant_name = models.TextField()
    start_time = models.FloatField()

    class Meta:
    #    managed = False
        db_table = 'campaigns'


class Injections(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    campaign_id = models.IntegerField()
    frame = models.IntegerField()
    word = models.IntegerField()
    bit = models.IntegerField()
    time = models.FloatField()
    injection_status = models.IntegerField()
    system_status = models.IntegerField()
    system_status_raw = models.IntegerField()
    recovery = models.IntegerField()
    net_speed = models.FloatField()
    transition = models.IntegerField()

    class Meta:
    #    managed = False
        db_table = 'injections'

class Logs(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    injection_id = models.IntegerField()
    position = models.IntegerField()
    master_value = models.BinaryField()
    slave_value = models.BinaryField()

    class Meta:
    #    managed = False
        db_table = 'logs'

class Sensitive_bits(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    injection_id = models.IntegerField()
    frame = models.IntegerField()
    word = models.IntegerField()
    bits = models.IntegerField()

    class Meta:
    #    managed = False
        db_table = 'sensitive_bits'
"""