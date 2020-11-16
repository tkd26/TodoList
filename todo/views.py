from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from .forms import TodoForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

    def get_queryset(self):
        sort = self.kwargs.get('sort', 'duedate')

        if sort=='title':
            return super().get_queryset().order_by('title')
        elif sort=='duedate':
            return super().get_queryset().order_by('duedate')
        elif sort=='priority':
            return super().get_queryset().order_by('priority')
        else:
            return super().get_queryset()

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    # fields = ('title', 'memo', 'priority', 'duedate')
    form_class = TodoForm
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')
    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse('list', args=request))
        else:
            return super(TodoDelete, self).post(request, *args, **kwargs)

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    # fields = ('title', 'memo', 'priority', 'duedate')
    form_class = TodoForm
    success_url = reverse_lazy('list')
    
    def form_invalid(self, form):
        print('修正内容の保存に失敗しました。')
        
        return super().form_invalid(form)