from django.shortcuts import render , redirect
# from django.http import HttpResponse

from .models import Person

# Create your views here.
def family(request):
    return render(request, "family/home.html")

def directory_view(request):

    people = Person.objects.all().order_by("branch")

    chandler = Person.objects.filter(branch="chandler")
    

    context = {
        "people": people,
        "chandler": chandler
        
    }

    return render(request,'family/directory_view.html', context=context)



def add_family(request): 

    if request.method =="POST":

        new_family = Person(first_name=request.POST['first'],
                            last_name=request.POST['last'],
                            schools=request.POST['schools'],
                            occupation=request.POST['occupation'],
                            branch=request.POST['branch'])
        
        new_family.save()        

        return redirect('directory')

    return render(request, 'family/input.html')

def delete_family(request):

    if request.method =="POST":

        to_delete = Person.objects.get(id=request.POST['id'])

        to_delete.delete()

        return redirect('directory')

    return render(request, 'family/input.html')
