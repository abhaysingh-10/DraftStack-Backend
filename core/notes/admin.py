from django.contrib import admin
from .models import Notes,SubTask


@admin.register(Notes)

class NotesAdmin(admin.ModelAdmin):
    list_display = ["title","created_at"]
    
    
@admin.register(SubTask)

class SubTaskAdmin(admin.ModelAdmin):
    list_display =['title','completed']
    
