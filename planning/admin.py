from django.contrib import admin
from .models import Planning
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PlanAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    list_filter = ('title', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Planning, PlanAdmin)
