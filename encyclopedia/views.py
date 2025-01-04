import random 
from django.shortcuts import render, redirect
from django import forms

from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea, label="Content")

class EditPageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label="Content")



def index(request):
    query = request.GET.get('q', '')
    if query:
        entries = util.list_entries()
        matching_entries = [entry for entry in entries if query.lower() in entry.lower()]
        
        # If the query matches exactly one of the entries, redirect to that entry's page
        if query.lower() in [entry.lower() for entry in entries]:
            return redirect('encyclopedia:title', title=query)
        
        # If no exact match, render search results page
        return render(request, 'encyclopedia/search.html', {
            'query': query,
            'results': matching_entries
        })
    else:
        entries = util.list_entries()
        return render(request, 'encyclopedia/index.html', {
            'entries': entries
        })

def title(request, title):
    aux = util.get_entry(title)
    if aux == None:
        return render(request, "encyclopedia/error.html")
    else:   
            return render(request, "encyclopedia/title.html", {
            "title" : aux,
            "realtitle" : title
        })
    return render(request, "encyclopedia/title.html", {
        "title" : aux,
        "realtitle" : title
    })


def create(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            if util.get_entry(title) is not None:
                return render(request, "encyclopedia/create.html", {
                    "form": form,
                    "error": "An entry with this title already exists."
                })
            
            util.save_entry(title, content)
            return redirect('encyclopedia:title', title=title)
    else:
        form = NewPageForm()

    return render(request, "encyclopedia/create.html", {
        "form": form
    })

def edit(request, title):
    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return redirect('encyclopedia:title', title=title)
    else:
        entry_content = util.get_entry(title)
        if entry_content is None:
            return render(request, "encyclopedia/error.html", {
                "message": "The requested page was not found."
            })
        form = EditPageForm(initial={'content': entry_content})
    
    return render(request, "encyclopedia/edit.html", {
        "form": form,
        "title": title
    })

def random_page(request):
    entries = util.list_entries()
    if entries:
        random_entry = random.choice(entries)
        return redirect('encyclopedia:title', title=random_entry)
    else:
        return render(request, "encyclopedia/error.html", {
            "message": "No entries found."
        })