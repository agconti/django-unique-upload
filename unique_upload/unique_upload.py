import uuid
import os

def unique_upload(instance, filename):
    ext = filename.split('.').pop()
    filename = "{}.{}".format(uuid.uuid4(), ext)
    return os.path.join('uploads/logos', filename)
