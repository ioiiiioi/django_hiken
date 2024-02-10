from django.contrib import admin
from .models import TemplateHTML
from django.utils.html import format_html
from django.http.response import HttpResponse
from django.urls import reverse, path
# Register your models here.

@admin.register(TemplateHTML)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'view_template']

    def get_urls(self):
        urls = super(TemplateAdmin, self).get_urls()
        urls += [path('views/<str:pk>', self.open_template, name='applabel_modelname_open-template'),]
        return urls

    def view_template(self, obj):
        return format_html(
                '<a href="{}">View Template</a>', reverse('admin:applabel_modelname_open-template', args=[obj.id]))
    
    view_template.short_description = "View template"

    def open_template(self, request, pk):
        content = self.get_object(request, pk).generate()
        response = HttpResponse(content)
        return response