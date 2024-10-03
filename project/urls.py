from django.urls import path

from .views import ProjectTypeView, ClientView, MessageView,ProjectView, TaskView

urlpatterns = [
    path('project-type/', ProjectTypeView.as_view()),
    path('client/', ClientView.as_view()),
    path('project/', ProjectView.as_view()),
    path('task/', TaskView.as_view()),
    path('message/', MessageView.as_view()),
]