from django.shortcuts import render
from salary.models import employee
def information(request):
    employees=employee.objects.all()
    context={
        'employees':employees,
    }

    return render(request,'home.html',context)