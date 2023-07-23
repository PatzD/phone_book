from uuid import UUID
from fastapi import FastAPI, HTTPException
from utils import contacts
from models import Contact
from utils import ContactsHelper

app = FastAPI()


@app.get('/api/v1/contacts')
def get_contacts_list():
    return contacts

@app.get('/api/v1/contact/{contact_id}')
def get_contact(contact_id: UUID):
    return ContactsHelper.search_for_contact(contact_id)

@app.post('/api/v1/contact')
def create_contact(contact: Contact):
    contacts.append(contact)

    return contact.id

@app.put('/api/v1/contact/{contact_id}')
def update_contact(contact_id: UUID, updated_contact: Contact):
    contact = ContactsHelper.search_for_contact(contact_id)
    if contact is None:
        raise HTTPException(status_code=404, detail='Contact not found')
    
    ContactsHelper.update_contact(contact_id, updated_contact)

    return updated_contact 

@app.delete('/api/v1/contact/{contact_id}')
def delete_contact(contact_id: UUID):
    contact_to_delete = ContactsHelper.search_for_contact(contact_id)
    if contact_to_delete is None:
         raise HTTPException(status_code=404, detail='Contact was not found')

    deleted_contact = contact_to_delete
    contacts.remove(contact_to_delete)

    return deleted_contact