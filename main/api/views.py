from rest_framework import generics
from ..models import Suscriptor
from .serializers import SuscriptorSerializer



class SuscriptorListView(generics.ListAPIView):
	queryset = Suscriptor.objects.all()
	serializer_class = SuscriptorSerializer

class SuscriptorDetailView(generics.RetrieveAPIView):
	queryset = Suscriptor.objects.all()
	serializers_class = SuscriptorSerializer


from rest_framework.permissions import IsAdminUser

class SuscriptorCreateView(generics.ListCreateAPIView):
	queryset = Suscriptor.objects.all()
	serializer_class = SuscriptorSerializer
	permission_classes = (IsAdminUser,)