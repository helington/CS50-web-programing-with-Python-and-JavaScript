from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from encyclopedia.functions import compare_string
from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label="title")
    text_area = forms.CharField(widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, title):
    return render(request, "encyclopedia/entry_page.html", {
        "entry": util.get_entry(title),
        "title": title
    })

def search(request):
    results = []
    if request.method == "GET":
        search_querry = request.GET.get('q')
        string_compare = compare_string(search_querry, util.list_entries())
        if string_compare[0] == True:
            return HttpResponseRedirect(f"/wiki/{string_compare[1]}")
        else:
            for entry in util.list_entries():
                if search_querry.lower() in entry.lower():
                    results.append(entry)

            return render(request, "encyclopedia/result_page.html", {
                "results": results
            })

def add(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            text_area = form.cleaned_data["text_area"]

        else:
            return render(request, "encyclopedia(add.html", {
                "form": form
            })
    return render(request, "encyclopedia/add.html", {
        "form": NewPageForm()
    })