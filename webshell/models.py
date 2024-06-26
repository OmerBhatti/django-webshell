from django.db import models
try:
    from django.utils.translation import gettext_lazy as _
except ImportError:
    from django.utils.translation import ugettext_lazy as _


class Script(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    source = models.TextField(_('Source'))

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Script')
        verbose_name_plural = _('Scripts')
