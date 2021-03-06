from django.conf.urls import patterns

urlpatterns = patterns('crits.certificates.views',
    (r'^details/(?P<md5>\w+)/$', 'certificate_details'),
    (r'^set_description/(?P<md5>\w+)/$', 'set_certificate_description'),
    (r'^upload/$', 'upload_certificate'),
    (r'^remove/(?P<md5>[\S ]+)$', 'remove_certificate'),
    (r'^list/$', 'certificates_listing'),
    (r'^list/(?P<option>\S+)/$', 'certificates_listing'),
)
