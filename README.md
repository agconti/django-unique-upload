# django-unique-upload
[![Build Status](https://travis-ci.org/agconti/django-unique-upload.svg?branch=master)](https://travis-ci.org/agconti/django-unique-upload)

A django utility that creates unique file names for uploaded files via uuids.

## Why
This eliminates the need to check if the a file already exists with the same name. Checking incurs overhead. Removing the need to check boosts performance. Popular pacakges like django storages don't check if a file already exists with the same name by default. They instead overwrite the file. Using unique file names ensures that no file is over written.

## Install
```bash
pip install django-unique-upload
```

## Usage
Simply use the `unique_upload` function as value for a model's `FileField` or `ImageField` `upload_to` argument:
```python
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from unique_upload import unique_upload


@python_2_unicode_compatible
class MyModel(modles.Model):
    image = models.ImageField(upload_to=unique_upload)
    file = models.FileField(upload_to=unique_upload)
```
Now if we give save `MyModel` with two new files,  `cool-image.jpg` and `really-important.pdf`, Django will save the files to S3 with the values: `3fce8b21-5b0d-4f27-9d99-2bb202f211c7.jpg` and `50a44439-843e-4049-949d-b54cfcddff19.pdf`.

## Tests
Run the devepment tests with:
```bash
python -m unittest discover test
```
