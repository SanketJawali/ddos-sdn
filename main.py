from visualizer import visualize_topology
from controller import SimpleController

import subprocess

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.topo import Topo

class Topo(Topo):
    def build(self):
        s1 = self.addSwitch("s1")
        s2 = self.addSwitch("s2")

        h1 = self.addHost("h1")
        h2 = self.addHost("h2")
        h3 = self.addHost("h3")
        h4 = self.addHost("h4")

        self.addLink(h1, s1)
        self.addLink(h2, s1)

        self.addLink(h3, s2)
        self.addLink(h4, s2)

        self.addLink(s1, s2)


topo = Topo()
visualize_topology(topo)

def start_controller():
    return subprocess.Popen([
        "python3",
        "controller_runner.py",
    ])


controller_process = start_controller()

try:
    net = Mininet(
        topo=Topo(),
        controller=None
    )

    net.addController(
        "c0",
        controller=RemoteController,
        ip="127.0.0.1",
        port=6653
    )

    net.start()

    net.pingAll()

    input("Press Enter to stop...\n")

finally:
    net.stop()

    controller_process.terminate()
    controller_process.wait()
