from django.contrib import admin
from .models import *

# Register your models here.

class RoomsInline(admin.StackedInline):
    model = Room
        
class RoomAdmin(admin.ModelAdmin):
    inlines = [
        RoomsInline,
    ]
    
    
class ItemsInline(admin.TabularInline):
    model = Items
        
class ItemsAdmin(admin.ModelAdmin):
    inlines = [
        ItemsInline,
    ]

admin.site.register(Areas, RoomAdmin)
admin.site.register(Category, ItemsAdmin)
admin.site.register(User)