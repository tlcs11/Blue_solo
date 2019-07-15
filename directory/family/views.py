from django.shortcuts import render , redirect
# from django.http import HttpResponse

from .models import Person

# Create your views here.
def family(request):
    return render(request, "family/home.html")

def directory_view(request):

    people = Person.objects.all().order_by("branch")[:5]

    chandler = Person.objects.filter(branch="Chandler")[:2]

    lapsley = Person.objects.filter(branch="Lapsley")[:2]

    fowlkes = Person.objects.filter(branch="Fowlkes")[:2]

    lovelace = Person.objects.filter(branch="Lovelace")[:2]

    sullivan = Person.objects.filter(branch="Sullivan")[:2]
    

    context = {
        "people": people,
        "chandler": chandler,
        "lapsley": lapsley,
        "fowlkes": fowlkes,
        "lovelace": lovelace,
        "sullivan": sullivan
        
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

def delete_family(request, id):
    to_delete = Person.objects.get(id=id)
    to_delete.delete()
    return redirect('directory')

    context = {
        "id": id
    }
    
    return render(request, 'family/directory_view.html', context=context)


    # if request.method =="POST":

    #     to_delete = Person.objects.get(id=request.POST['id'])

    #     to_delete.delete()

    #     return redirect('directory')

    # return render(request, 'family/input.html')

def update_family(request, id):
    to_update = Person.objects.get(id=id)
    if request.method == "POST":

        
        for key, value in request.POST.items():
            
            if (value and key != "csrfmiddlewaretoken"):
                setattr(to_update, key, value)

            to_update.save()

        
        return redirect('directory')

    context = {
        "id": id,
        "update_person":to_update
    }
    
    return render(request, 'family/update.html', context=context)
    
        