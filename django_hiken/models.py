from django.db import models
from django.template import Template, Context

# Create your models here.
class TemplateHTML(models.Model):
    name = models.CharField(max_length=150)
    template = models.TextField(help_text="Put the placeholder around double curly bracket in template as template_tags.")
    placeholder = models.JSONField(default=dict, null=True, blank=True)

   
    def generate(self, content:dict[str, str]=None):
        context = Context({})

        if self.placeholder and content:
            context = Context(content)
        
        elif self.placeholder is None and content:
            context = Context(content)

        elif self.placeholder and content is None:
            context = Context(self.placeholder)

        template = Template(self.template)
        return template.render(context)



