from django.shortcuts import render, redirect
from .models import URL
from .forms import URLForm
from .utils import url_generator


# mongod --dbpath \..\..\mongoDB-databases\
def index(request):
    form = URLForm()
    if request.method == 'POST':
        form = URLForm(request.POST)

        if form.is_valid():
            url = URL()
            url.user_url = form['user_url'].value()
            url.shortened_url = url_generator.new_url_generator()
            url.save()
            context = {'url': request.get_host() + '/' + url.shortened_url}
            return render(request, 'shortener_app/generated_url.html', context)

    context = {'form': form}
    return render(request, 'shortener_app/index.html', context)


def redirect_url(request, pk):
    try:
        url = URL.objects.get(shortened_url=pk)
    except Exception:
        return render(request, 'shortener_app/wrong_url.html')

    return redirect(url.user_url)
