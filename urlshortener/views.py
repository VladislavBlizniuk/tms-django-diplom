'''
Shortener views
'''
from django.shortcuts import render # We will use it later
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect


# Model
from .models import Shortener

# Custom form

from .forms import ShortenerForm, UrlUpdateForm

# Create your views here.

def home_view(request):
    
    template = 'urlshortener/home.html'

    context = {}

    data = Shortener.objects.all()
    context['links'] = data
    context['absolute_uri'] = request.build_absolute_uri('/')
    try:
        context['new_url'] = data[0].short_url
        context['long_url'] = data[0].long_url
    except:
        pass
    # Empty form
    context['form'] = ShortenerForm()


    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':

        used_form = ShortenerForm(request.POST)

        if used_form.is_valid():
            
            shortened_object = used_form.save()

            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            
            long_url = shortened_object.long_url 
             
            context['new_url']  = new_url
            context['long_url'] = long_url
            
            return HttpResponseRedirect(reverse("home", ))

        context['errors'] = used_form.errors

        return render(request, template, context)
    
def redirect_url_view(request, shortened_part):

    try:
        shortener = Shortener.objects.get(short_url=shortened_part)

        shortener.times_followed += 1        

        shortener.save()
        
        return HttpResponseRedirect(shortener.long_url)
        
    except:
        raise Http404('Sorry this link is broken :(')
    


def show_url_info(request, shortened_part):
    try:
            
        template = 'urlshortener/info.html'

        current_url = Shortener.objects.get(short_url=shortened_part)

        context = {"url": current_url, "absolute_uri": request.build_absolute_uri('/')}
        context['form'] = UrlUpdateForm()

        if request.method == 'GET':
            return render(request, template, context)

        elif request.method == 'POST':

            used_form = UrlUpdateForm(request.POST)

            if used_form.is_valid():

                current_url.long_url = used_form.cleaned_data['long_url']
                current_url.save()
                return HttpResponseRedirect(reverse("info", args=[shortened_part]))

            context['errors'] = used_form.errors

            return render(request, template, context)

    except Exception as e:
        print(e)
        raise Http404('Sorry this link is broken :(')
    
def redirect_home(request):
    return HttpResponseRedirect(reverse("home"))

def delete_url(request, shortened_part):
    try:
        Shortener.objects.filter(short_url=shortened_part).delete()
        return HttpResponseRedirect(reverse("home"))
    except:
        raise Http404('Sorry this link is broken :(')