from django.shortcuts import render
from django import forms
from encyclopedia.util import save_entry, list_entries
from django.shortcuts import redirect
import markdown2

class NewEntry(forms.Form):

    title = forms.CharField(label="Title")
    discription = forms.CharField(label="", widget=forms.Textarea(attrs={"class": "form-control"}))

def index(request):
    if request.method == "POST":
        form = NewEntry(request.POST)
        if form.is_valid() and (len([i for i in list_entries() if i.lower() == form.cleaned_data['title'].lower()]) == 0):
            save_entry(form.cleaned_data['title'], form.cleaned_data['discription'])
            return redirect("goto_entries:show_entry", entry=form.cleaned_data["title"])
        else:
            return render(request, "post_entries/new.html", {
                "form": form,
                'isnew': False
            })

    return render(request, "post_entries/new.html", {
        "form": NewEntry(),
        "isnew": True
    })