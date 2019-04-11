from django import forms
from home.models import Post
from accounts.models import Book1
class HomeForm(forms.ModelForm):
    language =forms.CharField(widget=forms.TextInput(attrs=
                                           {'class': 'special',
                                            'placeholder':'enter language...'}))
    location=forms.CharField(widget=forms.TextInput(attrs=
                                           {'class': 'special',
                                            'placeholder':'enter location...'}))
    class Meta:
        model =Post
        fields=(
            'language',
            'location',
        )
class BookForm(forms.ModelForm):

    column=forms.CharField(widget=forms.TextInput(attrs=
                                           {'class': 'special',
                                            'placeholder':'enter column'}))
    row=forms.CharField(widget=forms.TextInput(attrs=
                                           {'class': 'special',
                                            'placeholder':'enter row'}))
    class Meta:
        model= Book1
        fields=(
            'row',
            'column'
        )