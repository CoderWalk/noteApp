from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Note
from .form import NoteCreationForm,NoteUpdationForm
# Create your views here.
def index(request):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,'notes/index.html',{})

def home(request):
    notes=Note.objects.all()
    form=NoteCreationForm()
    if(request.method=='POST'):
        form=NoteCreationForm(request.POST)
        if(form.is_valid()):
            note_to_save=form.save(commit=False)
            note_to_save.author=request.user
            note_to_save.save()
            return redirect('home')

    context={
        'notes':notes,
        'form':form,
    }
    return render(request,'notes/home.html',context)

#def login(request):
#    return render(request,'')

def loggedout(request):
    return render(request,'notes/loggedout.html')

def register(request):
    if(request.method=='POST'):
        form=UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request,'Account Created Successfully')
            return redirect('login')
    else:
        form = UserCreationForm()
    context={
        'form':form,
    }
    return render(request,'notes/register.html',context)

def settings(request):
    return render(request,'notes/settings.html')

def update(request,id):
    note_to_update = Note.objects.get(id=id)
    form = NoteUpdationForm(instance=note_to_update)

    if (request.method == 'POST'):
        form = NoteUpdationForm(request.POST)

        if (form.is_valid()):
            note_to_update.title = form.cleaned_data['title']
            note_to_update.description = form.cleaned_data['description']

            note_to_update.save()
            return redirect('home')
    context = {
        'note': note_to_update,
        'form': form
    }
    return render(request,'notes/update.html',context)


def delete(request,id):
    note_to_delete = Note.objects.get(id=id)
    note_to_delete.delete()
    return redirect('home')