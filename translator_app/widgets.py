from django import forms


class CustomTextArea(forms.Textarea):
    def __init__(self, size_tuple):
        rows, cols = size_tuple
        super(CustomTextArea, self).__init__(attrs={
            'class': 'form-control',
            'rows': rows,
            'cols': cols,
        })
