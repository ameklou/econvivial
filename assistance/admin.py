from django.contrib import admin
from .models import Assistance
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class AssistanceAdmin(SummernoteModelAdmin):
    list_display = ('owner','service','created_at',)
    prepopulated_fields = {'slug': ('service',)}
    list_filter = ('owner','service','created_at')
    search_fields = ('owner', 'service')
admin.site.register(Assistance, AssistanceAdmin)
