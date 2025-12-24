from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.contacts import ContactRepository


class ContactService:
    def __init__(self, session: AsyncSession):
        self.repo = ContactRepository(session)

    async def create_contact(self, data):
        return await self.repo.create(data)

    async def list_contacts(self, query=None):
        return await self.repo.get_all(query)

    async def get_contact(self, contact_id):
        return await self.repo.get_by_id(contact_id)

    async def update_contact(self, contact, data):
        return await self.repo.update(contact, data)

    async def delete_contact(self, contact):
        await self.repo.delete(contact)

    async def birthdays(self):
        return await self.repo.upcoming_birthdays()
