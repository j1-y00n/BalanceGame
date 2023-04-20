from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'select1_content',
                  'select2_content', 'image1', 'image2')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'select1_content': forms.Textarea(attrs={'class': 'form-control', 'rows': '2', }),
            'select2_content': forms.Textarea(attrs={'class': 'form-control', 'rows': '2', }),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content': '댓글',
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '2', })
        }
