from .models import Psubjects
from rest_framework import viewsets
from .Serializers import PsubjectsSerializers

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Psubjects.objects.all().order_by('-date_created')
    serializer_class = PsubjectsSerializers


# Create your views here.
