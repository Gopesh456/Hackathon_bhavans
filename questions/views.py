from django.shortcuts import render, redirect
from .models import Questions,answer
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime,timedelta
import questions.checker.python_checker as pyC
# Create your views here.

@login_required(login_url='login')
def questions(req,pk):
    context = {
        'pk': str(pk)
    }
    if req.method == 'POST':
        userAns = req.POST['textarea']
        # print(questions)
        ans_q = Questions.objects.get(qno = pk)
        current_username = req.user.username
        if pk =='1':
            ans_q.ans = userAns.replace("input_data = eval(input())","import sys\ninput_data = eval(sys.argv[1])\ndel sys")
        elif pk =='2':
            ans_q.ans = userAns.replace("input_data = eval(input())","import sys\ninput_data = eval(sys.argv[1])\ndel sys")
        ans_q.save()
        ans_a = answer(username = current_username,ans = userAns)
        ans_a.qno = pk
        ans_a.create = datetime.now()
        print(ans_q.ans)
        now = datetime.now()
        current_time = str(now.strftime("%H_%M_%S"))
        pyChecker = pyC.PythonChecker(True)
        file_name = 'Answer/'+str(ans_a.qno)+'/'+current_username+"@"+current_time+".py"
        with open(file_name,'w+') as f:
            f.write(ans_q.ans)
        correct = False
        if pk == '1':
            result1_1 = pyChecker.check_python_file(1.1,file_name,['1234'])
            result1_2 = pyChecker.check_python_file(1.2,file_name,['4125'])
            result1_3 = pyChecker.check_python_file(1.3,file_name,['786'])
            if result1_1 and result1_2 and result1_3:
                correct = True
                print(result1_1, result1_2,result1_3)
            else:
                correct = False
                print(result1_1, result1_2,result1_3)
        elif pk == '2':
            result2_1 = pyChecker.check_python_file(2.1,file_name,['"hello"'])
            result2_2 = pyChecker.check_python_file(2.2,file_name,['"python"'])
            result2_3 = pyChecker.check_python_file(2.3,file_name,['"python hello"'])
            if result2_1 and result2_2 and result2_3:
                correct = True
                print(result2_1, result2_2,result2_3)
            else:
                correct = False
                print(result2_1, result2_2,result2_3)
        if correct:
            print("correct")
            ans_a.Result = 'Correct' 
            starttime = datetime(now.year, now.month, now.day, 22)  
            time_difference = now - starttime
            seconds = time_difference.total_seconds()
            points = seconds // 180 
            points *=10
            ans_a.points =int(400 - points)
            ans_a.save()
            return redirect('/questions/')  

        elif not correct:
            print("wrong")
            ans_a.Result = 'Incorrect'
            ans_a.save()       
            return redirect('/questions/') 

    return render(req,'questions/index.html',context)

def homepage(req):
    return render(req,'index.html')

def getques(req):
    questions = Questions.objects.all()
    return JsonResponse({'question':list(questions.values())})

@login_required(login_url='login')
def overview(req):
    
    context = {
        '1_QE' : answer.objects.filter(username = req.user.username, qno = '1').exists(),
        '2_QE' : answer.objects.filter(username = req.user.username, qno = '2').exists(),
        '3_QE' : answer.objects.filter(username = req.user.username, qno = '3').exists(),
        '4_QE' : answer.objects.filter(username = req.user.username, qno = '4').exists(),
        '5_QE' : answer.objects.filter(username = req.user.username, qno = '5').exists(),
        '6_QE' : answer.objects.filter(username = req.user.username, qno = '6').exists(),
        '7_QE' : answer.objects.filter(username = req.user.username, qno = '7').exists(),
        '8_QE' : answer.objects.filter(username = req.user.username, qno = '8').exists(),
        '9_QE' : answer.objects.filter(username = req.user.username, qno = '9').exists(),
        '10_QE' : answer.objects.filter(username = req.user.username, qno = '10').exists(),
    }
    context2 = {
        '1_QE' : '-',
        '2_QE' : '-',
        '3_QE' : '-',
        '4_QE' : '-',
        '5_QE' : '-',
        '6_QE' : '-',
        '7_QE' : '-',
        '8_QE' : '-',
        '9_QE' : '-',
        '10_QE' : '-',
#       'points':points,
        '1_P' : '0',
        '2_P' : '0',
        '3_P' : '0',
        '4_P' : '0',
        '5_P' : '0',
        '6_P' : '0',
        '7_P' : '0',
        '8_P' : '0',
        '9_P' : '0',
        '10_P' : '0',
    }

    for i in range(1,11):
        key = str(i)+'_QE'
        if context[key]:
            context2[key] = answer.objects.filter(username = req.user.username, qno = i).last().Result
            key2 = str(i)+'_P'
            context2[key2] = answer.objects.filter(username = req.user.username, qno = i).last().points # type: ignore
        else:
            pass


    return render(req,'questions/overview.html',context2)

    