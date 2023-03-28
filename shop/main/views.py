from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from . import models, forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from main import serializers, models
from main.models import Book
from django.urls import reverse, reverse_lazy
from .models import BookPage
from django.views.generic import View
from django.views.generic.edit import CreateView


from random import randint


# Create your views here.
def index(request):
    print("gghgfhfghfghgfhgf")
    return render(request, 'main/index.html', context ={
        'books': models.Book.objects.all()
        
    }  )
    
def book(request, book_id):
    b = get_object_or_404(models.Book, id=book_id)
    
    if not b.first_page:
        print ('_________________________-')
        return render(request, 'main/book.html', context ={
        'book': b,
        })
    try: 
        print ('zzzzzzzzzzzzzzzzzaaaaaaaaaaaaaaaa')
        progress = models.BoolProgress.objects.get(book = b, user = request.user.id)
    except models.BoolProgress.DoesNotExist:
        print ('aaaaaaaaaaaaaaaa')
        progress = models.BoolProgress.start_reading(user = request.user.id, book = b )
    return redirect (reverse('page', kwargs={'book_id': b.id, 'page_id': progress.book_page.id}))


def page(request,book_id, page_id):
    query = models.BoolProgress.objects.filter(book = book_id, user = request.user.id, book_page = page_id)
    if not query:
        print (request.user.id)
        print ('aaaaaaaaaaaaaaaaffffffff')
        return redirect (reverse('book', kwargs={'book_id': book_id}))
    
    return render(request, 'main/page.html', context ={
        'page': get_object_or_404(models.BookPage, book__id=book_id, id=page_id,
        ),
    }  )

# def get_random_book():
#     pages_count = BookPage.objects.all().count()
#     rand_page_id = randint(2, pages_count)
    
#     get_current_page = BookPage.objects.filter(id=rand_page_id)
#     ...
#     data = []
    

# def login(request):
#     form = forms.UserLoginForm()
#     if request.method == "POST":
#         print("EMAIL: ", request.POST.get("email"))
#         print("PASSWORD: ", request.POST.get("password"))
        
#         form = forms.UserLoginForm(request.POST)
        
#         if form.is_valid():
#             user = models.User.objects.filter(email=request.POST.get("email"), password=request.POST.get("password")).exists()
#             if user == True:
#                 return redirect('/index')
#             else:
#                 form.add_error('email', 'Неправильный логин или пароль')
                
#                 for error in form.errors:
#                     print(dir(error))

#         return render(request, "main/log.html", context={'form': form})

#     return render(request, 'main/log.html', context={'form': form})



# def register(request):
    
#     if request.method == "POST":
        
#         login = request.POST.get("login")
        
#         password = request.POST.get("password")
        
#         email = request.POST.get("email")
        
        
#         user = models.User(
#             login = login,
#             password = password,
#             email = email,
#         )
        
#         form = forms.UserRegisterForm (request.POST)
        
#         if form.is_valid(): 
#             user.save()
#             user = authenticate(request.POST)
#             messages.success(request, f'Создан аккаунт {email}!')
#             return redirect('/login')
        
#         return HttpResponse("Invalid data") 
#     return render(request, 'main/register.html')

class RegisterView (CreateView):
    form_class = forms.SignUpForm   
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')
    success_message = "Your profile was created successfully"
    
    def form_valid(self, form):
        return super(RegisterView, self).form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['sname'] = 'asdasdasdasd'
        return context
    
def check_admin(user):
    is_saler = False
    print("FFFFFFFFFFFF", user.is_saler())
    if user.is_saler().name == 'Модератор':
        is_saler = True
    
    return is_saler


class UserListView (generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]
    
    
class CustomLoginView(LoginView):
    form_class = forms.CustomLoginForm   
    template_name = 'main/login.html'
    
    def get_success_url(self):
        return reverse_lazy('index')
    
    def form_valid(self, form):
        print ('aaaaaaaaaaaaaaaaa')
        return super().form_valid(form)
    
    
class AddPageView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        form = forms.BookPageForm
        return render(
            request=request,
            template_name='main/page_add.html',
            context={
                'form' : form
            }
        )
        
    
    def post(self, request, *args ,   **kwargs):
         print(request.POST)
         if request.method == 'POST':
            form = forms.BookPageForm (request.POST)
            print ('ffffffffff', request.POST)
            
            if form.is_valid():
                    print("8888888888888888888888888888888888888888888888888")
                    order = form.save(commit=False)
                    order.save()
                    return redirect('index')
            
                        
            
            return render(request, 'main/page_add.html', context ={'form': form})
        
        
def logout_user(request):
    logout(request)
    messages.success(request, ('Вы вышли'))
    return redirect ('login')


def profile(request):
	return render(request, 'main/index.html')