from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import TCLink

class SimpleTopo( Topo ):
    "Simple topology with 1 main node connecting to 4 worker nodes."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        #host0 = self.addHost('h0', ip='10.0.1.100/24')
        #host1 = self.addHost('h1', ip='10.0.1.1/24')
        #host2 = self.addHost('h2', ip='10.0.2.1/24')
        #host3 = self.addHost('h3', ip='10.0.3.1/24')
        #host4 = self.addHost('h4', ip='10.0.4.1/24')
        
        # use switch
        s1 = self.addSwitch('s1')

        host0 = self.addHost('h0', ip='10.0.0.1/16')
        host1 = self.addHost('h1', ip='10.0.1.1/16')
        host2 = self.addHost('h2', ip='10.0.1.2/16')
        host3 = self.addHost('h3', ip='10.0.1.3/16')
        host4 = self.addHost('h4', ip='10.0.1.4/16')
        host5 = self.addHost('h5', ip='10.0.1.5/16')
        
        # Add links
        #self.addLink(host0, host1, intfName1='h0-eth0', bw=20)
        #self.addLink(host0, host2, intfName1='h0-eth1')
        #self.addLink(host0, host3, intfName1='h0-eth2')
        #self.addLink(host0, host4, intfName1='h0-eth3')
        
        self.addLink(host0, s1)
        self.addLink(s1, host1)
        self.addLink(s1, host2, bw=10)
        self.addLink(s1, host3)
        self.addLink(s1, host4)
        self.addLink(s1, host5)

def run():
    topo = SimpleTopo()
    net = Mininet( topo=topo, link=TCLink)
    net.start()
    
    #net['h0'].intf('h0-eth1').setIP('10.0.2.100', 24)
    #net['h0'].intf('h0-eth2').setIP('10.0.3.100', 24)
    #net['h0'].intf('h0-eth3').setIP('10.0.4.100', 24)
    #net['h0'].cmd('route add -net 10.0.2.1 netmask 255.255.255.0 gw 10.0.2.1 h0-eth2')
    #net['h0'].cmd('route add -net 10.0.3.1 netmask 255.255.255.0 gw 10.0.3.1 h0-eth3')
    #net['h0'].cmd('route add -net 10.0.4.1 netmask 255.255.255.0 gw 10.0.4.1 h0-eth4')
    #
    #net['h1'].cmd('route add default gw 10.0.1.100')
    #net['h2'].cmd('route add default gw 10.0.2.100')
    #net['h3'].cmd('route add default gw 10.0.3.100')
    #net['h4'].cmd('route add default gw 10.0.4.100')
    
    CLI( net )
            
if __name__ == '__main__':
    setLogLevel( 'info' )
    run()