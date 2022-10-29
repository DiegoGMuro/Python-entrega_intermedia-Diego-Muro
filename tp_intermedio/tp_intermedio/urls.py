"""tp_intermedio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from credit.views import create_credit
from customer.views import create_customer
from payment.views import create_payment
from product.views import create_product 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    #path("create_credit/<int:code>/<str:description>/<int:amount>", create_credit, ),
    #path("create_customer/<int:code>/<str:name>/<str:email>/<str:segment>", create_customer, ),
    #path("create_payment/<int:code>/<str:name>/<int:days>", create_payment, ),
    #path("create_product/<int:code>/<str:description>/<int:unit_sales>", create_product, ),
    path("credit/", include("credit.urls")),
    path("customer/", include("customer.urls")),
    path("payment/", include("payment.urls")),
    path("product/", include("product.urls")),
]
