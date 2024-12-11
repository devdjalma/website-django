from datetime import datetime
from formulario.models import UserData, UserCategory
from faker import Faker
from unidecode import unidecode
import re
import random
from formulario.constantes import GRAUS_ENSINO, USER_CATEGORIES

# Criar uma instância do Faker
fake = Faker(locale="pt_BR")  # Gera dados no formato brasileiro


class PopulateDataBase:

    def populate(self):
        self.populate_categories()
        self.populate_users()

    @staticmethod
    def create_email(name: str) -> str:
        """Formata o nome para ASCII sem caracteres especiais ou espacos."""
        name_ascii = unidecode(name)
        clear_name = re.sub(rf"[^a-zA-Z\s]", "", name_ascii)
        email_name = "".join(clear_name.lower().split(" "))
        return f"{email_name}@gmail.com"

    def populate_categories(self):
        for categoria in USER_CATEGORIES:
            UserCategory.objects.get_or_create(user_data_category=categoria)
        # Buscar todas as categorias disponíveis
        self.categorias_instancias = list(UserCategory.objects.all())

    def populate_users(self):
        for _ in range(1):

            fake_name = fake.name()
            fake_email = self.create_email(fake_name)

            UserData.objects.create(
                nome=fake_name,
                email=fake_email,
                numero=fake.phone_number(),
                idade=random.randint(18, 50),
                mensagem=fake.sentence(nb_words=10),  # Mensagem com 10 palavras
                grau_ensino=random.choice(GRAUS_ENSINO),
                user_category_id=random.choice(self.categorias_instancias),
                data_registro=datetime.now(),
            )


def main(*args, **kwargs) -> None:
    PopulateDataBase().populate()
    # from formulario.models import UserData
    # python manage.py makemigrations
    # python manage.py migrate
    # python manage.py showmigrations
    # python manage.py migrate formulario 0001 --plan # mostrar reversão
    # python manage.py sqlmigrate formulario 0001
    # UserData.objects.get(id=<numero>)
    # UserData.objects.filter(idade=21)
    # UserData.objects.filter(nome="Pedro") & UserData.objects.filter(idade=22)



if __name__ == "__main__":
    main()
    # Fim do Código
    