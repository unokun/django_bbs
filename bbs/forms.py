# forms をインポート
from django import forms
 
from .models import Message

# Form クラスを継承
# class MessageCreateForm(forms.Form):
class MessageCreateForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('created_at',)
 
    # name の入力フォームを作成
    # name = forms.CharField(
    #     label="お名前", # label の文字列
    #     required=True, # 必須か否か
    #     widget=forms.TextInput() # 入力欄は type="text"
    # )
    # body = forms.CharField(
    #     label="本文",
    #     required=True,
    #     widget=forms.TextInput()
    # )