from django.contrib import admin
from webapp.models import Post_category, Post, User

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Post_category)
