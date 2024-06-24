from django.shortcuts import render
from core1.models import Student 

# Create your views here.
def studentinfo(request):
    stud = Student.objects.all()
    print(stud)
    return render(request, 'core/student.html',{'stu':stud})