from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Exam,TimeTable

class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['about', 'contact','disclaimer']

    def location(self, item):
        return reverse(item)

class TimeTable_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return TimeTable.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated
