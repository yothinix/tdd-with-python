from django.http import HttpResponse
from django.shortcuts import redirect, render

from lists.models import Item


def home_page(request):
    #TODO
    # - Don't save blank items for every request
    # - Display multiple items in the table
    # - Support more than one list!

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
