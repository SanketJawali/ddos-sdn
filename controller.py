from os_ken.base import app_manager
from os_ken.controller import ofp_event
from os_ken.controller.handler import MAIN_DISPATCHER
from os_ken.controller.handler import set_ev_cls


class SimpleController(app_manager.OSKenApp):

    @set_ev_cls(
        ofp_event.EventOFPSwitchFeatures,
        MAIN_DISPATCHER
    )
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath

        self.logger.info(
            "Switch connected: datapath=%s",
            datapath.id
        )
