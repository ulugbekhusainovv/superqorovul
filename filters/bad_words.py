BAD_WORDS=['http', 'https', 'www','.com','@',"t.me"]

from aiogram.filters import BaseFilter
from aiogram import types


class CheckBadWords(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        if self.is_edited(message):
            return self.check_for_bad_words(message.text.lower())

        if (message.text and isinstance(message.text, str) and
                self.check_for_bad_words(message.text.lower())):
            return True

        if (message.caption and isinstance(message.caption, str) and
                self.check_for_bad_words(message.caption.lower())):
            return True

        return False

    def is_edited(self, message) -> bool:
        return message.edit_date is not None

    def check_for_bad_words(self, text: str) -> bool:
        return any(word in text for word in BAD_WORDS)
