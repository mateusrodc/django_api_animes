from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome_categoria= models.CharField(max_length=255)

    class Meta:
        ordering = ['nome_categoria']
        verbose_name='Categoria'

    def __str__(self):
        return self.nome_categoria

class Status(models.Model):
    situacao= models.CharField(max_length=255)
    observacao= models.CharField(max_length=255,null=True,blank=True)

    class Meta:
        ordering= ['situacao']
        verbose_name='Status'

    def __str__(self):
        return self.situacao

class Autor(models.Model):
    nome= models.CharField(max_length=255)
    sobrenome= models.CharField(max_length=255)
    idade= models.IntegerField()
    sexo= models.CharField(max_length=10)
    cpf= models.CharField(max_length=15)

    class Meta:
        ordering= ['nome','sobrenome']
        verbose_name= 'autor'

    def __str__(self):
        return '{},{}'.format(self.nome,self.sobrenome)

class Anime(models.Model):

    nome= models.CharField(max_length=255)
    autor= models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria= models.ForeignKey(Categoria,on_delete=models.CASCADE)
    status= models.ForeignKey(Status,on_delete=models.CASCADE)
    ano_lancamento= models.IntegerField()
    qt_episodio= models.IntegerField()
    duracao_episodio= models.TimeField()
    sinopse= models.CharField(max_length=300,null=True,blank=True)
    classificacao= models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        ordering= ['nome','ano_lancamento']
        verbose_name='Anime'

    def __str__(self):
        return '{},{}'.format(self.nome,self.ano_lancamento)

    


