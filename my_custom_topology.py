from mininet.topo import Topo

class CustomTreeTopo(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # Add switches
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')

        # Add hosts
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        host4 = self.addHost('h4')
        host5 = self.addHost('h5')
        host6 = self.addHost('h6')

        # Add links between switches (tree backbone)
        self.addLink(switch1, switch2)
        self.addLink(switch1, switch3)

        # Add links between switches and hosts
        self.addLink(switch2, host1)
        self.addLink(switch2, host2)
        self.addLink(switch2, host3)
        self.addLink(switch3, host4)
        self.addLink(switch3, host5)
        self.addLink(switch3, host6)

# Register the topology
topos = {'custom_tree_topo': CustomTreeTopo}
