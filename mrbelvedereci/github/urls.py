from django.conf.urls import url

from mrbelvedereci.github import views as github_views

urlpatterns = [
    url(r'^$', github_views.repo_list),
    url(r'^repo/(?P<owner>\w+)/(?P<name>[^/].*)/branch/(?P<branch>.*)$', github_views.branch_detail),
    url(r'^repo/(?P<owner>\w+)/(?P<name>[^/].*)/commit/(?P<sha>\w+)$', github_views.commit_detail),
    url(r'^repo/(?P<owner>\w+)/(?P<name>[^/].*)/*$', github_views.repo_detail),
    url(r'^webhook/github/push$', github_views.github_push_webhook),
]
