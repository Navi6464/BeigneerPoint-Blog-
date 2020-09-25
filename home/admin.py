from django.contrib import admin
from . models import Contact , Topic ,News , BlogComment
# Register your models here.


admin.site.register(Contact)

admin.site.register((Topic, BlogComment))

admin.site.register(News)


