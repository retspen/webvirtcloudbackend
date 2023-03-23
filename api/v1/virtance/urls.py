from django.urls import re_path

from virtance.views import VirtanceListAPI, VirtanceDataAPI, VirtanceActionAPI, VirtanceConsoleAPI
from virtance.views import VirtanceMetricsCpuAPI

urlpatterns = [
    re_path(r"$", VirtanceListAPI.as_view(), name="virtance_list_api"),
    re_path(r"(?P<id>\d+)/?$", VirtanceDataAPI.as_view(), name="virtance_data_api"),
    re_path(r"(?P<id>\d+)/action/?$", VirtanceActionAPI.as_view(), name="virtance_action_api"),
    re_path(r"(?P<id>\d+)/console/?$", VirtanceConsoleAPI.as_view(), name="virtance_console_api"),
    re_path(r"(?P<id>\d+)/metrics/cpu/?$", VirtanceMetricsCpuAPI.as_view(), name="virtance_mertrics_cpu_api"),
    # re_path(r"(?P<id>\d+)/metrics/net/?$", VirtanceMetricNetAPI.as_view(), name="virtance_metrics_net_api"),
    # re_path(r"(?P<id>\d+)/metrics/disk/?$", VirtanceMetricDiskAPI.as_view(), name="virtance_metrics_disk_api"),
]
