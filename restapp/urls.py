from django.conf.urls import urlfrom .views import *from .payments import views as payment_viewsurlpatterns = [    url(r'categories/$', CategoryViews.as_view(), name='categories'),    url(r'categories/top/$', CategoryTopViews.as_view(), name='top_categories'),    url(r'companies/$', CompaniesViews.as_view(), name='companies'),    url(r'companies/promoted/$', CompaniesPromotedViews.as_view(), name='companies_promoted'),    url(r'companies/promoted/related/$', CompaniesPromotedRelatedViews.as_view(), name='companies_promoted_related'),    url(r'companies/nearby/$', CompaniesNearByViews.as_view(), name='companies_nearby'),    url(r'companies/nearby/promoted/$', CompaniesPromotedNearByViews.as_view(), name='promoted_companies_nearby'),    url(r'companies/nearby/(?P<phone>[\d]+)/$', CompaniesNearByForUserViews.as_view(), name='companies_nearby_for_user'),    url(r'companies/(?P<company_id>[\d]+)/$', CompanyDetailViews.as_view(), name='company_detail'),    url(r'companies/(?P<company_id>[\d]+)/(?P<phone>[\d]+)/$', CompanyDetailForUserViews.as_view(),        name='company_detail_for_user'),    url(r'companies/(?P<company_id>[\d]+)/files/$', CompanyFilesViews.as_view(), name='company_files'),    url(r'companies/(?P<company_id>[\d]+)/reviews/$', CompanyReviewViews.as_view(), name='company_reviews'),    url(r'companies/(?P<company_id>[\d]+)/reviews/for/user/(?P<phone>[\d]+)/$',        CompanyReviewForUserViews.as_view(),        name='company_reviews_for_user'),    url(r'companies/(?P<company_id>[\d]+)/reviews/create/$', CompanyReviewCreateViews.as_view(),        name='company_review_create'),    url(r'companies/(?P<company_id>[\d]+)/reviews/(?P<review_id>[\d]+)/$', CompanyReviewRUD.as_view(),        name='company_review_rud'),    url(r'companies/(?P<company_id>[\d]+)/reviews/(?P<review_id>[\d]+)/like-dislike/$', ReviewLikeDislikeView.as_view(),        name='company_review_like_dislike'),    url(r'companies/(?P<company_id>[\d]+)/reviews/(?P<review_id>[\d]+)/like-dislike/all/$', ReviewLikeDislikeAllView.as_view(),        name='company_review_like_dislike_all'),    url(r'companies/(?P<company_id>[\d]+)/reviews/files/$', ReviewAllFilesView.as_view(),        name='company_all_review_files'),    url(r'companies/(?P<company_id>[\d]+)/reviews/(?P<review_id>[\d]+)/files/$', ReviewFilesView.as_view(),        name='company_review_files'),    url(r'companies/(?P<company_id>[\d]+)/reviews/(?P<review_id>[\d]+)/files/upload/$', ReviewFilesUploadView.as_view(),        name='company_review_files_upload'),    url(r'clients/$', ClientListView.as_view(), name='clients'),    url(r'clients/create/$', ClientCreateView.as_view(), name='client_create'),    url(r'clients/(?P<phone>[\d]+)/$', ClientRetrieveView.as_view(), name='client_detail'),    url(r'clients/(?P<phone>[\d]+)/reviews/$', ClientReviewListView.as_view(), name='client_reviews'),    url(r'clients/(?P<phone>[\d]+)/update/$', ClientUpdateView.as_view(), name='client_update'),    url(r'clients/(?P<phone>[\d]+)/password/change/$', ClientPasswordChangeView.as_view(), name='password_change'),    url(r'clients/(?P<phone>[\d]+)/avatar/$', ClientAvatarUploadView.as_view(), name='client_avatar'),    url(r'clients/(?P<phone>[\d]+)/bookmarks/$', BookmarkViews.as_view(), name='client_bookmarks'),    url(r'clients/(?P<phone>[\d]+)/bookmarks/create/$', BookmarkCreateViews.as_view(), name='client_bookmarks_create'),    url(r'clients/(?P<phone>[\d]+)/bookmarks/(?P<company_id>[\d]+)/$', BookmarkDestroyViews.as_view(),        name='client_bookmarks_destroy'),    url(r'clients/(?P<phone>[\d]+)/recently/viewed/$', ClientRecentlyViewedListView.as_view(),        name='client_recently_viewed_list'),    url(r'clients/(?P<phone>[\d]+)/recently/viewed/send/$', ClientRecentlyViewedCreateView.as_view(),        name='client_recently_viewed_send'),    url(r'clients/(?P<phone>[\d]+)/recently/viewed/(?P<company_id>[\d]+)/delete/$', ClientRecentlyViewedDeleteView.as_view(),        name='client_recently_viewed_delete'),    url(r'clients/(?P<phone>[\d]+)/recently/viewed/clear/$', ClientRecentlyViewedClearAllView.as_view(),        name='client_recently_viewed_delete'),    url(r'clients/(?P<phone>[\d]+)/notifications/$',        ClientNotificationsView.as_view(),        name='client_notifications'),    url(r'clients/(?P<phone>[\d]+)/notifications/clear/$',        ClientNotificationsClearView.as_view(),        name='client_notifications_clear'),    url(r'clients/(?P<phone>[\d]+)/notifications/(?P<notification_id>[\d]+)/update/$',        ClientNotificationsUpdateView.as_view(),        name='client_notification_update'),    url(r'payment/payme/$', payment_views.PaycomView.as_view(), name='paycom'),    url(r'payment/payme/subscribe/$', payment_views.PaycomSubscribeView.as_view(), name='paycom_subscribe')]