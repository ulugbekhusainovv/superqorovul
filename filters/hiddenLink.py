from aiogram import types
from aiogram.filters import BaseFilter


class ContainsHiddenLink(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        if message:
            return self.contains_hidden_link(message=message)

        if self.is_edited(message):
            return self.contains_hidden_link(message=message)

        return False
    def is_edited(self, message: types.Message) -> bool:
        return message.edit_date is not None
    
    def contains_hidden_link(self, message) -> bool:
        # Qo'shilgan shartlar:
        if message.caption and message.caption_entities and any(entity.type == 'text_link' for entity in message.caption_entities):
            return True
        elif message.entities and any(entity.type == 'text_link' for entity in message.entities):
            return True
        else:
            return False
