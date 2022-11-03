from django.db import models

class Configuarcion(models.Model):
    nombre_blog = models.CharField(max_lenght=14)
    contruido_por = models.CharField(max_lenght=30)
    titulo_principal = models.CharField(max_lenght=40)
    subtitulo_principal = models.CharField(max_lenght=40)

class Post(models.Model):
    title = models.CharField(max_lenght=100)
    short_content = models.CharField(max_lenght=255)
    content = models.CharField(max_lenght=3000)
    date_published = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to= "posts", null=True, blank=True)

    def __str__(self):
        return f"id:{self.id}, title:{self.title}"
