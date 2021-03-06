from django.db import models
from django.forms import model_to_dict
from core.models import BaseModel
from crum import get_current_user

# Create your models here.

#Modelo de la base de datos, llamando a la clase BaseModel para discriminacion de usuarios
class Categoria(BaseModel):
    #modelo category con personalizaciones específicas
    category = models.CharField(max_length=50, verbose_name='Categoria')

    #Elemento para gusradar la categoría dependiendo de su id identificador
    def save(self, force_insert=False, force_update=False, usig=None,
             update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            self.modified_by = user
        super(Categoria, self).save()

    def __str__(self):
        return self.category

    def toJson(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']
