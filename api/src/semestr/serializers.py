from rest_framework import serializers

from .models import Semester, Class, Requirement

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ('id', 'text', 'done')


class ClassSerializer(serializers.ModelSerializer):
    requirements = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = ('id', 'name', 'requirements')

    def get_requirements(self, instance):
        reqs = instance.requirements.all().order_by('-id')
        return RequirementSerializer(reqs, many=True).data


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ('id', 'number')


class SemesterDetailSerializer(serializers.ModelSerializer):
    classes = ClassSerializer(many=True)
    
    class Meta:
        model = Semester
        fields = ('id', 'number', 'classes')
        