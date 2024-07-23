from django import forms
import _project_.widgets as widgets
from . import models


class MessageForm(forms.ModelForm):
    class Meta:
        model = models.ForumMessage
        fields = ('content', )

        labels = {
            'content': 'Содержание',
        }
        widgets = {
            'content': forms.Textarea(
                attrs={
                    "rows": 16,
                    "cols": 64
                }
            )
        }
