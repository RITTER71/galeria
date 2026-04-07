from django.db import models
from PIL import Image
from contextlib import suppress

class Foto(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='fotos/')
    orientacion = models.CharField(max_length=10, editable=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.imagen:
            return

        # Works with local filesystem and remote storages (e.g. Cloudinary).
        with suppress(Exception):
            self.imagen.open("rb")
            img = Image.open(self.imagen)
            img.load()
            self.orientacion = "horizontal" if img.width > img.height else "vertical"

        super().save(update_fields=['orientacion'])

    def __str__(self):
        return self.titulo
