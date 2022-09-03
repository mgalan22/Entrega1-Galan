from django.contrib import admin
from webapp.models import Post_categories, Posts, Users

admin.site.register(Posts)
admin.site.register(Users)
admin.site.register(Post_categories)
