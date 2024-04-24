from django.forms import ModelForm
from questions.models import answer

class answerForm(ModelForm):
    class Meta:
        model = answer
        fields = ['Result']