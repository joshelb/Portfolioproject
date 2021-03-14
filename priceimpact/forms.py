from django import forms


class mainForm(forms.Form):
     CHOICES = (
          ("BTCUSD","BTCUSD"),
          ("ETHUSD","ETHUSD"),
     )
     symbol = forms.ChoiceField(choices=CHOICES)
