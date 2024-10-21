import base64
import uuid

from django.conf import settings
from django.core.files.storage import Storage
from django.core.files.uploadedfile import UploadedFile
from imagekitio import ImageKit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions


class ImageKitStorage(Storage):
    def __init__(self, *args, **kwargs):
        self.imagekit = ImageKit(
            private_key=settings.IMAGEKIT_PRIVATE_KEY,
            public_key=settings.IMAGEKIT_PUBLIC_KEY,
            url_endpoint=settings.IMAGEKIT_URL_ENDPOINT
        )
        super().__init__(*args, **kwargs)

    def _save(self, name, content):
        options = UploadFileRequestOptions(
            use_unique_file_name=False,
            tags=['abc', 'def'],
            folder='/etovar/',

        )
        content = UploadedFile(content, name)
        encoded = base64.b64encode(content.read())
        result = self.imagekit.upload_file(
            file=encoded,
            file_name=name,
            options=options
        )
        return result.url

    def exists(self, name):
        return False

    def url(self, name):
        return name

    def delete(self, name):
        self.imagekit.delete_file(file_id=name)
