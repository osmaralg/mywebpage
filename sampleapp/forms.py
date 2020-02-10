
from django.forms import Form, ModelForm
from .models import *

class ProjectForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        pass

    class Meta():
        fields = '__all__'
        model = Project
    '''
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    title = forms.CharField()
    website = forms.URLField()
    content = forms.CharField()
    image = forms.ImageField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    language = forms.ModelChoiceField(queryset=Language.objects.all())
    '''



