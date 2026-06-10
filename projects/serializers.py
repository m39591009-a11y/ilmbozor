from rest_framework import serializers
from .models import Project, Category, Application

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    category_name = serializers.CharField(source='category.name_tj', read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'category', 'category_name',
                  'author', 'author_name', 'price', 'status', 'ai_business_plan', 'created_at')
        read_only_fields = ('author', 'ai_business_plan')

class ApplicationSerializer(serializers.ModelSerializer):
    investor_name = serializers.CharField(source='investor.username', read_only=True)
    project_title = serializers.CharField(source='project.title', read_only=True)

    class Meta:
        model = Application
        fields = ('id', 'project', 'project_title', 'investor',
                  'investor_name', 'message', 'status', 'created_at')
        read_only_fields = ('investor', 'status')