from django.shortcuts import render
from students.models import Student
from students.forms import StudentForm

def index(request):
    context = {}
    form  = StudentForm()
    students = Student.objects.all()
    context['students'] = students
    context['title'] = 'Home'
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = StudentForm(request.POST)
            else:
                student = Student.objects.get(id=pk)
                form = StudentForm(request.POST, instance=student)
            form.save()
            form = StudentForm()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            student = Student.objects.get(id=pk)
            student.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            student = Student.objects.get(id=pk)
            form = StudentForm(instance=student)

    context['form'] = form

    return render(request, "index.html", context)

def details(request): 
    context = {}
    students = Student.objects.all()
    context['students'] = students
    context['title'] = 'Details'
    return render(request, 'details.html', context)