from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Project, Category, Application
from .serializers import ProjectSerializer, CategorySerializer, ApplicationSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)

class ProjectListView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Project.objects.filter(status='active')
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Project.objects.all()

class ApplicationListView(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Application.objects.filter(investor=self.request.user)

    def perform_create(self, serializer):
        serializer.save(investor=self.request.user)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def generate_ai_plan(request, pk):
    try:
        project = Project.objects.get(pk=pk, author=request.user)
    except Project.DoesNotExist:
        return Response({'error': 'Лоиҳа ёфт нашуд'}, status=404)

    plan = f"""Бозори ҳадаф: Ширкатҳои обрасонӣ ва мақомоти маҳаллии Тоҷикистон
Арзиши бозор: $2.3M (Осиёи Марказӣ)
Рақибон: Технологияҳои ворид аз Туркия ва Россия
Даромади тахминӣ: 180,000–220,000 сомонӣ дар сол
Тавсия: Бо ширкатҳои коммунали шаҳр гуфтугӯ оғоз кунед"""

    project.ai_business_plan = plan
    project.save()

    return Response({'ai_business_plan': project.ai_business_plan})