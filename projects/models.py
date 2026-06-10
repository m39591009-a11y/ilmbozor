from django.db import models
from accounts.models import User

class Category(models.Model):
    name_tj = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)

    def __str__(self):
        return self.name_tj

class Project(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Дар кор'),
        ('active', 'Фаъол'),
        ('sold', 'Фурӯхта шуд'),
    )
    title = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    ai_business_plan = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Дар интизор'),
        ('accepted', 'Қабул'),
        ('rejected', 'Рад'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='applications')
    investor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.investor} → {self.project}"