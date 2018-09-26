from rest_framework import serializers
from ..models import Suscriptor

class SuscriptorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Suscriptor
		fields = ('id', 'nombre', 'email')