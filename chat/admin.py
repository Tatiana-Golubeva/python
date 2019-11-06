from django.contrib import admin
from chat.models import User, Chat, Message

admin.site.register(User)
admin.site.register(Chat)
admin.site.register(Message)

# Register your models here.
