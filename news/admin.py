from django.contrib import admin
from .models import NewsPost,Category

admin.site.register(Category)
@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'categorys', 'pub_date', 'avilable')
    list_filter = ('avilable', 'categorys', 'pub_date')


