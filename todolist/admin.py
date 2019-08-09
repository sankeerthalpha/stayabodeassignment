from django.contrib import admin
from .models import List, Item, Deleted
from django.http import HttpResponse
import csv

# Register your models here.

class ListAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]
    list_display = ("id", "title")

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_date", "completed")

class DeletedAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

admin.site.register(List, ListAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Deleted, DeletedAdmin)
