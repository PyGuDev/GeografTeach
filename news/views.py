#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.db.models import Q
from .models import NewsPost, Category


class NewsPage(ListView):
    model = NewsPost
    template_name = "news/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = Category.objects.all()
        return context
    
    def get_queryset(self):
        queryset = NewsPost.objects.all().order_by("-pk")
        print(self.request)
        s = self.request.GET.get("s")
        q = self.request.GET.get("q")
        if q:
            return queryset.filter((Q(title__icontains=q)|Q(text__icontains=q)))
        if s:
            return queryset.filter((Q(categorys__name__icontains=s)))
        return queryset


class NewsPageDetail(DeleteView):
    model = NewsPost
    template_name = "news/detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pks = self.request.path.rsplit('/')
        pks = pks[pks.__len__()-2]
        visit_post = NewsPost.objects.get(pk=pks);
        visit_post.visite_count += 1
        visit_post.save() 
        return context

