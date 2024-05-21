from email.policy import HTTP
from re import T
import re
from django.shortcuts import render, redirect
from .models import Questions,answer,TotalPoints
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime,timedelta
import questions.checker.python_checker as pyC
from threading import Timer
# Create your views here.




@login_required(login_url='login')
def questions(req,pk):
    context = {
        'pk': str(pk),
        'result': 'not working',
        'output': '',
    }
    if req.method == 'POST':
        userAns = req.POST['textarea']
        ans_q = Questions.objects.get(qno = pk)
        current_username = req.user.username
        if pk =='1':
            ans_q.ans = userAns.replace("input_data = input()","import sys\ninput_data = eval(sys.argv[1])\ndel sys")
        elif pk =='2':
            ans_q.ans = userAns.replace("input_data = input()","import sys\ninput_data = eval(sys.argv[1])\ndel sys")
        ans_q.save()
        ans_a = answer(username = current_username,ans = userAns)
        ans_a.qno = pk
        ans_a.create = datetime.now()
        print(ans_q.ans)
        now = datetime.now()
        current_time = str(now.strftime("%H_%M_%S"))
        pyChecker = pyC.PythonChecker(True)
        file_nameC = 'Answer/'+str(ans_a.qno)+'/'+current_username+".py"
        with open(file_nameC,'w+') as f:
            f.write(ans_q.ans) # type: ignore
        correct = False
        if pk == '1':
            result1_1 = pyChecker.check_python_file(1.1,file_nameC,['1234'], current_username)
            result1_2 = pyChecker.check_python_file(1.2,file_nameC,['4125'], current_username)
            result1_3 = pyChecker.check_python_file(1.3,file_nameC,['786'], current_username)
            if result1_1 and result1_2 and result1_3:
                correct = True
                print(result1_1, result1_2,result1_3)
            else:
                correct = False
                print(result1_1, result1_2,result1_3)
        elif pk == '2':
            result2_1 = pyChecker.check_python_file(2.1,file_nameC,['"hello"'])
            result2_2 = pyChecker.check_python_file(2.2,file_nameC,['"python"'])
            result2_3 = pyChecker.check_python_file(2.3,file_nameC,['"python hello"'])
            if result2_1 and result2_2 and result2_3:
                correct = True
                print(result2_1, result2_2,result2_3)
            else:
                correct = False
                print(result2_1, result2_2,result2_3)
        if correct:
            print("correct")
            ans_a.Result = 'Correct' 
            context['result'] = "Correct"
            print(context['result'])
            starttime = datetime(now.year, now.month, now.day,14)  
            time_difference = now - starttime
            seconds = time_difference.total_seconds()
            points = seconds // 180 
            print(points)
            points *=10
            ans_a.points =int(400 - points)
            ans_a.save()
            return redirect('/questions/')  

        elif not correct:
            print("wrong")
            ans_a.Result = 'Incorrect'
            context['result'] = "Incorrect"
            ans_a.save()       
            return redirect('/questions/') 

    return render(req,'questions/index.html',context)

def homepage(req):
    return render(req,'index.html')
def getCorrect(req):

    checkExists =  answer.objects.filter(username = req.user.username, qno = str(req.POST['qno'])).exists()
    if  not checkExists or answer.objects.filter(username = req.user.username, qno = req.POST['qno'] ).last().Result == 'Incorrect' :
            current_username = req.user.username
            now = datetime.now()
            ans_a = answer(username = current_username,ans = req.POST['code'])
            ans_a.qno = req.POST['qno']
            ans_a.create = datetime.now()
            ans_a.Result = req.POST['result']
            if ans_a.Result == 'Correct':
                starttime = datetime(now.year, now.month, now.day,0)  
                time_difference = now - starttime
                seconds = time_difference.total_seconds()
                points = seconds // 180 
                points *=10
                ans_a.points =int(400 - points)
                ans_a.save()
            ans_a.save()
    else:
        pass
    return redirect('/questions/') 
def getConsoleOutput(req):
    pass

def getques(req):
    questions = Questions.objects.all()
    return JsonResponse({'question':list(questions.values())})

def getPoints(req):
    ptsLi = []
    for i in range(1,11) :
        try:
            pts= answer.objects.filter(username = req.user.username, qno = str(i)).last().points  #type: ignore  
        except:
            pts = 0
        ptsLi.append(pts)
    return JsonResponse({'points':ptsLi}) 

def getResults(req):
    resLi = []
    for i in range(1,11) :
        try:
            res= answer.objects.filter(username = req.user.username, qno = str(i)).last().Result # type: ignore   
        except:
            res = '-'
        resLi.append(res)
    return JsonResponse({'results':resLi})

def updatingTotalPoints(req):
    current_username = req.user.username
    pointsDB = TotalPoints.objects.get(username = current_username)
    pts = 0
    for i in range(1,11):
        try:
            pts += answer.objects.filter(username = req.user.username, qno = str(i)).last().points  #type: ignore  
        except:
            pass
    pointsDB.points = int(pts)
    pointsDB.save()


def leaderboard(req):
    return render(req,'questions/leaderboard.html')
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
    totalPoints = 0

    for i in range(1,11):
        key = str(i)+'_QE'
        if context[key]:
            context2[key] = answer.objects.filter(username = req.user.username, qno = i).last().Result # type: ignore
            key2 = str(i)+'_P'
            context2[key2] = answer.objects.filter(username = req.user.username, qno = i).last().points # type: ignore
        else:
            pass
    
    Timer(1000,updatingTotalPoints(req)).start()
    return render(req,'questions/overview.html',context2)


