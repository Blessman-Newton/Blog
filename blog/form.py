from .models import *
from django import forms
 
 
class AddPost(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Post
        fields = ['headline','body_text','img']
        widgets = {
            'body_text': forms.Textarea(attrs={"placeholder":'Post Here',
                                               'style':'width: 100vh; height: 50vh'})
        }

class Image(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Post
        fields = ['headline','body_text','img']