from __future__ import unicode_literals

from django.db import models
from uuslug import uuslug
from ckeditor.fields import RichTextField


STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('withdrawn', 'Withdrawn'),
)


class Category(models.Model):
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('Slug')
    icon = models.CharField('Icon', max_length=50, default='')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuslug(self.name, instance=self)
        super(Category, self).save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField('Slug', default='')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuslug(self.title, instance=self)
        super(Tag, self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    description = RichTextField(config_name='ckeditor')
    content = RichTextField(config_name='ckeditor')
    date = models.DateTimeField()
    image = models.ImageField(null=True, blank=True, upload_to='images/posts', verbose_name=u'Images')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='draft')
    views = models.IntegerField(default=0)
    slug = models.SlugField('Slug')
    tag = models.ManyToManyField(Tag, related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ("-date",)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuslug(self.title, instance=self)
        super(Post, self).save(*args, **kwargs)


class Event(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    content = RichTextField(config_name='ckeditor')
    ev_date = models.CharField(max_length=255)
    ev_place = models.CharField(max_length=255, default='')
    date = models.DateTimeField()
    image = models.ImageField(null=True, blank=True, upload_to='images/events', verbose_name=u'Images')
    slug = models.SlugField('Slug')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='draft')

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ("-date",)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuslug(self.title, instance=self)
        super(Event, self).save(*args, **kwargs)


class Fact(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    content = RichTextField(config_name='ckeditor')
    date = models.DateTimeField()
    image = models.ImageField(null=True, blank=True, upload_to='images/facts', verbose_name=u'Images')
    slug = models.SlugField('Slug')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='draft')

    class Meta:
        verbose_name = 'Fact'
        verbose_name_plural = 'Facts'
        ordering = ("-date",)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuslug(self.title, instance=self)
        super(Fact, self).save(*args, **kwargs)
