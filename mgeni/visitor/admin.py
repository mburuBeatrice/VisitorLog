from django.contrib import admin
from .models import Visitor,County
# Register your models here.
# class VisitorModelAdmin(admin.ModelAdmin):
#     list_display = ["name", "arrival","departure"]
#     list_display_links = ["arrival"]
#     list_editable = ["name"]
#     list_filter = ["arrival","departure"]
#     search_fields = ["name"]
#     class Meta:
#         model = Visitor
admin.site.register(Visitor)
admin.site.register(County)