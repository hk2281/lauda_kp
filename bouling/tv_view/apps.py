from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TvViewConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tv_view"
    verbose_name = _('таблицы боулинг клуба')
