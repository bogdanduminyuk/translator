import django.forms as forms
from .widgets import *


class InputForm(forms.Form):
    words = forms.CharField(label="Слова для перевода",
                            widget=forms.Textarea(attrs={
                                        "class": "form-control",
                                        "rows": 15,
                                        "placeholder": "Впишите слова для перевода..."
                                })
                            )

    translate_option = forms.BooleanField(label='Перевести', required=False)

    synonyms_option = forms.BooleanField(label='Найти синонимы', required=False)

    antonyms_option = forms.BooleanField(label='Найти антонимы', required=False)

    definitions_option = forms.BooleanField(label='Найти определения', required=False)

    def is_valid(self):
        valid = super(InputForm, self).is_valid()

        for string in self.words.text.split('\n'):
            pass