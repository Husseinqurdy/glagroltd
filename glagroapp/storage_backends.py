import os
from django.core.files.storage import Storage
from supabase import create_client

class SupabaseStorage(Storage):
    def __init__(self, option=None):
        self.url = os.environ.get("SUPABASE_URL")
        self.key = os.environ.get("SUPABASE_KEY")
        self.client = create_client(self.url, self.key)
        self.bucket = os.environ.get("SUPABASE_BUCKET", "media")

    def _save(self, name, content):
        # Soma data ya file
        data = content.read()
        # Upload file kwa Supabase
        self.client.storage.from_(self.bucket).upload(name, data)
        return name

    def url(self, name):
        # Rudisha public URL
        return f"{self.url}/storage/v1/object/public/{self.bucket}/{name}"
