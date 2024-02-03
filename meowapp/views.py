from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("meowapp/index.html")
    context = {
        "text": "testing testing 123",
    }
    return HttpResponse(template.render(context, request))
