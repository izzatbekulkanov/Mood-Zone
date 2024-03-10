from rest_framework import serializers
from .models import University, Specialty, Curriculum


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['name', 'code']

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ['name', 'code']

class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = ['name', 'codeID']

class GroupUniverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = ['name', 'codeID']