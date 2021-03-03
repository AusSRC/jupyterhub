from write_error import WriteError
from django.db import models
from run.models import Run


class Instance(models.Model):
    id = models.BigAutoField(primary_key=True)
    run = models.ForeignKey(Run, models.DO_NOTHING)
    filename = models.CharField(max_length=200)
    boundary = models.TextField()
    run_date = models.DateTimeField()
    flag_log = models.BinaryField(blank=True, null=True)
    reliability_plot = models.BinaryField(blank=True, null=True)
    log = models.BinaryField(blank=True, null=True)
    parameters = models.JSONField()
    version = models.CharField(max_length=200, blank=True, null=True)
    return_code = models.IntegerField(blank=True, null=True)
    stdout = models.BinaryField(blank=True, null=True)
    stderr = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance'
        unique_together = (('run', 'filename', 'boundary'),)

    def save(self, *args, **kwargs):
        raise WriteError('This table is read only.')