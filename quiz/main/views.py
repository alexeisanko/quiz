from django.views.generic.base import TemplateView

from quiz.main.models import Question


class IndexView(TemplateView):
    template_name = "pages/index.html"


class NewQuizView(TemplateView):
    template_name = "pages/new-quiz.html"


class BankQuestionView(TemplateView):
    template_name = "pages/bank-question.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["questions"] = Question.objects.all()
        context["themes"] = Question.objects.values_list(
            "qs_type",
            flat=True,
        ).distinct()
        return context


class NewsView(TemplateView):
    template_name = "pages/news.html"


class TeamsView(TemplateView):
    template_name = "pages/teams.html"


class ApplicationsView(TemplateView):
    template_name = "pages/applications.html"


class UsersView(TemplateView):
    template_name = "pages/users.html"
