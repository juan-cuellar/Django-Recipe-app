from django.urls import path
from my_recipes import views

from .views import HomeTemplateView, RecipeListView, RecipeCreateView, RecipeDetailView, signup, RecipeLoginView, RecipeDeleteView, RecipeUpdateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('recipe-list/', RecipeListView.as_view(), name='recipe-list'),
    path('recipe-create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe'),
    path('recipe-update/<int:pk>/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe-delete/<int:pk>/', RecipeDeleteView.as_view(), name='recipe-delete'),

    path('signup/', views.signup, name='signup'),
    path('signin/', RecipeLoginView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(next_page='signin'), name='logout'),



]