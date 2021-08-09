from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .forms import WebForm
from django.views.generic import ListView



def webcrawl_input(request):
    
    task = False
    message = None
    if request.method == "GET":
        form = WebForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            message = f"{cd['Article_Url']}  and {cd['Article_Title']} and {cd['Words_Per_Column']}"
            request.session['url'] = cd['Article_Url']
            request.session['sub'] = cd['Article_Title']
            request.session['char'] = cd['Words_Per_Column']
            task = True
            
            #add.delay(request)
            # post = form.save(commit=False)
            # post.header = form['header']
            # post.sub_header =  form['sub_header']
            # post.character_len = form['character_len']
            # post.save()

    else:
        form = WebForm()

    return render(request,
                'post/detail.html', {'form': form, 'message': message, 'task':task})


