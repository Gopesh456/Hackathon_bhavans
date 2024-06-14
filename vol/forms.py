from django.forms import ModelForm
from questions.models import answer, Questions

class answerForm(ModelForm):
    class Meta:
        model = answer
        fields = ['Result']


class questionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['question','ans1','ans2','ans3']