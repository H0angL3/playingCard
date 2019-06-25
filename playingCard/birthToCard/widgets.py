from django.forms import widgets
from django.utils.formats import get_format
class DateSelect(widgets.SelectDateWidget):

    @staticmethod
    def _parse_date_fmt():
        fmt = get_format('j N, Y')
        escaped = False
        for char in fmt:
            if escaped:
                escaped = False
            elif char == '\\':
                escaped = True
            elif char in 'Yy':
                yield 'year'
            elif char in 'bEFMmNn':
                yield 'month'
            elif char in 'dj':
                yield 'day'