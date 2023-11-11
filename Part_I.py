# !/usr/bin/python
import sys
sys.path.append('/usr/bin/mn')  # Replace with the actual path to your Mininet installation

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.node import Controller


class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()


class NetworkTopo(Topo):
    def build(self, **_opts):
        r1 = self.addHost('r1', cls=LinuxRouter, ip='10.0.1.1/24')
        r2 = self.addHost('r2', cls=LinuxRouter, ip='10.0.2.1/24')
        r3 = self.addHost('r3', cls=LinuxRouter, ip='10.0.3.1/24')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        self.addLink(s1,
                     r1,
                     params2={'ip': '10.0.1.1/24'})

        self.addLink(s2,
                     r2,
                     params2={'ip': '10.0.2.1/24'})
                     
        self.addLink(s3,
                     r3,
                     params2={'ip': '10.0.3.1/24'})
        

        self.addLink(r1,
                     r2,
                     params1={'ip': '10.100.1.1/24'},
                     params2={'ip': '10.100.1.2/24'})

        self.addLink(r2,
                     r3,
                     params1={'ip': '10.100.2.1/24'},
                     params2={'ip': '10.100.2.2/24'})

        self.addLink(r3,
                     r1,
                     params1={'ip': '10.100.3.1/24'},
                     params2={'ip': '10.100.3.2/24'})

        h1 = self.addHost(name='h1',
                          ip='10.0.1.251/24',
                          defaultRoute='via 10.0.1.1')
        h2 = self.addHost(name='h2',
                          ip='10.0.1.252/24',
                          defaultRoute='via 10.0.1.1')
        h3 = self.addHost(name='h3',
                          ip='10.0.2.251/24',
                          defaultRoute='via 10.0.2.1')
        h4 = self.addHost(name='h4',
                          ip='10.0.2.252/24',
                          defaultRoute='via 10.0.2.1')
        h5 = self.addHost(name='h5',
                          ip='10.0.3.251/24',
                          defaultRoute='via 10.0.3.1')
        h6 = self.addHost(name='h6',
                          ip='10.0.3.252/24',
                          defaultRoute='via 10.0.3.1')
                          
                          
        self.addLink(h1,s1)
        self.addLink(h2,s1)
        self.addLink(h3,s2)
        self.addLink(h4,s2)
        self.addLink(h5,s3)
        self.addLink(h6,s3)


def run():
    topo = NetworkTopo()
    net = Mininet(topo=topo)

    info(net['r1'].cmd("ip route add 10.0.2.0/24 via 10.100.1.2"))
    info(net['r1'].cmd("ip route add 10.0.3.0/24 via 10.100.3.1")) #To change route from r1 to r3 so it goes through r2, comment this line and uncomment next
    #info(net['r1'].cmd("ip route add 10.0.3.0/24 via 10.100.1.2"))
    
    info(net['r2'].cmd("ip route add 10.0.1.0/24 via 10.100.1.1"))
    info(net['r2'].cmd("ip route add 10.0.3.0/24 via 10.100.2.2"))
    info(net['r3'].cmd("ip route add 10.0.1.0/24 via 10.100.3.2"))
    info(net['r3'].cmd("ip route add 10.0.2.0/24 via 10.100.2.1"))
    info(net['r1'].cmd("ip route show"))     # this and the next two lines generate the routing table
    info(net['r2'].cmd("ip route show"))
    info(net['r3'].cmd("ip route show"))
    
    net.start()
    #racap = net['r1'].popen('tcpdump -i any -w r1.pcap')     #uncomment these to generate pcap file for ra router
    #net.pingAll()
    
    CLI(net)
    #net['r1'].cmd("kill %tcpdump")
    net.stop()
    

if __name__ == '__main__':
    setLogLevel('info')
    run()
