from django.db import models
# Create your models here.
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid
import os
from datetime import datetime, timedelta
from datetime import date
from django.utils.timezone import now
import datetime
from multiselectfield import MultiSelectField
from decimal import Decimal
from smart_selects.db_fields import ChainedForeignKey,ChainedManyToManyField,GroupedForeignKey
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw  

def get_file_path1(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)

def get_file_path01(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)
    return os.path.join('working_emp', filename)   
def get_file_path02(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)
    return os.path.join('retired_emp', filename)     
def get_file_path2(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)
    return os.path.join('cartridges', filename)
def get_file_path3(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)
    return os.path.join('spareparts', filename)
def get_file_path4(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)
    return os.path.join('passrecovery', filename)
class Leave_Requests(models.Model):
      reasons=(('Work',' Work'),('Emergency','Emergency'))
      leave_type=(('With return',' With return'),('No Return','No Return'))
      employee_name = models.CharField(null=True,max_length=120, verbose_name='Employee Name ')
      department_name = models.CharField(max_length=120, verbose_name='Department Number ')
      time_to_leave = models.DateField(auto_now_add=True, auto_now=False,null=True)
      uuid = models.CharField(max_length=120,default=uuid.uuid4)
      qr_code    = models.ImageField(upload_to='qr_codes', blank=True)
      request_status = models.BooleanField(default=False)
      request_revised = models.BooleanField(default=False)  
      leave_reason = models.CharField(max_length=120,choices=reasons, verbose_name='Leaving For ... ')  
      leave_type = models.CharField(max_length=120,blank=True,choices=leave_type, verbose_name='Leave Type ')  

      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)

      def __str__(self):
          return str(self.uuid)

      def save(self, *args, **kwargs):
          qrcode_img = qrcode.make(self.uuid)
          canvas = Image.new('RGB', (290, 290), 'white')
          canvas.paste(qrcode_img)
          fname = f'qr_code-{self.uuid}.png'
          buffer = BytesIO()
          canvas.save(buffer,'PNG')
          self.qr_code.save(fname, File(buffer), save=False)
          canvas.close()
          super().save(*args, **kwargs)











