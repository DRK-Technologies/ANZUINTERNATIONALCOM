# sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'about','ourstory','globalpresence','ourteam','contact','services','importservices','exportservices','logistics_shipping','warehousing_distribution','cashew_nuts','goli_soda','export_pallets']  # Add names of URL patterns you want in sitemap

    def location(self, item):
        return reverse(item)


