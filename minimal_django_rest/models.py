from django.db import models


class SampleModel(models.Model):
    name = models.CharField(max_length=20)
    fieldA = models.TextField()
    fieldB = models.IntegerField()
    fieldC = models.EmailField()
    createdBy = models.DateTimeField(auto_now_add=True)
    updatedBy = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
