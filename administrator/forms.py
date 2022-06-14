from django import forms
from.models import school


class Add_std(forms.ModelForm):

	class Meta:

		model = school

		fields = ('stname' , 'stcls' , 'stroll' , 'staddr')


		widgets = {

			'stname' : forms.TextInput(attrs={'class': 'form-control' , 'placeholder' : 'Enter the name'}),
			'stcls' : forms.TextInput(attrs={'class': 'form-control' , 'placeholder' : 'Enter the class'}),
			'stroll' : forms.TextInput(attrs={'class': 'form-control' , 'placeholder' : 'Enter the roll number'}),
			'staddr' : forms.TextInput(attrs={'class': 'form-control' , 'placeholder' : 'Enter the address'}),
		}