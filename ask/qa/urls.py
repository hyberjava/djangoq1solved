from django.conf.urls import url
from django.contrib import admin
import qa.views as qa

urlpatterns = [
    url(r'^$', qa.index),
    url(r'^login/$', qa.login),
    url(r'^signup/$', qa.signup),
    url(r'^question/\d+/$', qa.question),
    url(r'^ask/.*$', qa.ask),
    url(r'^popular/$', qa.popular),
    url(r'^new/$', qa.new),
    url(r'^admin/$', admin.site.urls),
]