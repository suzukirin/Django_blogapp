from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    # 番号
    intro = models.TextField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    # 投稿すると自動的に日時を取得できる

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    # 紐付けられているものが一つでも削除されたら全て削除する
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)