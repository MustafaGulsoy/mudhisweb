from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse


@api_view(['GET'])
def get_example(request):
    return JsonResponse({"test":12})


@api_view(['POST'])
def post_example(request):
    return JsonResponse({"test":34})
