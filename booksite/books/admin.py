#coding=utf-8
from django.contrib import admin
from books.models import Publisher,Author,Book

# Register your models here.
#以下两个类是对admin主页的效果配置，变量名固定继承于ModelAdmin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title','author','publisher','publication_date')


admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
