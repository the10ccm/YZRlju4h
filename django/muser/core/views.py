# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date

from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import CustomUser
from .forms import CustomUserForm, CustomUserFormSet


class UserList(ListView):
    """ List of user """
    template_name = 'core/user_list.html'
    queryset = get_user_model().objects.select_related('profile').all()
    context_object_name = 'users'


class UserCreate(CreateView):
    """ Create User View """
    template_name = 'core/user_create_form.html'
    model = get_user_model()
    form_class = UserCreationForm
    success_url = reverse_lazy('user_list')

    def _get_context_data(self, **kwargs):
        formset = CustomUserFormSet()
        context = super(UserCreate, self).get_context_data(**kwargs)
        context['formset'] = formset
        return context

    def get(self, request, *args, **kwargs):
        self.object = None
        formset = CustomUserFormSet()
        return self.render_to_response(
            self.get_context_data(formset=formset))

    def post(self, request, *args, **kwargs):
        self.object = None
        form = UserCreationForm(request.POST)
        formset = CustomUserFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            instance = form.save()
            for fs in formset:
                fs.instance.user = instance
                fs.save()
            return HttpResponseRedirect(self.success_url)
        # Invalid forms
        return self.render_to_response(
            self.get_context_data(formset=formset))


class UserUpdate(UpdateView):
    template_name = 'core/user_update_form.html'
    model = CustomUser
    form_class = CustomUserForm
    success_url = reverse_lazy('user_list')

    def get_context_data(self, **kwargs):
        context = super(UserUpdate, self).get_context_data(**kwargs)
        context['username'] = self.object.user.username
        context['pk'] = self.object.user.profile.pk
        return context

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk is not None:
            return self.model.objects.select_related('user').get(pk=pk)
        raise AttributeError("Unknown pk")


class UserDelete(DeleteView):
    # Leave this for history
    # template_name = 'core/user_confirm_delete.html'
    model = CustomUser
    success_url = reverse_lazy('user_list')

    def get(self, request, *args, **kwargs):
        """ Overrided to get rid the annoying confirmation """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.user.delete()
        return HttpResponseRedirect(success_url)
