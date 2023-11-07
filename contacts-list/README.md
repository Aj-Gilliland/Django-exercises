# Contacts List - Models

For this exercise, you will implement a model and some helper functions that perform tasks similar to the Python Fundamentals "Contacts List" exercise.

To do this, you should make a `Contact` model with fields for each of these pieces of information:

- `name`: A string representing the contact's name
- `email`: A string representing the contact's email address
- `phone`: A string representing the contact's phone number
- `is_favorite`: A boolean representing whether or not this contract is a "favorite".

Additionally, you should create each of the following functions.
 
- [ ] `app.models.create_contact(name, email, phone, is_favorite)` - The user can create an arbitrary amount of contacts.
- [ ] `app.models.all_contacts()` - The user should be able to view all of the contacts at once.
- [ ] `app.models.find_contact_by_name(name)` - The user should be able to search for a contact by name.
- [ ] `app.models.favorite_contacts()` - The user should be able to view the favorite contacts.
- [ ] `app.models.update_contact_email(name, new_email)` - The user should be able to search for a contact by name and update their information.
- [ ] `app.models.delete_contact(name)` - The user should be able to delete contact by name.
