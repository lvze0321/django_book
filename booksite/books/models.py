#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BookManager(models.Manager):
    def title_count(self,keyword):
        return self.filter(title__icontains=keyword).count()

class Publisher(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 60)
    state_province = models.CharField(max_length = 30)
    country = models.CharField(max_length = 50)
    website = models.URLField()
#__unicode__这个函数用来返回某个值可以很好的用于查询和admin界面的显示
    def __unicode__(self):
        return self.name

#对数据库表对象的设置
    class Meta:
        ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    email = models.EmailField(blank=True,verbose_name = 'e-mail')
    def __unicode__(self):
        return u'%s %s'%(self.first_name,self.last_name)

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank = True,null = True)
    objects = BookManager()
    def __unicode__(self):
        return self.title
