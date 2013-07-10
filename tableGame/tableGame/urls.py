from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
(r'^$', 'tableGame.hello.index'),
(r'^articles/', 'articles.views.latest_article'),
    # Examples:
    # url(r'^$', 'tableGame.views.home', name='home'),
    # url(r'^tableGame/', include('tableGame.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
