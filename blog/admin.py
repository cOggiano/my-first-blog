from django.contrib import admin
from .models import Post

#stiamo importando il modello Post definito inn models.py e lo registriamo
admin.site.register(Post)

