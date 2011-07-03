from django import forms

class RssUrlForm(forms.Form):
    url = forms.URLField(label='Rss url', initial='http://')


class RssRefreshForm(forms.Form):
    id = forms.IntegerField()
