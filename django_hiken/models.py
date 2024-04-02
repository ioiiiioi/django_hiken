from django.db import models
from django.template import Template, Context
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.exceptions import ValidationError


# Create your models here.
class TemplateHTML(models.Model):
    name = models.CharField(max_length=150)
    subject = models.CharField(max_length=150, null=True, blank=True)
    template = models.TextField(
        help_text="Put the placeholder around double curly bracket in template as template_tags."
    )
    placeholder = models.JSONField(default=dict, null=True, blank=True)

    def generate(self, content: dict[str, str] = None):
        context = Context({})

        if self.placeholder and content:
            context = Context(content)

        elif self.placeholder is None and content:
            context = Context(content)

        elif self.placeholder and content is None:
            context = Context(self.placeholder)

        template = Template(self.template)
        return template.render(context)

    def send_mail(self, content: dict[str, str]):
        message = self.generate(content)
        if not hasattr(settings, "EMAIL_SENDER"):
            raise ValidationError("Missing EMAIL_SENDER setting.")
        email = EmailMultiAlternatives(
            self.subject, message, to=[email], from_email=settings.EMAIL_SENDER
        )
        email.content_subtype = "html"
        email.send(fail_silently=False)
        return email

    class Meta:
        verbose_name_plural = "HTML Templates"
