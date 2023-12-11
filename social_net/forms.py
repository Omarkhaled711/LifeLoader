from django import forms
from social_net.models import Comment


class CommentForm(forms.ModelForm):
    """
    A form for creating or updating comments on posts.

    This form is specifically designed for creating or updating Comment objects
    associated with posts.

    Fields:
        - content: The content of the comment.

    Widgets:
        - 'content': Textarea widget with adjustable rows and columns.

     Note:
        Adjust the 'rows' and 'cols' attributes in the 'content' widget as
        needed for styling.
    """
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }
