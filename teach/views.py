from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView, DeleteView
from .models import TeachFile


def download(request, pk):
    obj = TeachFile.objects.get(pk=pk)
    return redirect(obj.file.url)


class TeachPage(ListView):
    model = TeachFile
    template_name = "teach/index.html"


class SearchTeach(ListView):
    model = TeachFile
    template_name = "teach/index.html"

    def get_queryset(self):
        queryset = TeachFile.objects.all()
        q = self.request.GET.get("q")
        print(q)
        if q:
            return queryset.filter((Q(title__icontains=q) | Q(description__icontains=q)))
        return queryset
