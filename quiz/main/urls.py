from django.urls import path

from .views import (
    IndexView,
    NewQuizView,
    BankQuestionView,
    NewsView,
    TeamsView,
    ApplicationsView,
    UsersView,
)

app_name = "main"
urlpatterns = [
    path("", view=IndexView.as_view(), name="index"),
    path("new-quiz/", view=NewQuizView.as_view(), name="new-quiz"),
    path("bank-question/", view=BankQuestionView.as_view(), name="bank-question"),
    path("news/", view=NewsView.as_view(), name="news"),
    path("teams/", view=TeamsView.as_view(), name="teams"),
    path("applications/", view=ApplicationsView.as_view(), name="applications"),
    path("users/", view=UsersView.as_view(), name="users"),
]
