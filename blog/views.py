from http.client import HTTPResponse
from django.shortcuts import render, redirect

from blog.forms import CommentForm
from .models import Post



def frontpage(request):
    posts = Post.objects.all()
    return render(request, "blog/frontpage.html", {"posts": posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                # コメントが有効ならFormをセーブ

                return redirect("post_detail", slug=post.slug)
# リダイレクトはどこにページを遷移するか。送信したあとにどこに飛ぶか。今回は現在の詳細ページに飛ぶ
    else:
        form = CommentForm()





    return render(request, "blog/post_detail.html",{"post":post, "form": form})