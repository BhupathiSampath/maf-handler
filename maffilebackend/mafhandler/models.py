import os
from django.db import models
from django.db.models.deletion import SET_DEFAULT
from authentication.models import Account
from django.core.validators import FileExtensionValidator
# Create your models here.

class MafFile(models.Model):
    data_entry                      = models.DateTimeField(verbose_name ="date joined", auto_now_add=True)
    username                        = models.ForeignKey(Account,verbose_name="username",to_field="username",on_delete=models.CASCADE)
    maf_file                        = models.FileField(max_length=300,null=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])], unique=True)

    # def __str__(self):
    #     return self.maf_file
