from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import DrsModelSerializer, Drs


@api_view(["GET"])
def home(request):
    api_urls = {
        "=== Authentication URLs ===": "=============================",
        "rest_password_reset_confirm": "auth/password/reset/confirm",
        "rest_password_reset        ": "auth/password/reset/",
        "rest_password_change       ": "auth/password/change",
        "signup                     ": "auth/registration",
        "rest_login                 ": "auth/login",
        "rest_logout                ": "auth/logout",
        "rest_user_details          ": "auth/user",
        "======== DRS Report =======": "=============================",
        "List                       ": "/drs_report/list/",
        "Detail                     ": "/drs_report/detail/<int:pk>/",
        "Create                     ": "/drs_report/create/",
        "Update                     ": "/drs_report/update/<int:pk>/",
        "Delete                     ": "/drs_report/delete/<int:pk>/",
    }
    return Response(api_urls)


@api_view(["GET"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def drsreportlist(request):
    obj = Drs.objects.all().order_by("-id")
    serializer = DrsModelSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def drsreportdetail(request, pk):
    obj = Drs.objects.get(id=pk)
    serializer = DrsModelSerializer(obj, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def drsreportcreate(request):
    serializer = DrsModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data)


@api_view(["POST"])
def drsreportupdate(request, pk):
    task = Drs.objects.get(id=pk)
    serializer = DrsModelSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def drsreportselete(request, pk):
    task = Drs.objects.get(id=pk)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
