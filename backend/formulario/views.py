from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from formulario.forms import UserDataFrom
from formulario.models import UserCategory, UserData
from django.views import View
from rich.console import Console

console = Console()


class UserFormView(View):

    template_name = "formulario.html"

    def get(self, request: HttpRequest):
        form = UserDataFrom()
        return render(
            request=request,
            template_name=self.template_name,
            context={"form": form},
        )

    def post(self, request: HttpRequest):

        form = UserDataFrom(request.POST)

        if form.is_valid():

            attrs = [
                "user_category_id",
                "nome",
                "email",
                "numero",
                "idade",
                "grau_ensino",
                "mensagem",
            ]
            lista_attrs = [str(form.cleaned_data.get(attr, "Error")) for attr in attrs]
            console.print(f"{lista_attrs=} {type(lista_attrs)=}", style="yellow bold")

            _string = "<br>".join(lista_attrs)
            string = f"""{_string}"""
            # Sempre tem que ser a instancia da parada filtrada
            # e não uma string se não sempre vai dar BO

            already_on_db = UserData.objects.filter(
                email=form.cleaned_data["email"]
            ).first()

            console.print(f"{already_on_db = }", style="blue bold")

            user_category_id = UserCategory.objects.filter(
                user_data_category=form.cleaned_data["user_category_id"]
            ).first()

            if not already_on_db:

                console.print("Criando usuario", style="green bold")

                UserData.objects.create(
                    nome=form.cleaned_data["nome"],
                    email=form.cleaned_data["email"],
                    numero=form.cleaned_data["numero"],
                    idade=form.cleaned_data["idade"],
                    grau_ensino=form.cleaned_data["grau_ensino"],
                    mensagem=form.cleaned_data["mensagem"],
                    user_category_id=user_category_id,
                )
                console.print("Usuario criado com sucesso!", style="green bold")

                # Retornando as informações do Novo User
                user_banco = UserData.objects.filter(
                    email=form.cleaned_data["email"]
                ).first()

                if user_banco:
                    context = {
                        "user_category_id": str(user_banco.user_category_id),
                        "nome": user_banco.nome,
                        "email": user_banco.email,
                        "numero": user_banco.numero,
                        "idade": str(user_banco.idade),
                        "grau_ensino": user_banco.grau_ensino,
                        "mensagem": user_banco.mensagem,
                        "data_registro": user_banco.data_registro.strftime(" %x %X"),
                    }

                console.print(f"{context = }", style="magenta bold")
                return render(
                    request=request, template_name="sucesso.html", context=context
                )

            else:
                context = {
                    "user_category_id": str(already_on_db.user_category_id),
                    "nome": already_on_db.nome,
                    "email": already_on_db.email,
                    "numero": already_on_db.numero,
                    "idade": str(already_on_db.idade),
                    "grau_ensino": already_on_db.grau_ensino,
                    "mensagem": already_on_db.mensagem,
                    "data_registro": already_on_db.data_registro.strftime(" %x %X"),
                }
                console.print(
                    "Usuario ja presente no Banco de Dados.", style="yellow bold"
                )
                return render(
                    request=request, template_name="japresente.html", context=context
                )

        # Se inválido, renderizar novamente com erros
        return HttpResponse("<h1>Falha!</h1>")
