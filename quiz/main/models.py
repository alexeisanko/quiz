from django.db import models
from django.utils.translation import gettext_lazy as _


class QuizList(models.Model):
    name = models.CharField(_("Name quiz"), max_length=255, null=False)
    theme = models.CharField(_("Theme quiz"), max_length=255, null=False)
    description = models.TextField(_("Description quiz"))
    img = models.ImageField(
        _("ScreenSaver"),
        upload_to=None,
        height_field=None,
        width_field=None,
        max_length=None,
    )
    status = models.BooleanField(_("Status quiz"), default=False, null=False)
    start_time = models.DateTimeField(_("Start time"))
    end_time = models.DateTimeField(_("End time"))
    creation_time = models.DateTimeField(_("Creation time"), auto_now_add=True)
    available_cert = models.BooleanField(_("Available certificate"), default=False)

    def __str__(self):
        return f"{self.name} ({self.theme})"


class Team(models.Model):
    quiz_id = models.ForeignKey(QuizList, on_delete=models.PROTECT)
    name = models.CharField(_("Name team"), max_length=255, null=False)
    color = models.CharField(_("Color team"), max_length=255, null=False)
    team_key = models.CharField(_("Team key"), max_length=255, null=False)
    active = models.BooleanField(_("Active team"), default=True, null=False)

    def __str__(self) -> str:
        return f"{self.name} ({self.color})"


class QuizArchive(models.Model):
    quiz_id = models.ForeignKey(QuizList, on_delete=models.PROTECT)
    team_id = models.ForeignKey(Team, on_delete=models.PROTECT)
    result = models.IntegerField(_("Result quiz"), null=True)

    def __str__(self):
        return f"{self.quiz_id.name} ({self.team_id.name})"


class Question(models.Model):
    quiz_id = models.ForeignKey(QuizList, on_delete=models.CASCADE)
    question = models.TextField(_("Question"), null=False)
    answer = models.TextField(_("Answer"), null=False)
    media_type = models.CharField(_("Media type"), max_length=255)
    media_name = models.CharField(_("Media name"), max_length=255)
    qs_type = models.CharField(_("Question type"), max_length=255)

    def __str__(self):
        return f"{self.id}"


class TeamAnswer(models.Model):
    quiz_id = models.ForeignKey(QuizList, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(_("Answer"), null=False)
    correct = models.BooleanField(_("Correct answer"), default=False, null=False)
    time_given = models.DateTimeField(_("Time given"), auto_now_add=True)

    def __str__(self):
        return f"{self.id}"


class TeamChat(models.Model):
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    message = models.TextField(_("Message"), null=False)
    time_given = models.DateTimeField(_("Time given"), auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.id}"
