# Python
from typing import Any

# Django
from django.shortcuts import render
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import (
    HttpRequest,
    HttpResponse,
    QueryDict,
)
from django.views.generic import (
    View,
    ListView,
)
from django.core.files.uploadedfile import InMemoryUploadedFile

# Local
from .models import (
    UserCall,
)
from abstracts.mixins import HttpResponseMixin
# from .forms import (
#     UserCallForm,
# )


class MainView(HttpResponseMixin, View):
    """Main view."""

    def get(self, request: HttpRequest, *args, **kwargs):

        return self.get_http_response(
            request=request,
            template_name='home_page.html',
            context={
                'ctx_user': request.user
            }
        )
    

# class UserCallView(HttpResponseMixin, View):
#     """View for UserCall."""

#     form = UserCallForm

#     def get(self, request: HttpRequest, *args: tuple, **kwargs: dict):
#         return self.get_http_response(
#             request=request,
#             template_name='.html',
#             context={
#                 'ctx_form' : self.form()
#             }
#         )

#     def post(
#         self, 
#         request: HttpRequest,
#         *args: tuple, 
#         **kwargs: dict
#     ) -> HttpResponse:
#         form = self.form(request.POST or None)
#         if not form.is_valid():
#             return HttpResponse('')
#         print(form.cleaned_data)
#         form.save()
#         return HttpResponse('OK')