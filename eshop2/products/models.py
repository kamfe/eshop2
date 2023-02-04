from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.name

    def save(self):
        self.name = self.name[0].capitalize() + self.name[1:]
        super(Category, self).save()

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    units_in_stock = models.PositiveIntegerField(default=0)
    img = models.ImageField(upload_to='products_images/%Y/', null=True, blank=True)
    on_sale = models.BooleanField(default=False)
    category = models.ManyToManyField(to=Category)

    def __str__(self) -> str:
        category_list = [i.name for i in self.category.all()]
        category_list = ', '.join(category_list)
        return f'Product: {self.name}, Category: {category_list}'
