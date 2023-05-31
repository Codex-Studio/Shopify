from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    slug = models.CharField(
        max_length=100,
        verbose_name="Slug",
        unique=True
    )

    def __str__(self):
        return f"{self.title} {self.slug}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug()
        super().save(*args, **kwargs)

    def generate_slug(self):
        slug = slugify(self.title)
        base_slug = slug
        counter = 1
        while Category.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"