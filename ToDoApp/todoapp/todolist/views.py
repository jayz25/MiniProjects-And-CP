from django.shortcuts import render, redirect
from .models import Task
# Create your views here.
def index(request): #The Index View
    tasks = Task.objects.all()
    #Fetching All Tasks
    if request.method == "POST": #Checkinng POST Call
        if "taskAdd" in request.POST: # Checking If AddTask is called i.e Creating new Task
            title = request.POST["description"] #Getting description of new task
            date = str(request.POST["date"]) #Getting date for new task
            content = title + " -- " + date + " " #getting content for new tasl
            task = Task(title = title, content = content, due_date = date) #Creating new Task Instance 
            task.save() #Saving that new instance 
            return redirect("/") #Redirecting to same page after creating.. i.e Updated records

        if "taskDelete" in request.POST: #Checking If Deleting task in inputed
            checkedList = request.POST["checkedBox"] #Getting Checkcked Tasks i.e Completed Tasks in List
            for task_id in checkedList:
                task = Task.objects.get(id=int(task_id)) #Deleting By searching ID
                task.delete()
    return render(request, "index.html", {"tasks": tasks}) #Redirecting to Index with inputing tasks Dictionary contains tasks

