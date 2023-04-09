# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from main.serializers import UserSerializer

import datetime
import json
from rest_framework import generics
from main.forms import SignUpForm
from main.models import *
from .serializers import *
from django.db.models import Q
from rest_framework.permissions import *
from .permissions import *
from django.http import HttpResponse

# @api_view(['GET'])
# def getData(request):
#     User = User.object.all()
#     serializer = UserSerializer(User, many=True)
#     return Response(serializer.data)


class RegistrationView (generics.CreateAPIView):
    model = CustomUser
    
    def post(self, request):
        form = SignUpForm()
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps(['Работает']))
        else: 
            response = []
            errors = form.errors 
            for field in errors: 
                error_msgs = errors[field]
                for error_msg in error_msgs:
                    response.append(error_msg)
            return HttpResponse(json.dumps(response))
        

# class indexView(generics.ListAPIView):
#     model = 
    
class BookView (generics.ListAPIView):
    serializer_class = BookSerializer
    model = Book 
    # permission_classes = (IsAuthenticated, )
    queryset = Book.objects.all() 
    
class BookView1 (generics.RetrieveAPIView):
    
    serializer_class = BookSerializer
    model = Book 
    # permission_classes = (IsAuthenticated, )
    queryset = Book.objects.all()
    
    
    
    
class BookPageView (generics.ListAPIView):
    
    serializer_class = BookPageSerializer
    model = BookPage 
    permission_classes = (IsAuthenticated, )
    queryset = BookPage.objects.all()
    
class BookPageView (generics.RetrieveAPIView):
    
    serializer_class = BookPageSerializer
    model = BookPage 
    permission_classes = (IsAuthenticated, )
    queryset = BookPage.objects.all()
    
    
    
    
class ItemView (generics.ListAPIView):
    
    serializer_class = ItemSerializer
    model = Item
    permission_classes = (IsAuthenticated, )
    queryset = Item.objects.all()

class ItemView (generics.RetrieveAPIView):
    
    serializer_class = ItemSerializer
    model = Item
    permission_classes = (IsAuthenticated, )
    queryset = Item.objects.all()
    
    
    
    
class PageLinkView (generics.ListAPIView):
    
    serializer_class = PageLinkSerializer
    model = PageLink
    permission_classes = (IsAuthenticated, )
    queryset = PageLink.objects.all()

class PageLinkView (generics.RetrieveAPIView):
    
    serializer_class = PageLinkSerializer
    model = PageLink
    permission_classes = (IsAuthenticated, )
    queryset = PageLink.objects.all()
    
    
    
    
class BoolProgressView (generics.ListAPIView):
    
    serializer_class = BoolProgressSerializer
    model = BoolProgress
    permission_classes = (IsAuthenticated, )
    queryset = BoolProgress.objects.all()

class BoolProgressView (generics.RetrieveAPIView):
    
    serializer_class = BoolProgressSerializer
    model = BoolProgress
    permission_classes = (IsAuthenticated, )
    queryset = BoolProgress.objects.all()

        
        

