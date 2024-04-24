from django.shortcuts import render,redirect
from questions.models import answer
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import answerForm
# Create your views here.

@login_required(login_url='login')
def vol(req,pk):
    context = {'pk':pk}
    current_username = req.user.username
    if current_username == 'volunteer.hackathon' or current_username == 'Gopesh':

        return render(req,'vol/index.html',context)
    else:
        # print(adminRole)
        return redirect('/questions')

def getAnswer(req):
    ans = answer.objects.all()
    return JsonResponse({'ans': list(ans.values())})

def answerChecker(request,pk):
    ans = answer.objects.get(id = pk)
    form = answerForm()
    qno = ans.qno
    context = {
        'answer' : ans.ans,
        'time': ans.create,
        'qno': ans.qno,
        'username': ans.username,
        'result': ans.Result,
        'form': form
    }
    form = answerForm(instance=ans)
    if request.method == 'POST':
        form = answerForm(request.POST,instance=ans)
        if form.is_valid():
            form.save()
            return redirect('/vol/'+str(qno))
    return render(request,'vol/answer.html',context)