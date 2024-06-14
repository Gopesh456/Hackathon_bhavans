from django.shortcuts import render,redirect
from questions.models import answer,Questions
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import answerForm,questionForm
# Create your views here.

@login_required(login_url='login')
def vol(req):
    current_username = req.user.username
    if current_username == 'volunteer.hackathon' or current_username == 'Gopesh' or current_username == 'admin':

        return render(req,'vol/index.html')
    else:
        # print(adminRole)
        return redirect('/questions')

def getAnswer(req):
    # ans = answer.objects.all()
    # return JsonResponse({'ans': list(ans.values())})
    ques = Questions.objects.all()
    return JsonResponse({'ans': list(ques.values())})

def answerChecker(request,pk):
    ques = Questions.objects.get(qno = pk)
    qno = ques.qno
    question = ques.question
    ans1 = ques.ans1
    ans2 = ques.ans2
    ans3 = ques.ans3
    intial_data = {
        'question': question,
        'ans1': ans1,
        'ans2': ans2,
        'ans3': ans3,
    }
    form = questionForm(initial=intial_data)
    context = {
        'qno': qno,
        'question': question,
        'form': form,
    }
    form = questionForm(instance=ques)
    if request.method == 'POST':
        form = questionForm(request.POST,instance=ques)
        if form.is_valid():
            form.save()
            return redirect('/vol/')

    return render(request,'vol/answer.html',context)