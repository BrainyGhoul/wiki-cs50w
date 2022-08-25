from django.shortcuts import render
from django import forms
from encyclopedia.util import get_entry, save_entry
from django.shortcuts import redirect


def index(request, entry):
    global name
    name = entry
    class EditForm(forms.Form):
        text = forms.CharField(widget=forms.Textarea(attrs={}), initial=get_entry(name))
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            save_entry(entry, form.cleaned_data["text"])
            return redirect("goto_entries:show_entry", entry=entry)
        else:
            return render(request, "edit/index.html", {
                'title': entry,
                "form": form
            })
    return render(request, "edit/index.html", {
        "title": entry,
        "form": EditForm()
    })

