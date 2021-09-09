from django.contrib import admin
from .models import Category, Product, Slider
# from translations.admin import TranslatableAdmin, TranslationInline


# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Slider)
