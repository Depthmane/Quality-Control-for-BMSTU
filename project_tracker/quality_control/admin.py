from django.contrib import admin
from .models import FeatureRequest, BugReport


# класс администратора для BugReport
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'task')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('name', 'description')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'


# класс администратора для FeatureRequest

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'task', 'project',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
