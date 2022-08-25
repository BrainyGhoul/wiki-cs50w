from django.shortcuts import render, redirect
import re
from . import util
import random


def index(request):
    entries = util.list_entries()

    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def random_page(request):
    page = random.choice(util.list_entries())
    return redirect("goto_entries:show_entry", page)
