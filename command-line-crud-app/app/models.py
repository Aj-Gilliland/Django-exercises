from django.db import models
#main idea (expandable)
#backend for a base camp stat tracker



#id like this to track leave
#where you are kl











class BaseCamper(models.Model):
        first_name = models.CharField(max_length=200) #likely text field or char
        last_name = models.CharField(max_length=200) #likely text field or char
        leadership_team = models.CharField(max_length=200, null=False, blank=False) #likely text field or char #!!!search for list of people on a team!!!
        module_status = models.CharField(max_length=200)  #number that will increment on command #!!! can attach function to search for people on the same thing for help !!!!
        leave_left_hour = models.CharField(max_length=100) #should likely be float and increment on command #!!!once the login features are added you'll be able to view your leave in a easy manner!!!

        def __str__(self):
                return self.name
        
#methods (see params for method ideas) at the very least the project requires that it add, update, and delete the people and all their data

#!!!add!!!
def create_camper(first_name, last_name, leadership_team, module_status, leave_left_hour):
    entry = BaseCamper(first_name=first_name, last_name=last_name, leadership_team=leadership_team, module_status=module_status, leave_left_hour=leave_left_hour)     
    entry.save()
    return entry

#!!!update functions drawn out into the 3 things you should be able to change (team,mod,and leave)!!!
def update_module(id, new_module_status):
    person = BaseCamper.objects.get(id=id)
    person.module_status = new_module_status
    person.save()
    return person

def update_team(id, new_leadership_team):
    person = BaseCamper.objects.get(id=id)
    person.leadership_team = new_leadership_team
    person.save()
    return person

def update_leave(id, new_leave_left_hour):
    person = BaseCamper.objects.get(id=id)
    person.leave_left_hour = new_leave_left_hour
    person.save()
    return person

#!!!delete!!!
def delete_camper(id):
    entry = BaseCamper.objects.get(id=id)
    entry.delete()
    return None



#extras I might expand on into a admin panel later
def all_campers():#not for display in individuals screens 
    return BaseCamper.objects.all()

def team_lister(team):
    return BaseCamper.objects.filter(leadership_team = team)

def find_id_by_name(first_name,last_name):
    person = BaseCamper.objects.filter(first_name=first_name, last_name=last_name)
    return person.id


       






