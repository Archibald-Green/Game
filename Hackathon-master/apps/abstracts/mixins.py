from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.template import (
    loader,
    Template,
)
from django.forms.models import ModelFormMetaclass


class HttpResponseMixin:
    """Mixin from http handlers."""

    content_type = 'text/html'

    def get_http_response(
        self,
        request: WSGIRequest,
        template_name: str,
        context: dict = {}
    ) -> HttpResponse:
        
        template: Template =\
            loader.get_template(
                template_name
            )

        return HttpResponse(
            template.render(
                context=context,
                request=request
            ),
            content_type=self.content_type
        )

    def get_http_response_and_check_form(
        self,
        request,
        form: ModelFormMetaclass
    ) -> HttpResponse:
        form = self.form(request.POST)
        if not form.is_valid():
            return HttpResponse('not ok')
        form.save()
        return HttpResponse('ok')