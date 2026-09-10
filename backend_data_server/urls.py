"""
URL configuration for backend_data_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pathlib import Path

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

BASE_DIR = Path(__file__).resolve().parent.parent


def home(request):
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Duelo de Cartas Penal</title>
    <style>
      body{
        margin:0; min-height:100vh; display:flex; align-items:center; justify-content:center;
        font-family:"Segoe UI",Arial,sans-serif; color:#eef3f9;
        background:radial-gradient(ellipse at center, #1f5c3a 0%, #0e2a1c 60%, #060f0a 100%);
      }
      .card{
        max-width:560px; width:90%; text-align:center; padding:36px 30px; border-radius:20px;
        background:linear-gradient(160deg,#20304a,#141d29); border:3px solid #e8c15c;
        box-shadow:0 20px 50px rgba(0,0,0,.6);
      }
      .card .emoji{font-size:3rem; margin-bottom:6px;}
      .card h1{margin:0 0 8px; font-size:1.6rem;}
      .card p{opacity:.85; font-size:.95rem; margin:0 0 22px;}
      .btn-play{
        display:inline-block; text-decoration:none; background:linear-gradient(160deg,#e8c15c,#c69a2e);
        color:#1a1305; border-radius:14px; padding:16px 36px; font-size:1.2rem; font-weight:bold;
        box-shadow:0 6px 16px rgba(0,0,0,.4); transition:transform .15s ease;
      }
      .btn-play:hover{transform:translateY(-3px) scale(1.03);}
      .admin-link{display:block; margin-top:18px; font-size:.8rem; opacity:.6; color:#eef3f9;}
    </style>
    </head>
    <body>
      <div class="card">
        <div class="emoji">⚖️🃏🔫</div>
        <h1>Duelo de Cartas Penal</h1>
        <p>Proceso N.° 06283-2026-00147 · Fiscalía vs. Andrés Mauricio Salazar Peña</p>
        <a class="btn-play" href="/juego/">🎮 Entrar al juego</a>
        <a class="admin-link" href="/admin/">Panel de administración</a>
      </div>
    </body>
    </html>
    """
    return HttpResponse(html)


def juego(request):
    html = (BASE_DIR / 'duelo_cartas_penal.html').read_text(encoding='utf-8')
    return HttpResponse(html)


urlpatterns = [
    path('', home, name='home'),
    path('juego/', juego, name='juego'),
    path('admin/', admin.site.urls),
]
