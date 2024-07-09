from django.urls import path

from cookbooks.views import ListCreateCookbookView, RetrieveUpdateDeleteCookbookView
from ingredients.views import ListCreateIngredientsView, RetrieveUpdateDeleteIngredientView

urlpatterns = [
    path("", ListCreateIngredientsView.as_view()),
    path("<int:pk>/", RetrieveUpdateDeleteIngredientView.as_view()),
]
