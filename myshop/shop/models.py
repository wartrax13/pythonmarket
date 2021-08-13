from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])  # pegar as URLS de urls.py


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)  # de um para muitos
    name = models.CharField(max_length=200, db_index=True)  # nome do produto
    slug = models.SlugField(max_length=200, db_index=True)  # urls
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)  # imagem opcional
    description = models.TextField(blank=True)  # descrição opcional
    price = models.DecimalField(max_digits=10, decimal_places=2)  # preço (sem o FLoat, para evitar problemas)
    available = models.BooleanField(default=True)  # está ou não disponível
    created = models.DateTimeField(auto_now_add=True)  # quando foi criado
    updated = models.DateTimeField(auto_now=True)  # quando foi atualizado pela última vez

    class Meta:  # para consultar os produtos por id e slug
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

#    def get_absolute_url(self):
#        return reverse('shop:product_detail', args=[self.id, self.slug])
