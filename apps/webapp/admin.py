from django.contrib import admin

from webapp.models import Post, Category, Event, Fact, Tag


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'tag', 'category', 'description', 'content', 'date', 'image']
    list_display = ['title', 'slug', 'status', 'date', 'views', 'category']
    list_filter = ['date', 'title', 'category', 'status', 'views']
    search_fields = ['title', 'status', 'date', 'category', 'author']
    actions = ['make_published']

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='published')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
            self.message_user(request, "%s successfully marked as published." % message_bit)


class EventAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'content', 'ev_date', 'ev_place', 'date', 'image']
    list_display = ['title', 'slug', 'status', 'author', 'date']
    list_filter = ['title', 'author', 'status', 'date']
    search_fields = ['title', 'status', 'author', 'date']
    actions = ['make_published']

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='published')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
            self.message_user(request, "%s successfully marked as published." % message_bit)


class FactAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'content', 'date', 'image']
    list_display = ['title', 'slug', 'status', 'author', 'date']
    list_filter = ['title', 'status', 'author', 'date']
    search_fields = ['title', 'status', 'author', 'date']
    actions = ['make_published']

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='published')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
            self.message_user(request, "%s successfully marked as published." % message_bit)


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'icon']
    list_display = ['name', 'slug']


class TagAdmin(admin.ModelAdmin):
    fields = ['title']
    list_display = ['title', 'slug']

admin.site.register(Post, PostAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Fact, FactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
