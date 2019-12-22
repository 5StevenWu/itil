from django import forms
from repository import models


class ServerForm(forms.ModelForm):
    class Meta:
        model = models.Server
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed in self.fields.values(): #有序字典
            filed.widget.attrs['class'] = 'form-control'
