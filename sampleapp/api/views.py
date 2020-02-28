from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ProjectSerializer
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from sampleapp.models import Project

class ProjectListView(ListAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer

class ProjectDetailView(RetrieveAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
