from django.contrib import admin
from .models import Thermal, User
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin


class ThermalAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


admin.site.register(Thermal, ThermalAdmin)

admin.site.register(User)

