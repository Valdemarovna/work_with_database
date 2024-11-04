from django.shortcuts import render, redirect
from phones.models import Phone
from django.forms.models import model_to_dict


def index(request):
    return redirect('catalog')


def get_name(dictionary):
    return dictionary['name']


def get_price(dictionary):
    return dictionary['price']


def show_catalog(request):
    template = 'catalog.html'
    temp_list = list()
    sort = request.GET.get('sort')
    for i in Phone.objects.all():
        temp_list.append(model_to_dict(i))
    if sort == 'name':
        temp_list.sort(key=get_name)
    elif sort == 'min_price':
        temp_list.sort(key=get_price)
    elif sort == 'max_price':
        temp_list.sort(reverse=True, key=get_price)
    context = {'phones':temp_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': model_to_dict(Phone.objects.get(slug=slug))}
    return render(request, template, context)
