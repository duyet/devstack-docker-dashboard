from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.mydashboard import dashboard


class DockerMonitor(horizon.Panel):
    name = _("Monitor")
    slug = "monitor"


dashboard.Mydashboard.register(DockerMonitor)