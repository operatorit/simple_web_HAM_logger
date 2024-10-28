from django import forms

from .models import Activity, Contact

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['text']
        labels = {'text': 'Activity name'}

class QSOForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['my_ref',
                  'my_call',
                  'your_call',
                  'freq',
                  'mode',
                  'sent_report',
                  'received_report',
                  'your_ref',
                  ]
        labels = {'my_ref': 'my reference: ',
                  'my_call': 'My call: ', 
                  'your_call': 'Correspondent call:',
                  'freq': 'FQ',
                  'mode': 'mode',
                  'sent_report': 'RST sent',
                  'received_report': 'RST received',
                  'your_ref': 'Correspondent reference',
                  }
