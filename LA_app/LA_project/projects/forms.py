from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'featured_img', 'tags', 'demo_link', 'source_link',]  # '__all__'