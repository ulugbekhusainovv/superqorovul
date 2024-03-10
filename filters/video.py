from aiogram import types
from aiogram.filters import BaseFilter

class IsVideo(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        document_video = False

        if message.document and message.document.file_name:
            video_extensions = (".mp4", ".m4v", ".m4p", ".avi", ".mov", ".mkv", ".wmv", ".flv")
            document_video = message.document.file_name.endswith(video_extensions)
        if message.video or document_video or message.video_note:
            return True
        return False
    