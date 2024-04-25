from django.db import models

class User_tg(models.Model):
    name = models.CharField(max_length=100)
    token = models.CharField(max_length=100)

class DocumentType(models.Model):
    name = models.CharField(max_length=100)
    fields_count = models.IntegerField()
    file = models.FileField(upload_to='documents/')

class DocumentTypeField(models.Model):
    document_type = models.ForeignKey(DocumentType,on_delete=models.CASCADE)
    field_name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=100)
    number = models.IntegerField()

class UserDocumentFill(models.Model):
    user = models.ForeignKey(User_tg, on_delete=models.CASCADE)
    document_type = models.ForeignKey(DocumentType,on_delete = models.CASCADE)
    filled_file= models.FileField(upload_to='user_documents/')