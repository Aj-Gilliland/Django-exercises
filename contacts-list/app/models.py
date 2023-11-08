from django.db import models

class Contact(models.Model):
        name = models.CharField(max_length=200)
        email = models.CharField(max_length=200, null=False, blank=False, unique=True)
        phone = models.CharField(max_length=200)
        is_favorite= models.BooleanField(default=False)

        def __str__(self):
                return self.name

def create_contact(name, email, phone, is_favorite):
        entry = Contact(name=name, email=email, phone=phone, is_favorite=is_favorite)     
        entry.save()
        return entry

def delete_contact(name):
        whole_contact = Contact.objects.get(name=name)
        whole_contact.delete()
        return whole_contact

def all_contacts():
        return Contact.objects.all()  

def find_contact_by_name(name):
       try:
        return Contact.objects.get(name=name)
       except:
        return None
       
def favorite_contacts():
        return Contact.objects.filter(is_favorite = True)

def update_contact_email(name, new_email):
        contact = Contact.objects.get(name=name)
        contact.email = new_email
        contact.save()
        return contact




