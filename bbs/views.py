from django.shortcuts import render, redirect
from django.http import HttpResponse
from bbs.models import Message
from .forms import MessageCreateForm

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the bbs index.")
    messages = Message.objects.all()
    return render(request, "message_list.html", {
        "title" : "一言掲示板",
        "messages" : messages,
    })

def message_detail(request, id):
    message = Message.objects.get(id=id)
    return render(request, "message_detail.html", {
        "title" : f"id: {id} のメッセージ",
        "message" : message,
    })

def message_create(request):
    form = MessageCreateForm(request.POST or None)

    # フォーム送信時の処理
    if request.method == "POST" and form.is_valid():
        # # メッセージインスタンスを生成
        # message = Message()
        # # name と comment をフォームの値から設定
        # message.name = form.cleaned_data.get("name")
        # message.body = form.cleaned_data.get("body")
        # # Message インスタンスを保存
        # message.save()

        form.save()
        # 一覧ページへリダイレクト
        return redirect("/bbs/message_list/")
 
    return render(request, "message_create.html", {
        "title" : "新規投稿",
        "form" : form,
    })

def message_update(request, id):
    message = Message.objects.get(id=id)
    if request.method == "POST":
        # name と comment をフォームの値から更新
        message.name = request.POST.get("name")
        message.body = request.POST.get("body")
        # Message インスタンスを保存
        message.save()
        # 詳細ページへリダイレクト
        return redirect(f"/bbs/message_detail/{message.id}")
 

    return render(request, "message_update.html", {
        "title" : f"id: {id} のメッセージ",
        "message" : message,
    })

def message_delete(request, id):
    if request.method == "POST":
        message = Message.objects.get(id=id)
        message.delete()
 
    # 一覧ページへリダイレクト
    return redirect("/bbs/message_list/")