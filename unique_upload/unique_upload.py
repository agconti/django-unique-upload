import uuid
import os

def unique_upload(instance, filename):
    ext = filename.split('.').pop()
    return "{}.{}".format(uuid.uuid4(), ext)
