from django.urls import path

from sweets_wiki.views import SampleView

urlpatterns = [
    path("sample", SampleView.as_view()),
]
