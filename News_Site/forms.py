from django import forms


class AddNews(forms.Form):
    name = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()

    # fix css bootstrap

    name.widget.attrs.update({'class': "form-control"})
    content.widget.attrs.update({'class': "form-control"})
    #image.widget.attrs.update({'class': "form-control"})
