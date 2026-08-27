from django.urls import path
from . import views

app_name = "dojo"

urlpatterns = [
    path("", views.index, name="index"),
    path("hiragana/", views.hiragana, name="hiragana"),
    path("katakana/", views.katakana, name="katakana"),
    path("vocabulary/", views.vocabulary, name="vocabulary"),
    path("quiz/", views.quiz, name="quiz"),
    path("quiz/answer/", views.quiz_answer, name="quiz_answer"),
    path("quiz/reset/", views.quiz_reset, name="quiz_reset"),
]

