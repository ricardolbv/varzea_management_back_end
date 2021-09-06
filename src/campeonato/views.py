from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


@swagger_auto_schema(methods=['get'])
@api_view(['GET'])
def say_hello(request):
    return HttpResponse('HelloWord')
