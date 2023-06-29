from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Data
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def is_correct(request, pk):
    data = Data.objects.filter(pk=pk)
    update_data = data[0]
    update_data.isCorrect = True
    update_data.save()

    data = Data.objects.all() #filter(isCorrect = False)

    p = Paginator(data, 1)

    page_number = request.GET.get('page')

    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    context = {
        'page_obj' : page_obj
    }

    # return redirect(f'{index}?{page_number}')
    return redirect("index")
    # return render(request, "valsite/index.html", context)


def update_text(request, pk, page):
    text = request.GET.get('q') if request.GET.get('q') != None else ""
    data = Data.objects.filter(pk = pk) #filter(isCorrect = False)

    p = Paginator(data, 1)
    # page_number = request.GET.get('page')



    if text != None:
        # data = Data.objects.filter(pk=pk)
        update_data = data[0]

        update_data.correctText = text
        update_data.save()



    
    url = reverse('main',  kwargs={'pk':1}) + f"?page={page}"
    return HttpResponseRedirect(url)

    # return redirect("index")
    # return render(request, "valsite/index.html", context)


def main(request, pk):

    if request.method == 'POST':
        data = Data.objects.filter(pk=pk)
        update_data = data[0]
        update_data.isCorrect = True
        update_data.save()

        return redirect(request.META.get('HTTP_REFERER'))

        # return render('index', pk)



    if request.method == 'GET':
        text = request.GET.get('q') if request.GET.get('q') != None else ""
        data = Data.objects.all() #filter(isCorrect = False)

        if text != None:
            # data = Data.objects.filter(pk=pk)
            update_data = data[0]

            update_data.text = text
            update_data.save()
 
            p = Paginator(data, 1)

            page_number = request.GET.get('page')
            page_obj = p.get_page(page_number)

            context = {
                'page_obj' : page_obj
            }

            # url = reverse('main',  kwargs={'pk':1}) + f"?page={page_number}"
            # return HttpResponseRedirect(url)





    
    
    
    data = Data.objects.all() #filter(isCorrect = False)
    p = Paginator(data, 1)

    page_number = request.GET.get('page')

    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    context = {
        'page_obj' : page_obj
    }

    return render(request, "valsite/main.html", context)

def index(request):

    data = Data.objects.filter()[:1].get()
    id = data.id

    context = {
        'id': id
    }

    return render(request, "valsite/index.html", context)