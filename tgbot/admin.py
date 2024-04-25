from django.contrib import admin
from. models import User_tg,DocumentType,DocumentTypeField,UserDocumentFill
# Register your models here.
admin.site.register(User_tg)
admin.site.register(DocumentType)
admin.site.register(DocumentTypeField)
admin.site.register(UserDocumentFill)