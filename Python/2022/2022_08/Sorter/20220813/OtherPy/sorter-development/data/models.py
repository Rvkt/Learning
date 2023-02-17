from django.db import models


class File(models.Model):
    filename = models.TextField()
    filepath_hash = models.TextField()
    last_modified = models.DateTimeField()
    added_at = models.DateTimeField()


class Path(models.Model):
    filename = models.ForeignKey(File, related_name='filename_path')
    source = models.TextField()
    destination = models.TextField()
    accepted = models.BooleanField(default=True)
    added_at = models.DateTimeField()
