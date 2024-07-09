from django.urls import path

from cookbooks.views import ListCreateCookbookView, RetrieveUpdateDeleteCookbookView, ListMyOwnCookbooksView

urlpatterns = [
    path("", ListCreateCookbookView.as_view()),
    path("<int:pk>/", RetrieveUpdateDeleteCookbookView.as_view()),
    path("me/", ListMyOwnCookbooksView.as_view()),

]