from django import forms
from social_net.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            # Adjust rows and cols as needed
            'content': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }
