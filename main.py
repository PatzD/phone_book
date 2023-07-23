from uuid import UUID
from fastapi import FastAPI, HTTPException
from utils import contacts
from models import Contact
from utils import ContactsHelper

app = FastAPI()

"""
retrieve all contacts
"""
@app.get('/api/v1/contacts')
def get_contacts_list():
    return contacts

"""
reteieve one contact from id
"""
@app.get('/api/v1/contact/{contact_id}')
def get_contact(contact_id: UUID):
    return ContactsHelper.search_for_contact(contact_id)

"""
create a new contact, passing id is optional
"""
@app.post('/api/v1/contact')
def create_contact(contact: Contact):
    contacts.append(contact)
    
    return contact.id

"""
update an existing contact
"""
@app.put('/api/v1/contact/{contact_id}')
def update_contact(contact_id: UUID, updated_contact: Contact):    
    ContactsHelper.update_contact(contact_id, updated_contact)

    return updated_contact 

"""
delete an existing contact
"""
@app.delete('/api/v1/contact/{contact_id}')
def delete_contact(contact_id: UUID):
    return ContactsHelper.delete_contact(contact_id)
