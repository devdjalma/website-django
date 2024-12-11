from django.shortcuts import render
from django.http import HttpRequest
from django.views import View
from faker import Faker
from formulario.models import UserData

fake = Faker("pt_BR")

# Create your views here.


def home(request: HttpRequest):
    return render(request, "home.html")


class RegistradosView(View):

    template_name: str = "registrados.html"

    def get(self, request: HttpRequest):

        usuarios = UserData.objects.all()

        registrados = {"registrados": usuarios}

        return render(
            request=request,
            template_name=self.template_name,
            context=registrados,
        )


if __name__ == "__main__":
    print("imported!")
