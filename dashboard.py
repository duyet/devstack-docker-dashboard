from django.utils.translation import ugettext_lazy as _

import horizon


class DockerDashboard(horizon.Dashboard):
   name = _("Docker Dashboard")
   slug = "docker"
   panels = (DockerDashboardGroup)           # Add your panels here.
   default_panel = 'monitor'    # Specify the slug of the dashboard's default panel.


class DockerDashboardGroup(horizon.PanelGroup):
    slug = "dockergroup"
    name = _("Docker")
    panels = ('monitor',)

horizon.register(DockerDashboard)