from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Chat(models.Model):
    first_user = models.ForeignKey(User, related_name='first_user', on_delete=models.CASCADE)
    second_user = models.ForeignKey(User, related_name='second_user', on_delete=models.CASCADE)

    def __str__(self):
        return 'chat between {} and {}'.format(self.first_user.username, self.second_user.username)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300, null=False, default='')

    def __str__(self):
        return '{}: {}'.format(self.user.username, self.content)

# Create your models here.
