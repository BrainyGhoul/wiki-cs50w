from django.shortcuts import render
from encyclopedia.util import get_entry, list_entries
import markdown2
import re


def index(request, entry):
    
    query = get_entry(entry)
    if query == None:
        return render(request, "goto_entries/index.html", {
            "entry": entry,
            "content": None
        })
    else:
        return render(request, "goto_entries/index.html", {
            "entry": entry,
            "content": markdown2.markdown(get_entry(entry)),
            "url": f"/edit/{entry}"
        })

def redirect(request):
    entries = list_entries()
    search_string = request.GET["q"]
    superstrings = []
    for entry in entries:

        if entry == search_string:
            return index(request, entry)
        
        if search_string.lower() in entry.lower():
            superstrings.append(entry)
    

    return render(request, "goto_entries/search.html", {
        "entries": superstrings,
        "length": len(superstrings)
    })