# Your imports should be here
from rest_framework.generics import ListAPIView
from restaurants.models import Restaurant
from .serializers import RestaurantListSerializer
from django.http import JsonResponse
# Complete me! I should be your APIListView

class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer

def resturant_list_api(request):
	restaurants = Restaurant.objects.all()
	json_restaurants =  RestaurantListSerializer(restaurants ,many=true).data
	return JsonResponse(json_restaurants, safe=False)