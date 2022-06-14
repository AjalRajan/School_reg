from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from administrator.models import school
from django.urls import reverse_lazy
from .forms import Add_std

class Home(ListView):

	model = school

	template_name = 'administrator/home.html'

	ordering = ['stcls',"stroll"]

class Addstd(CreateView):

	model = school

	form_class = Add_std
	template_name = 'administrator/add_stud.html'


class Updatestd(UpdateView):

	model = school

	fields = ['stname' , 'stroll' , 'stcls' , 'staddr']

	template_name = 'administrator/update_stud.html'

class Deletestu(DeleteView):

	model = school
	template_name = 'administrator/del_stud.html'

	success_url = reverse_lazy('home')