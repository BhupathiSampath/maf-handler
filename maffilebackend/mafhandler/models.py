import os
from django.db import models
from django.db.models.deletion import SET_DEFAULT
from authentication.models import Account
from django.core.validators import FileExtensionValidator
import hashlib
from functools import partial
# Create your models here.
def hash_file(maf_file, block_size=65536):
    hasher = hashlib.md5()
    for buf in iter(partial(maf_file.read, block_size), b''):
        hasher.update(buf)

    return hasher.hexdigest()

def user_directory_path(instance, filename):
    # hash_file(instance.maf_file.open())
    # filename_base, filename_ext = os.path.splitext(filename)
    
        # .format(instance.username.username, filename)
    return "user_{0}/{1}".format(instance.username.username, filename)
class MafFile(models.Model):
    data_entry                      = models.DateTimeField(verbose_name ="date joined", auto_now_add=True)
    username                        = models.ForeignKey(Account,verbose_name="username",to_field="username",on_delete=models.CASCADE)
    maf_file                        = models.FileField(upload_to=user_directory_path,max_length=3000,null=True, validators=[FileExtensionValidator(allowed_extensions=['pdf','tsv'])], unique=True)

    def __str__(self):
        return self.maf_file.name
    