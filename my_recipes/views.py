from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, TemplateView, DeleteView
from django.views.generic.edit import  CreateView, UpdateView, FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from .forms import RecipeForm
from .models import Recipe



# LoginView
class RecipeLoginView(LoginView):
    template_name = 'signin.html'
    form_class = AuthenticationForm
    #fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('recipe-list')


# Register view.
    
def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password = request.POST['password1'])
                user.save()
                login(request, user)    # Login function attach the user to the current session. 
                return redirect('recipe-list')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username aldeady exist.'
                })
                
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Password do not match.'
                })


# class SignUpView(CreateView):
#     template_name = 'signup.html'
#     def get(self, request):
#         return render(request, 'signup.html', { 'form': UserCreationForm() })

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('signin')

#         return render(request, 'signin.html',{ 'form': form })


    # model = User
    # form = UserRegisterForm
    # template_name = "signup.html"
    # form_class = UserCreationForm
    # fields = ['username', 'password']
    # redirect_authenticated_user = True # Redirect authenticated user.
    # success_message = "Your profile was created successfully"
    # success_url = reverse_lazy("signin")

    # def form_valid(self, form):
    #     user = form.save()
    #     if user is not None:
    #         login(self.request, user)
    #     return super(SignUpView, self).form_valid(form)

    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         return redirect('recipe-list')
    #     return super(SignUpView, self).get(*args, **kwargs)



# Home
class HomeTemplateView(TemplateView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'home.html'



#Lsit user recipes.
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipe-list.html'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['recipes'] = context['recipes'].filter(user=self.request.user)
        context['count'] = context['recipes'].filter(name=False).count()
        return context
    
    


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipe.html'



# Create recipe.
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipe-create.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipe-list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    
    success_url = reverse_lazy('recipe-list')
    

# UPDATE RECIPE.   
class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe-update.html'
    #fields = '__all__'
    success_url = reverse_lazy('recipe-list')



# DELETE RECIPE.
class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipe-delete.html'
    context_object_name = 'recipe'
    success_url = reverse_lazy('recipe-list')




# =================================================================
# FUNCTIONS BASED VIEWS.
# =================================================================

# def signup(request):

#     if request.method == 'GET':
#         return render(request, 'signup.html', {
#             'form': UserCreationForm
#         })
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(username=request.POST['username'],
#                 password = request.POST['password1'])
#                 user.save()
#                 login(request, user)    # Login function attach the user to the current session. 
#                 return redirect('recipe-list')
#             except IntegrityError:
#                 return render(request, 'signup.html', {
#                     'form': UserCreationForm,
#                     'error': 'Username aldeady exist.'
#                 })
                
#         return render(request, 'signup.html', {
#                     'form': UserCreationForm,
#                     'error': 'Password do not match.'
#                 })



# def signin(request):

#     if request.method == 'GET':
#         return render(request, 'signin.html', {
#             'form': AuthenticationForm
#         })
#     else:
#         user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
#         if user is None:
#             return render(request, 'signin.html', {
#                 'form': AuthenticationForm,
#                 'error': 'Username or Password is Incorrect.'
#         })
#         else:
#             login(request,  user)
#             return redirect('recipe-list')


# def signout(request):
#     logout(request)
#     return redirect('home')

            