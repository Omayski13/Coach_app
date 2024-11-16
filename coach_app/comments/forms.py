from django import forms

from coach_app.comments.models import Comment


class BaseCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class CommentAddForm(BaseCommentForm):
    pass