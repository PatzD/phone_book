from models import Contact
from uuid import UUID
from typing import List
from fastapi import HTTPException

contacts: List[Contact] = []

contact1 = Contact(name='Adam', surname='Doe', phone_number=123, email='ad@gmail.com')
contacts.append(contact1)

class ContactsHelper:
    """
    Searches for a contact in a given list of entries
    
    Takes id as input

    Returns the contact object if found
    Otherwise returns False
    """
    @classmethod
    def search_for_contact(cls, id: UUID):
        for contact in contacts:
            if contact.id == id: return contact
        raise HTTPException(status_code=404, detail='Contact not found')
    
    """
    Updates contact
    
    takes contact to update
    new data to update contact with 

    returns updated contact
    """
    @classmethod
    def update_contact(cls, contact_id: UUID, update_contact: Contact):
        contact_in = None

        for i, contact_search in enumerate(contacts):
            if contact_search.id == contact_id:
                contact_in = i
                break
        
        if contact_in is None:
            raise HTTPException(status_code=404, detail='Contact not found')
        
        contacts[contact_in] = update_contact

        return update_contact
    
    """
    delete a contact
    
    take contact id
    
    return deleted contact data
    """
    @classmethod 
    def delete_contact(cls, contact_id: UUID):
        if contact_id is None:
            raise HTTPException(status_code=404, detail='Contact was not found')

        contact_del = ContactsHelper.search_for_contact(contact_id)
        contacts.remove(contact_del)
        return contact_del
        
