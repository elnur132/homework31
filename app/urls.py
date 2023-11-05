from django.urls import path
from .views import CreateProgrammer, CreateJuniorProgrammer, List

urlpatterns = [
    path('', List.as_view(), name='list'),
    path('programmers/', CreateProgrammer.as_view(), name='programmers'),
    path('juniors', CreateJuniorProgrammer.as_view(), name='juniors')
]
