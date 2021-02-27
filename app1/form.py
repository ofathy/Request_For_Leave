from django import forms

from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple
from django.db import models
from .models import  Leave_Requests
 





# -------------------------------------------------------------------------------------------------------
class Leave_request_form(forms.ModelForm):
      class Meta:
        model = Leave_Requests
        exclude = ['', '','']
        fields = ('leave_reason','leave_type')


      def __init__(self, *args, **kwargs):
        super(Leave_request_form, self).__init__(*args, **kwargs)
        # self.fields['problem_date'].widget.attrs['class'] = 'datepicker'
        # self.fields['problem_desc'].widget.attrs['class'] = 'tarea'

class Aprove_Reject_form(forms.ModelForm):
      class Meta:
        model = Leave_Requests
        exclude = ['', '','']
        fields = ('request_status','request_revised')


      def __init__(self, *args, **kwargs):
        super(Aprove_Reject_form, self).__init__(*args, **kwargs)
        # self.fields['problem_date'].widget.attrs['class'] = 'datepicker'
        # self.fields['problem_desc'].widget.attrs['class'] = 'tarea'        