from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','context','pub_time')
    list_filter = ('pub_time',)


admin.site.register(Article, ArticleAdmin)

# Register your models here.
