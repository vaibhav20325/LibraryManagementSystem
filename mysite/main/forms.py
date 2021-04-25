from django import forms

class BorrowRequest(forms.Form):
    time = forms.IntegerField(label = 'No. of Days', initial = 7)


class BorrowRenew(forms.Form):
    time = forms.IntegerField(label = 'No. of Days', initial = 7)