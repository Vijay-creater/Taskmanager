from .models import TaskStatus

def checkbulkcreations():
   if TaskStatus.objects.all().exists() == False:
      StatusCreation()

def  StatusCreation():
     TaskStatus.objects.bulk_create([
        TaskStatus(Status_name ='Not Started'),
        TaskStatus(Status_name ='In Progress'),
        TaskStatus(Status_name ='On Hold'),
        TaskStatus(Status_name ='Completed'),
        TaskStatus(Status_name ='Canceled'),
    ])