from django.shortcuts import render
from . models import *
#from . forms import StudentForm
# Create your views here.

def index(request):
    """ if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
        else:
            context = {'form':form}
            return render(request, 'results/index.html', context)
    context = {
        "form" : StudentForm(),
        "results" : Student.objects.all()
    } """
    
    totalcredit = CourseList.objects.count()
    creditval = []
    weightedgp_val = []
    
    i = 0
    incre = 1
    while incre <= totalcredit:
        course_credit = CourseList.objects.get(id = i + incre).coursecredit
        weighted_gp = CourseList.objects.get(id = i + incre).weightedgp
        creditval.append(course_credit)
        weightedgp_val.append(weighted_gp)
        incre = incre + 1
    
    a = 0
    b = 0
    newinc = 0
    while newinc < len(creditval):
        a += creditval[newinc]
        b += weightedgp_val[newinc]
        newinc = newinc + 1
    
    
    # Calculate the GPA by dividing the total WGP by total credit
    c = b / a
    context = {
        "studentmatric" : Student.objects.get(matricno  = "BU20CIT1073").matricno.upper(),
        "studentfname" : Student.objects.get(matricno  = "BU20CIT1073").first_name.upper(),
        "studentlname" : Student.objects.get(matricno  = "BU20CIT1073").last_name.upper(),
        "studentprogramme" : Student.objects.get(matricno  = "BU20CIT1073").programme.upper(),
        "studentcollege" : Student.objects.get(matricno  = "BU20CIT1073").college.upper(),
        "studentlevel" : Student.objects.get(matricno  = "BU20CIT1073").level,
        "course1" : CourseList.objects.get(id = 1),
        "course2" : CourseList.objects.get(id = 2),
        "course3" : CourseList.objects.get(id = 3),
        "course4" : CourseList.objects.get(id = 4),
        "course5" : CourseList.objects.get(id = 5),
        "credits" : a,
        "totalwgp" : b,
        "gradepa" : c
        
    }
    return render(request, "results/index.html", context)
