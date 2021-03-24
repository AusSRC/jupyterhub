from write_error import WriteError
from django.db import models
from run.models import Run


class Instance(models.Model):
    id = models.BigAutoField(primary_key=True)
    run = models.ForeignKey(Run, models.DO_NOTHING)
    filename = models.TextField()
    boundary = models.TextField()
    run_date = models.DateTimeField()
    flag_log = models.BinaryField(blank=True, null=True)
    reliability_plot = models.BinaryField(blank=True, null=True)
    log = models.BinaryField(blank=True, null=True)
    parameters = models.JSONField()
    return_code = models.IntegerField(null=True)
    version = models.CharField(max_length=512, blank=True, null=True)
    stdout = models.BinaryField(blank=True, null=True)
    stderr = models.BinaryField(blank=True, null=True)

    def __unicode__(self):
        return f"{str(self.id)}"

    def __str__(self):
        return f"{str(self.id)}"

    class Meta:
        managed = False
        db_table = 'instance'
        unique_together = (('run', 'filename', 'boundary'),)

    def save(self, *args, **kwargs):
        raise WriteError('This table is read only.')

    def delete(self, *args, **kwargs):
        raise WriteError('This table is read only.')
