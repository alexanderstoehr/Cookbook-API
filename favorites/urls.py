from django.urls import path

from favorites.views import LikeRecipeView, LikeCookbookView

urlpatterns = [
    path("cookbook/<int:pk>/", LikeCookbookView.as_view()),
    path("recipe/<int:pk>/", LikeRecipeView.as_view()),
]