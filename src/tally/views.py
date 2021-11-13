from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import DrsModelSerializer, Drs
from tally import serializers

# class DrsModelViewSet(viewsets.ModelViewSet):
# 	queryset = Drs.objects.all()
# 	serializer_class = DrsModelSerializer
	# authentication_classes = [SessionAuthentication]
	# permission_classes = [IsAuthenticated]

@api_view(['GET'])
def home(request):
    api_urls = {
        'Report': 'DRS',
		'List':'/drs_report/list/',
		'Detail':'/drs_report/detail/<int:pk>/',
		'Create':'/drs_report/create/',
		'Update':'/drs_report/update/<int:pk>/',
		'Delete':'/drs_report/delete/<int:pk>/',
		}
    return Response(api_urls)


@api_view(['GET'])
def drsreportlist(request):
	obj = Drs.objects.all().order_by('-id')
	serializer = DrsModelSerializer(obj, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def drsreportdetail(request, pk):
	obj = Drs.objects.get(id=pk)
	serializer = DrsModelSerializer(obj, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def drsreportcreate(request):
	serializer = DrsModelSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def drsreportupdate(request, pk):
	task = Drs.objects.get(id=pk)
	serializer = DrsModelSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def drsreportselete(request, pk):
	task = Drs.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')