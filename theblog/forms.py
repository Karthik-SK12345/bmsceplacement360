from django import forms
from .models import Post, Category, Comment

#choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment'),]
choices =  Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
	choice_list.append(item)


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('student_Name','company','Company_Logo', 'year_of_hiring','hiring_type','compensation_Details', 'author','number_hired_with_role', 'Interview_Rounds_with_detailed_description','Additional_Topics')

		widgets = {
			'student_Name': forms.TextInput(attrs={'class': 'form-control'}),
			'company': forms.TextInput(attrs={'class': 'form-control'}),
			'hiring_type': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
			#'author': forms.Select(attrs={'class': 'form-control'}),
			'compensation_Details': forms.TextInput(attrs={'class': 'form-control'}),	
			'number_hired_with_role': forms.TextInput(attrs={'class': 'form-control'}),
			'year_of_hiring': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'Interview_Rounds_with_detailed_description': forms.Textarea(attrs={'class': 'form-control'}),			
			'Additional_Topics': forms.Textarea(attrs={'class': 'form-control'}),	
			
					
		}


class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('student_Name','company','Company_Logo', 'year_of_hiring','hiring_type','compensation_Details', 'author','number_hired_with_role', 'Interview_Rounds_with_detailed_description','Additional_Topics')

		widgets = {
				'student_Name': forms.TextInput(attrs={'class': 'form-control'}),
				'company': forms.TextInput(attrs={'class': 'form-control'}),
			'hiring_type': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
			#'author': forms.Select(attrs={'class': 'form-control'}),
			'compensation_Details': forms.TextInput(attrs={'class': 'form-control'}),	
			'number_hired_with_role': forms.TextInput(attrs={'class': 'form-control'}),
			'year_of_hiring': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
			'Interview_Rounds_with_detailed_description': forms.Textarea(attrs={'class': 'form-control'}),			
			'Additional_Topics': forms.Textarea(attrs={'class': 'form-control'}),				
		}

 
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ( 'body',)

		widgets = {
			'body': forms.Textarea(attrs={'class': 'form-control'}),			
		}