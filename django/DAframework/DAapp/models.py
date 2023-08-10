from django.db import models

class Document(models.Model):
    txt_file = models.FileField(upload_to='documents/')
    db_file = models.FileField(upload_to='documents/')
