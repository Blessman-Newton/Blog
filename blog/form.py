from .models import Post
from django import forms
 
 
class AddPost(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Post
        fields = ('headline','body_text')

