from django.contrib import admin
from .models import*

# Register your models here.
@admin.register(Todo)
class Todolist(admin.ModelAdmin):
    list_display=['tittle','description','date','completed','created_at','updated_at']
    search_fields=['tittle','date']
    list_filter=['tittle']
    ordering=['-created_at']