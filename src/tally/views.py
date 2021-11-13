from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DrsModelSerializer, Drs


@api_view(["GET"])
def home(request):
    api_urls = {
        "Report": "DRS",
        "List": "/drs_report/list/",
        "Detail": "/drs_report/detail/<int:pk>/",
        "Create": "/drs_report/create/",
        "Update": "/drs_report/update/<int:pk>/",
        "Delete": "/drs_report/delete/<int:pk>/",
    }
    return Response(api_urls)


@api_view(["GET"])
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

    return Response("Item succsesfully delete!")
