from django.urls import path

from cookbooks.views import ListMyOwnCookbooksView
from recipes.views import ListCreateRecipesView, RetrieveUpdateDeleteRecipeView

# from recipes.views import RecipeView, RecipesView
#
urlpatterns = [
    path("", ListCreateRecipesView.as_view()),
    path("<int:pk>/", RetrieveUpdateDeleteRecipeView.as_view()),
]

#     path("<int:id>/", RecipeView.as_view())
# ]