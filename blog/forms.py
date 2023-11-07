from django import forms
from .models import Post, Comment, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'content', 'thumb_image', 'file_upload', 'tags'] 
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control postform'}),
            'content': forms.Textarea(attrs={'class': 'form-control postform', 'rows': 8, 'placeholder' : "글을 작성해주세요"}),
            'thumb_image': forms.ClearableFileInput(attrs={'class': 'form-control-file postform'}),
            'file_upload': forms.ClearableFileInput(attrs={'class': 'form-control-file postform'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control postform'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40, 'placeholder' : "댓글을 남겨주세요."})
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']