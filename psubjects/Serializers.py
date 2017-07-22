from .models import Psubjects
from rest_framework import serializers

class PsubjectsSerializers(serializers.ModelSerializer):
    doc = serializers.FileField(max_length=None, use_url=True)

    class Meta:
        model = Psubjects
        fields = ('id', 'Patient_name', 'date_created', 'doc')