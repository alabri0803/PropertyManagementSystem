from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Property


def property_list(request):
  query = request.GET.get('q')
  city = request.GET.get('city')
  type_filter = request.GET.get('type')
  status = request.GET.get('status')
  properties = Property.objects.all()
  if query:
    properties = properties.filter(Q(title__icontains=query) | Q(description__icontains=query))
  if city:
    properties = properties.filter(city__icontains=city)
  if type_filter:
    properties = properties.filter(type=type_filter)
  if status:
    properties = properties.filter(status=status)
  return render(request, 'properties/property_list.html', {'properties': properties})

def property_detail(request, pk):
  property = get_object_or_404(Property, pk=pk)
  return render(request, 'properties/property_detail.html', {'property': property})