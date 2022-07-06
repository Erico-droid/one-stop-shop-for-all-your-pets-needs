from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from accounts.models import User
from django.urls import reverse


class Post(models.Model):                                                   #Blog Post model
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.user}"

    @property
    def number_of_comments(self):
        return BlogComment.objects.filter(post=self).count()
