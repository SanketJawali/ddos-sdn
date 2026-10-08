from visualizer import visualize_topology
from controller import Controller

from mininet.net import Mininet
from mininet.node import OVSSwitch
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

net = Mininet(
    topo=Topo(),
    switch=OVSSwitch
)

c0 = net.addController(
    "c0",
    controller=Controller,
    ip="127.0.0.1",
    port=6653
)

net.start()

net.pingAll()

net.stop()
