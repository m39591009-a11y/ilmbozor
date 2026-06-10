from django.urls import path
from .views import (
    CategoryListView,
    ProjectListView,
    ProjectDetailView,
    ApplicationListView,
    generate_ai_plan
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('', ProjectListView.as_view(), name='projects'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('<int:pk>/ai/', generate_ai_plan, name='ai-plan'),
    path('applications/', ApplicationListView.as_view(), name='applications'),
]