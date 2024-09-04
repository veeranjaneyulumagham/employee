from django.shortcuts import render,get_object_or_404
from salary.models import employee

# Create your views here.
def employee_detail(request,pk):
    employees=get_object_or_404(employee,pk=pk)
    context={
        'employees':employees,
    }
    return render(request,'employee_detail.html',context)