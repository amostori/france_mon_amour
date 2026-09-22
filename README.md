1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install django`
4. `django-admin startproject config .`
5. `django-admin startapp website`
6. `python manage.py migrate`
7. settings.py: nazwa aplikacji do INSTALLED_APPS
8. config/urls.py: `path('', include('website.urls')),`
9. website/urls.py:

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```
10. website/views.py: def home()
11. Dwa foldery templates
12. settings.py: TEMPLATES:
    `'DIRS': [BASE_DIR / 'templates'],`
13. Folder static i settings.py:
    `STATICFILES_DIRS = [BASE_DIR / 'static']`

Modele do bazy danych
1. W pliku models.py stwórz klasę z polami modelu.
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. W pliku admin.py zarejestruj model.
5. `python manage.py createsuperuser`

Wyświetlenie danych z bazy
1. W pliku views.py pobierz dane `models.TaskList.objects.all()`, 
a w pliku .html użyj pętli 'for' i tabeli z Bootstrapa by wyświetlić dane.


1. Stwórz katalog, a w nim uruchom środowisko wirtualne Pythona:
`python3 -m venv venv`
2. Aktywacja środowiska wirtualnego:
`source venv/bin/activate` 
3. Instalacja django:
`pip install django`
4. Stwórz projekt Django:
`django-admin startproject nazwa_projektu .`
5. Stwórz aplikację:
`django-admin startapp nazwa_aplikacji`
6. `python manage.py migrate`
7. Uruchomienie serwera by podejrzeć stronę:
`python manage.py runserver`
8. W settings.py dodaj `<nazwa_aplikacji>.apps.<Nazwa_aplikacji>Config` do sekcji INSTALLED_APPS.
9. Do pliku projekt/urls.py dodaj path dla pliku aplikacja/urls.py, który utworzysz w katalogu aplikacji.
10. Napisz klasę reprezentującą widok strony w pliku aplikacja/views.py.
11. Do katalogu z projektem dodaj katalog 'templates' z bazą dla stron html. Drugi katalog 'templates' dodaj do katalogu z aplikacją, a w nim będziesz dodawał szablony szczegółowe (np. home.html).
12. W settings.py, w 'TEMPLATES' dodaj informację o lokalizacji katalogu templates:
`'DIRS': [(os.path.join(BASE_DIR, 'templates')),],` (zaimportuj os).
13. Pliki statyczne: w głównym katalogu projektu stwórz folder 'static', a w settings.py dodaj formułę:
`STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]`
14. W plikach html używających statycznych elementów należy dodać:
`{% load static %}`, następnie, jako src adres pliku, np:
`src="{% static 'images/1.jpg' %}"`

Tworzenie superusera:
1. `python manage.py createsuperuser` (admin, admin)

Modele do bazy danych
1. W pliku models.py stwórz klasę z polami modelu.
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. W pliku admin.py zarejestruj model.

Wyświetlenie danych z bazy
1. W pliku views.py pobierz dane `models.TaskList.objects.all()`, 
a w pliku .html użyj pętli 'for' i tabeli z Bootstrapa by wyświetlić dane.

Dodawanie danych do bazy 
1. Do pliku .html dodaj formularz z Bootstrapa. Dodaj metodę POST i 'name' do znacznika
'form' oraz `{% csrf_token %}`.
2. Stwórz nowy plik w aplikacji - 'forms.py', w którym zaimportuj swój model
oraz forms z django. Stwórz klasę formularza (tu: TaskForm) rozszerzającą
forms.ModelForm, z polami formularza jako klasa Meta. Meta klasa jest brana
pod uwagę w czasie tworzenia obiektu tej klasy.
3. W pliku views.py zaimportuj klasę formularza, następnie w widoku z formularzem
(tu: home) w przypadku POST pobierz dane z formularza i zapisz w bazie danych.
Dodaj message w przypadku udanego zapisu.
4. W .html wypisz message

Usuwanie obiektów z bazy - CRUD
1. W pliku urls.py dodaj 'path' do usuwania (delete) z `<task_id>`
2. W pliku views.py dodaj metodę delete_task, która pobierze `<task_id>` z url
i usunie task z tym id.
3. W pliku .html dodaj znacznik 'a' i w nim 'href' do url `delete/<task_id>` co pozwoli usuwać.

Edycja
1. Dodaj path do edycji w urls.py
2. We views.py dodaj metodę edit_task
3. Dodaj widok edit_task.html
4. Aby edytować done/not done postępuj jak wyżej.

Paginacja
1. W views.py import Pagination z django.core.paginator
2. W metodzie home dodaj kod definiujący paginację.
3. W html dodaj element paginujący z bootstrapa i połącz go z paginatorem z views.py

1. Aby zmienić kolor tła całej strony dodaj klasę bootstrapa z kolorem (np. bg-light) do znacznika 
'body' base.html.
2. Darmowe obrazki - unsplash

Autentykacja użytkowników
1. Stwórz nową aplikację (users_app)
    `django-admin startapp users_app`
2. Zarejestruj ją w settings.py i stwórz w niej plik urls.py z path dla 
'register':
    ```from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
]```
3. Stwórz plik forms.py w users_app:
```from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']```
3. W users_app/views.py zaimportuj CustomRegisterForm
i stwórz widok dla register.
4. Przygotuj register.html w users_app/templates.
5. Użyj crispy by poprawić wygląd formularza rejestracji:
    `pip install crispy-bootstrap5`
