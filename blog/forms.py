from django import forms
from .models import Post
from .models import CV
from .models import WorkExperience
from .models import Education
from .models import Activity
from .models import Calligraphy
from .models import Photography

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text', "image",)


class CVForm(forms.ModelForm):

	class Meta:
		model = CV
		fields = ("name", "title", "email", "website", "number", "headshot", "personal_profile", "skills",)


class WorkExperienceForm(forms.ModelForm):

	class Meta:
		model = WorkExperience
		fields = ("title", "company", "duration", "description",)


class EducationForm(forms.ModelForm):

	class Meta:
		model = Education
		fields = ("institution", "qualification", "duration", "description",)


class ActivityForm(forms.ModelForm):
	
	class Meta:
		model = Activity
		fields = ("title", "description",)


class CalligraphyForm(forms.ModelForm):

	class Meta:
		model = Calligraphy
		fields = ("description", "image", )


class PhotographyForm(forms.ModelForm):

	class Meta:
		model = Photography
		fields = ("description", "image", )