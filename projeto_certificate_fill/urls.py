
from django.urls import path
from app_certificate_fill import views
from app_certificate_fill.views import livros_api

urlpatterns = [ #rota,view responsável, nome de refêrencia.
    path('',views.home,name='home'),
    path('livros/', views.livros,name='listagem_livros'),
    path('api/livros/', livros_api, name="livros_api")
]
