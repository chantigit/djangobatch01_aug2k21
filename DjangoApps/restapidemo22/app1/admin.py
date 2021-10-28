from django.contrib import admin
from .models import Bucketlist
# Register your models here.

@admin.register(Bucketlist)
class BucketAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'date_created', 'date_modified']