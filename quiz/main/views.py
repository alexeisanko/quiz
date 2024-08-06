from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "pages/index.html"


class NewQuizView(TemplateView):
    template_name = "pages/new-quiz.html"


class BankQuestionView(TemplateView):
    template_name = "pages/bank-question.html"


class NewsView(TemplateView):
    template_name = "pages/news.html"


class TeamsView(TemplateView):
    template_name = "pages/teams.html"


class ApplicationsView(TemplateView):
    template_name = "pages/applications.html"


class UsersView(TemplateView):
    template_name = "pages/users.html"
