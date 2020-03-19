from django.shortcuts import render
from django.views import generic
from .models import Project
from .forms import *

from django.views.generic.edit import FormView
from rest_framework.generics import (ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView)
from .serializers import ProjectSerializer


class ProjectListView(ListAPIView):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer

class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectCreateView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDeleteView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectUpdateView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

def home(request):

    projects = Project.objects.all().order_by('created_on')
    return render(request, 'home.html', {'projects': projects})

def test(request):
    all_subjects = Project.objects.all().order_by('created_on')
    return render(request, 'test.html', {"Predmeti": all_subjects})

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'project_detail.html'

    def get_context_data(self, **kwargs):
        this_project = Project.objects.get(id=self.kwargs['pk'])
        context = super(ProjectDetail, self).get_context_data(**kwargs)

        return context

class ProjectView(FormView):
    template_name = 'add_project.html'
    form_class = ProjectForm
    success_url = '/home/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.


        project = form.save(commit=False)
        project.save()

        return super().form_valid(form)

def academic(request):
    return render(request, 'academic.html', {})

def profesional(request):
    return render(request, 'profesional.html', {})

def personal(request):
    return render(request, 'personal.html', {})

def predictive(request):
    return render(request, 'predictive.html', {})

def algorithm(request):
    return render(request, 'algorithm.html', {})

def optimization(request):
    return render(request, 'optimization.html', {})

def machine(request):
    return render(request, 'machine.html', {})

def spatial(request):
    return render(request, 'spatial.html', {})

def travel(request):
    return render(request, 'travel.html', {})

def places(request):
    return render(request, 'places.html', {})

def opinion(request):
    return render(request, 'opinion.html', {})

def album(request):
    return render(request,  'album.html', {})


def contact(request):
    return render(request,  'academic.html', {})
