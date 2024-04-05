from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    input = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control',
                                                          'placeholder': ' Enter file', }))