6. Dodaj 'crispy_forms' i 'crispy_bootstrap5' do settings.py i INSTALLED_APPS.
7. Na końcu settings.py dodaj info o CRISPY_TEMPLATE_PACK i
CRISPY_ALLOWED_TEMPLATE_PACKS.
8. W register.html dodaj instrukcję
`{% load crispy_forms_tags %}` i 
`{{ register_form|crispy }}` '|' oznacza filtrowanie w Jinja.

'user1, password888'

Logowanie
1. W urls.py dodaj import dla views z django.contrib.auth i path dla login
i logout. Te views pochodzą z django samego i używają 'form' jako 
formularza w pliku szablonu html. Pozwala to wyświetlić domyślny widok logowania.
2. Ze względu na to, że logowanie odbywa się na domyślnym "widoku", aby dokonać np.
'redirect' należy dodać LOGIN_REDIRECT_URL w settings.py i wskazać miejsce przeniesienia po
zalogowania.
3. Aby wylogować użytkownika stwórz logout.html, podaj do niego template w urls.py.
4. Uwaga, w Django 5.0 aby się wylogować należy użyć metody POST i tokena crsf, więc akcję logout
wykonuje się w formularzu (w szablonie base.html).

Restrykcja
1. Do views.py zawierający widoki, które mają być ograniczone do zalogowanych użytkowników
dodaj import 'login_required' z 'django.contrib.auth.decorators'.
2. Do widoku dodaj dekorator `@login_required`
3. W settings.py dodaj `LOGIN_URL = "login"` by w przypadku niezalogowanych użytkowników 
wskazać miejsce, do którego mają być przeniesieni (tu: strona logowania).

ForeignKey
1. Usuń dotychczasowe wpisy w bazie.
1. W pliku z modelem do modelu dodaj pole 'manage', które reprezentuje 
autora wpisu. Uwaga, w przeciwieństwie do kursu należy użyć 'auth.User' a nie 'User'
    `manage = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)`
2. Zmigruj bazę danych.
    `python manage.py makemigrations`
    `python manage.py migrate`
3. W views.py, w metodzie zapisującej dane z formularza do bazy danych
(tu: todolist) należy dodać pole 'manage' i ustawić na nim 'request.user'
zanim zapiszemy dane w bazie (czemu służy 'commit=False').
Gdy wyświetlamy wpisy (GET) należy dodać filtrowanie wpisów podług
użytkownika ('filter(manage=request.user)').
4. Zabezpiecz metody delete, pending_task, complete_task tak by tylko 
zalogowany użytkownik mógł z nich korzystać.
5. Szablon edit.html również wymaga takiego zabezpieczenia.

PostgreSQL
1. Usuń plik z bazą danych 'db.sqlite3'
2. Zainstaluj postgresql ze strony internetowej. Odklikaj 'stack builder',
podaj hasło
3. Zainstaluj psycopg2:
    `pip install psycopg2`
3. Zainstaluj django-environ, stwórz plik .env w katalogu z settings.py.
Upewnij się, że plik .env jest wpisany go .gitignore.
W settings.py dodaj 'import environ' oraz
    `env = environ.Env()` 
    `environ.Env.read_env()`    następnie podmień secret_key, debug, database (wszystko oprócz ENGINE) na `env('DJANGO_SECRET_KEY')` itp


5. Zrób migrację bazy danych, stwórz superusera.
    `python manage.py migrate`
    `python manage.py createsuperuser`

Deployment
1.  Zaktualizuj Django do wersji LTS:
    `pip install --upgrade django==<numer_wersji>`

2. W katalogu z plikiem manage.py stwórz .gitignore ze strony
 'https://github.com/github/gitignore/blob/main/Python.gitignore'


Railway
2. Install Gunicorn: `pip install gunicorn`
3. Zainstaluj whitenoise: `pip install whitenoise`
4. Create Procfile and add,
`web: python manage.py makemigrations && python manage.py migrate && gunicorn projekt_blog.wsgi`
5. Do settings.py dodaj
W sekcji Middlware, zaraz po 'middleware.security':
`'whitenoise.middleware.WhiteNoiseMiddleware'`
Poza tym dodaj:
`STATIC_URL = 'static/'`
`STATICFILES_DIRS = [BASE_DIR / "static",]`
`STATIC_ROOT = BASE_DIR / "staticfiles"`
5. `pip freeze > requirements.txt`
6. `python manage.py collectstatic`
7. W katalogu z manage.py zainicjuj repo i wyślij je na Githuba.

8. Stwórz nowy projekt na Railway - wybierz 'Deploy from Github' i znajdź
repo z apką.
9. Dodaj zmienne środowiskowe: DEBUG, SECRET_KEY, zmienne bazy danych (PGDATABASE, PGUSER, PGPASSWORD, PGHOST, PGPORT)
10. Dodaj bazę danych Postgres (guzik Create)
11. Kliknij 'Deploy'. Po szczęśliwym deployment kliknij 'View logs' by sprawdzić czy wszystko ok.
12. Przejdź do 'Networking' w ustawieniach i kliknij 'Generuj Domain'.
13. Zmień ALLOWED_HOSTS na adres domeny wygenerowanej:

`ALLOWED_HOSTS = ["taskmate-production-e8f2.up.railway.app", "localhost", "127.0.0.1"]`
`CSRF_TRUSTED_ORIGINS = ["https://taskmate-production-e8f2.up.railway.app"]`

Zdjęcia pochodzą z https://unsplash.com/s/photos/france

ctrl+w - usunięcie ostatniego słowa w terminalu


Mały, Pln
Beri, Pln
git reset --hard HEAD resetuje stan do ostatniego komita
git clean -fd usuwa pliki nieśledzione