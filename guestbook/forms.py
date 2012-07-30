from django import forms

class MessageForm(forms.Form):
    name = forms.CharField(max_length=100,required=False) #False because optional
    message = forms.CharField(widget=forms.Textarea)
