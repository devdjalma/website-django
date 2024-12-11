import random
from django import forms
from formulario.constantes import GRAUS_ENSINO, USER_CATEGORIES
from faker import Faker
from formulario.populate_userdata import PopulateDataBase

fake = Faker(locale="pt_BR")


GRAUS_ENSINO_T = tuple(zip(GRAUS_ENSINO, GRAUS_ENSINO))
USER_CATEGORIES_T = tuple(zip(USER_CATEGORIES, USER_CATEGORIES))


def initial_data(opt: str):
    name = fake.name()
    email = PopulateDataBase.create_email(name)

    data = {
        "nome": name,
        "email": email,
        "numero": fake.phone_number(),
        "idade": random.randint(18, 61),
    }
    return data.get(opt)


class UserDataFrom(forms.Form):

    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    numero = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "input-mask", "placeholder": "+55 (XX) XXXX-XXXX"}
        ),
    )
    idade = forms.IntegerField(required=False)
    grau_ensino = forms.ChoiceField(choices=GRAUS_ENSINO_T)
    mensagem = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}), required=False)
    user_category_id = forms.ChoiceField(choices=USER_CATEGORIES_T, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        name = fake.name()
        email = PopulateDataBase.create_email(name)

        self.fields["nome"].initial = name
        self.fields["email"].initial = email
        self.fields["numero"].initial = fake.phone_number()
        self.fields["idade"].initial = random.randint(18, 61)
        self.fields["mensagem"].initial = fake.paragraph(nb_sentences=5)
