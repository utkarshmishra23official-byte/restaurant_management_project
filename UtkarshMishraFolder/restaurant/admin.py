from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver