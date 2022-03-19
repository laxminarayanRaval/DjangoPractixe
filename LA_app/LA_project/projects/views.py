from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', {'projects': projects})

def project(request, pk):
    project = Project.objects.get(title=pk)
    # print(project)
    return HttpResponse(render(request, 'projects/project.html', {'project': project}))

def createProject(request):
    template_name = 'projects/project_form.html'
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    # print(form)
    return render(request, template_name, context)

def updateProject(request, pk):
    template_name = 'projects/project_form.html'
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    
    context = {'form': form}
    # print(form)
    return render(request, template_name, context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if project:
        project.delete()
        return redirect('projects')
    # return  # if not found then

def upvoteProject(request, pk):
    print('upvote', pk)
    # project = Project.objects.get(id=pk)
    # form = ProjectForm(instance=project)

    # if request.method == 'POST':
        # form = ProjectForm(request.POST, instance=project)
        # if form.is_valid():
            # form.save()
            # return redirect('projects')
    
    # context = {'form': form}
    # print(form)
    return redirect('projects/'+pk)

def downvoteProject(request, pk):
    print('downvote', pk)
    template_name = 'projects/project_form.html'

