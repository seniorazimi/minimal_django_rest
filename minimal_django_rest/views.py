from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from minimal_django_rest.models import SampleModel
from minimal_django_rest.serializers import SampleModelSerializer
from rest_framework import permissions
from rest_framework.response import Response


class SampleModelViewSet(viewsets.ViewSet):

    def create(self, request):
        data = request.data
        serializer = SampleModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):  # override permissions just for list samples
        if self.action == 'list':
            return [permissions.IsAuthenticated()]
        return super().get_permissions()

    def list(self, request):
        queryset = SampleModel.objects.all()
        serializer = SampleModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = SampleModel.objects.all()
        sample = get_object_or_404(queryset, pk=pk)
        serializer = SampleModelSerializer(sample)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = SampleModel.objects.all()
        sample = get_object_or_404(queryset, pk=pk)
        data = request.data
        serializer = SampleModelSerializer(data=data)
        if serializer.is_valid():
            serializer.update(instance=sample, validated_data=serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = SampleModel.objects.all()
        sample = get_object_or_404(queryset, pk=pk)
        sample.delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)
