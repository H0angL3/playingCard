from django import forms
from . import widgets

MONTHS = {
    1: ('Tháng 1'), 2:('Tháng 2'), 3:('Tháng 3'), 4:('Tháng 4'),
    5:('Tháng 5'), 6:('Tháng 6'), 7:('Tháng 7'), 8:('Tháng 8'),
    9:('Tháng 9'), 10:('Tháng 10'), 11:('Tháng 11'), 12:('Tháng 12')}
YEAR = [x for x in range(1900,2019)]

class Date(forms.Form):

    birth_date = forms.DateField(label='',widget=widgets.DateSelect(years=YEAR,months=MONTHS, attrs={'class':'birth_widget'}))

