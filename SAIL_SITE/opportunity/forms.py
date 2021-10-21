from django import forms
from django.utils.translation import activate
from .models import Opportunity

class OppForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = [
            'name',
            'email',
            'phone',
            'company',
            'role',
            'branch',
            'year',
            'program',
            'tags',
            'desc',
            'doc',
            'active',
        ]