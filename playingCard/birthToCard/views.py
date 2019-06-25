from django.shortcuts import render
from .form import Date
from django.http import HttpResponseRedirect
from . import dateToCard
# Create your views here.
def index(request):
    return render(request, 'page/index.html')

def getDate(request):
    #post method
    if request.method == 'POST':
        #tao form
        dateForm = Date(request.POST)

        if dateForm.is_valid():
            date = dateForm.cleaned_data.get('birth_date')
            name_card , card_content = dateToCard.getCard(date.day, date.month)
            card = name_card[0]
            img_name = name_card[1]
            img_path = '/image/{}.svg'.format(img_name)
            print(img_path)
            contex = {'birthday': date, 'image': img_path, 'card' : card,'num_content': card_content['number'], 'shape_content': card_content['shape']}
            return render(request,'page/result.html', contex)

    else:
        dateForm = Date()

    return render(request, 'page/index.html', {'form': dateForm})


#link : http://localhost:8000//accounts/facebook/login/?process=login%22