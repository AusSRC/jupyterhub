# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from write_error import WriteError
from django.db import models
from run.models import Run
from instance.models import Instance


class Detection(models.Model):
    id = models.BigAutoField(primary_key=True)
    instance = models.ForeignKey(Instance, models.DO_NOTHING)
    run = models.ForeignKey(Run, models.DO_NOTHING)
    name = models.TextField(blank=True, null=True)
    x = models.DecimalField(max_digits=65535, decimal_places=12)
    y = models.DecimalField(max_digits=65535, decimal_places=12)
    z = models.DecimalField(max_digits=65535, decimal_places=12)
    x_min = models.IntegerField(blank=True, null=True)
    x_max = models.IntegerField(blank=True, null=True)
    y_min = models.IntegerField(blank=True, null=True)
    y_max = models.IntegerField(blank=True, null=True)
    z_min = models.IntegerField(blank=True, null=True)
    z_max = models.IntegerField(blank=True, null=True)
    n_pix = models.IntegerField(blank=True, null=True)
    f_min = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    f_max = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    f_sum = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    rel = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    rms = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    w20 = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    w50 = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    ell_maj = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    ell_min = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    ell_pa = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    ell3s_maj = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    ell3s_min = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    ell3s_pa = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    kin_pa = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    err_x = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    err_y = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    err_z = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    err_f_sum = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    ra = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    dec = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    freq = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    l = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    b = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    v_rad = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    v_opt = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    v_app = models.DecimalField(max_digits=65535, decimal_places=12, blank=True, null=True)
    unresolved = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'detection'
        unique_together = (('name', 'x', 'y', 'z', 'x_min', 'x_max', 'y_min', 'y_max', 'z_min', 'z_max', 'n_pix', 'f_min', 'f_max', 'f_sum', 'instance', 'run'),)

    def save(self, *args, **kwargs):
        raise WriteError('This table is read only.')

    def delete(self, *args, **kwargs):
        raise WriteError('This table is read only.')