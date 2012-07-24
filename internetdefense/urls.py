from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from campaigns.views import IncludeView
from include.views import CustomizeView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', CustomizeView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^include/$', IncludeView.as_view()),
    url(r'^test/modal/$',
        TemplateView.as_view(template_name="tests/modal.html"),
        name='modal',
    ),
    url(r'^test/banner/$',
        TemplateView.as_view(template_name="tests/banner.html"),
        name='banner',
    ),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^404/', TemplateView.as_view(template_name='404.html')),
        url(r'^500/', TemplateView.as_view(template_name='500.html')),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        }),
    )
urlpatterns += staticfiles_urlpatterns()
