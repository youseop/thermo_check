from django.contrib import admin
from .models import Thermal
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin


class ThermalAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


admin.site.register(Thermal, ThermalAdmin)

