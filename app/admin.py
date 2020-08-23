from django.contrib import admin

from app.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
