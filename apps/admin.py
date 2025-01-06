from re import fullmatch

from django.contrib import admin
from .models import Data
from django.utils.html import format_html

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'location', 'full_time']

    def images(self, obj):
        if obj.photo and hasattr(obj.photo, 'url'):  # photo mavjudligini tekshirish
            return format_html(
                f'''<a href="{obj.photo.url}" target="_blank">
                            <img src="{obj.photo.url}" alt="image" width="150" height="100" 
                                 style="object-fit: cover;"/>
                        </a>'''
            )
        return "No Image"  # Agar fayl bo'lmasa, xatolik chiqarish o'rniga bu matnni qaytaramiz
    images.short_description = "Image Preview"

    def img(self, obj):
        if obj.photo and hasattr(obj.photo, 'url'):  # photo mavjudligini tekshirish
            return format_html(
                f'''<a href="{obj.photo.url}" target="_blank">
                              <img src="{obj.photo.url}" alt="image" width="150" height="100"
                                   style="object-fit: cover;"/>
                          </a>'''
            )
        return "No Image"
    img.short_description = "Clickable Image"
