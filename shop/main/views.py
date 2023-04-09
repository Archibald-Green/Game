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
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from main.models import CustomUser
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from random import randint


# Create your views here.
def index(request):
    print("gghgfhfghfghgfhgf")
    return render(request, 'main/index.html', context ={
        'books': models.Book.objects.all()
        
    }  )
    
def about(request):
    return render(request, 'main/about.html', context ={
         
    }  )
# def get_random_book():
#     pages_count = BookPage.objects.all().count()
#     rand_page_id = randint(2, pages_count)
    
#     get_current_page = BookPage.objects.filter(id=rand_page_id)
#     ...
#     data = []
    

class RegisterView (CreateView):
    form_class = forms.SignUpForm   
    template_name = 'main/register1.html'
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
    template_name = 'main/login1.html'
    
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

def password_reset_request(request):
    if request.method == 'POST':
        password_form = PasswordResetForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data['email']
            user_email = CustomUser.objects.filter(Q(email =data))
            if user_email.exists():
                for user in user_email:
                    subject = 'Сброс пароля'
                    email_template_name = 'main/password_message.txt'
                    parametrs = {
                        'email': user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'One_day',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http', 
                    }
                    email = render_to_string(email_template_name, parametrs)
                    try:
                        send_mail(subject, email, '', [user.email], fail_silently=False )
                    except: 
                        return HttpResponse('Invalid Header')
                    return redirect('password_reset_done')
    else:
        password_form = PasswordResetForm()
    context = {
        'password_form': password_form,
    }
    return render (request, 'main/password_reset.html', context)

def on_progress(view):
    def inner(request, book_id, **kwargs):
        try: 
            print ('zzzzzzzzzzzzzzzzzaaaaaaaaaaaaaaaa')
            progress = models.BoolProgress.objects.get(book=book_id, user=request.user)
            print ('sadasdasdasdasdasdasdasdasdasdasdasdas')
        except models.BoolProgress.DoesNotExist:
            return redirect(reverse('book', kwargs={'book_id': book_id}))
        return view (
            request = request, progress = progress, book_id = book_id, **kwargs 
            )
    return inner 

def book(request, book_id):
    b = get_object_or_404(models.Book, id=book_id)
    if not b.first_page:
        print ('_________________________-')
        return render(request, 'main/book.html', context ={'book': b,})
    try: 
        progress = models.BoolProgress.objects.get(book=b, user=request.user)
        print ('zccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
    except models.BoolProgress.DoesNotExist:
        progress = models.BoolProgress.start_reading(user = request.user, book = b )
        print ('aaaaaaaaaaaaaaaa')
    return redirect (reverse('page', kwargs={'book_id': b.id, 'page_id': progress.book_page.id,}))

@on_progress
def page(request, progress, book_id, page_id):
    
    page = get_object_or_404(models.BookPage, book__id = book_id, id = page_id,)
    progress.book_page = page
    progress.save()
    
    
    
    links = [(link, link.has_all_need(list(progress.items.all())))
             
             for link in page.pagelink_set.all()
             
             ]
    
    return render (request, 'main/page.html', context={
        'page': page,
        'progress': progress,
        'links': links,
        'page_items': page.items.exclude(id__in = progress.items.only('id')),
        
    })

@on_progress
def take (request,progress, book_id, page_id, item_id ):
   item = get_object_or_404(models.Item, id = item_id)
   progress.items.add(item)
   return redirect (reverse('page', kwargs={'book_id': book_id, 'page_id': page_id,}))

