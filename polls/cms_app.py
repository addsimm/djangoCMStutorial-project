
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class PollApp(CMSApp):
    name = _("PollApp")
    urls = ["polls.urls"]

apphook_pool.register(PollApp)