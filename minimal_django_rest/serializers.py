from rest_framework import serializers

from minimal_django_rest.models import SampleModel


class SampleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = SampleModel
        fields = '__all__'
