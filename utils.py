from models import Contact
from uuid import UUID
from typing import List

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
        return False
    
    """
    Updates contact
    
    takes contact to update
    new data to update contact with 

    returns updated contact
    """
    @classmethod
    def update_contact(cls, contact_id: UUID, update_contact: Contact):
        for i, contact_search in enumerate(contacts):
            if contact_search.id == contact_id:
                contact_in = i
                break
        
        contacts[contact_in] = update_contact

        return update_contact
    

        
