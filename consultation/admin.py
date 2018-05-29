from django.contrib import admin
from .models import Consultation
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class ConsultationAdmin(SummernoteModelAdmin):
    list_display = ('owner','motif','created_at',)
    prepopulated_fields = {'slug': ('motif',)}
    list_filter = ('owner','motif','created_at')
    search_fields = ('owner', 'motif')
admin.site.register(Consultation, ConsultationAdmin)
