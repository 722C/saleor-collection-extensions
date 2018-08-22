from django.conf.urls import url

from .dashboard_views import views as dashboard_views

urlpatterns = [
    url(r'^dashboard/collection-extensions/$',
        dashboard_views.collection_extension_list,
        name='collection-extension-dashboard-list'),
    url(r'^dashboard/collection-extensions/create/$',
        dashboard_views.collection_extension_create,
        name='collection-extension-dashboard-create'),
    url(r'^dashboard/collection-extensions/(?P<pk>[0-9]+)/$',
        dashboard_views.collection_extension_details,
        name='collection-extension-dashboard-detail'),
    url(r'^dashboard/collection-extensions/(?P<pk>[0-9]+)/delete/$',
        dashboard_views.collection_extension_delete,
        name='collection-extension-dashboard-delete'),
]
