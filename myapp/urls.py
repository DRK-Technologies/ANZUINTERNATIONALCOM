from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap  # Import your sitemap classes
sitemaps = {
    'static': StaticViewSitemap(),
    
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/ourstory', views.our_story, name='ourstory'),
    path('about/global-presence', views.global_presence, name='globalpresence'),
    path('about/our-team', views.out_team, name='ourteam'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('services/import-services', views.import_services, name='importservices'),
    path('services/export-services', views.export_services, name='exportservices'),
    path('services/logistics-shipping', views.logistics_shipping, name='logistics_shipping'),
    path('services/warehousing-distribution', views.warehousing_distribution, name='warehousing_distribution'),
    path('product/cashew-nuts', views.cashew, name='cashew_nuts'),
    path('product/goli-soda', views.golisoda, name='goli_soda'),
    path('product/export-pallets', views.exportpallets, name='export_pallets'),



    






]


