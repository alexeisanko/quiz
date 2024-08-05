import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "quiz.main"
    verbose_name = _("Main")

    def ready(self):
        with contextlib.suppress(ImportError):
            import quiz.main.signals  # noqa: F401
