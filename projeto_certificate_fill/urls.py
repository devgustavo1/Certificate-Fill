
from django.urls import path
from app_certificate_fill import views


urlpatterns = [ #rota,view responsável, nome de refêrencia.
    path('',views.home,name='home'),
    path('livros/', views.livros,name='listagem_livros'),
]
