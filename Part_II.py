import argparse
import socket
import time
from mininet.log import info

def tcp_server(network):
    h4 = network.get('h4')
    network['h4'].cmd("iperf -s &")

def tcp_client(network, client, congestion_control):
    command = f"iperf -c {network.get('h4').IP()} -t 10 -i 1 -Z {congestion_control} "
    info( network.get(client).cmd(command)) 

def tcp_client2(network, client, congestion_control):
    command = f"iperf -c {network.get('h4').IP()} -t 10 -i 1 -Z {congestion_control} &"
    info( network.get(client).cmd(command)) 

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import *
from mininet.cli import CLI
from mininet.log import setLogLevel

arguments = argparse.ArgumentParser()

arguments.add_argument('--config', choices=['b','c','d'], required=True)
arguments.add_argument('--congestion-control', choices=['Vegas','Reno','Cubic','BBR'], default='Reno')     #change the default choice here
arguments.add_argument('--link_loss', type=float, default=0.0)

params = arguments.parse_args()

class CustomTopology(Topo):
    def build(self):
        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Add links
        self.addLink(h1, s1, bw=100)
        self.addLink(h2, s1, bw=100)
        #self.addLink(s1,s2,bw=100)            #uncomment this line for b and c, but comment it for d
        self.addLink(h3, s2, bw=100)
        self.addLink(h4, s2, bw=100)
        self.addLink(s1, s2, loss=params.link_loss, bw=100)              #use this line only for d

def run_custom_topology():
    topo = CustomTopology()
    network = Mininet( topo = topo)
    network.start()
    
    racap = network['h4'].popen('tcpdump -i any -w h4-d3-bbr.pcap') 
    #cap = network['h4'].popen(f 'timeout 10000 tcpdump -i any -w h4.pcap')
    
    if params.config == 'b':
        tcp_server(network)
        tcp_client(network, "h1", params.congestion_control)

    elif params.config == 'c':
        tcp_server(network)
        tcp_client2(network, "h1", params.congestion_control)         #use tcp_clientt2 function for h1 and h2 while --config c and --config d, else tcp_client function
        tcp_client2(network, "h2", params.congestion_control)
        tcp_client(network, "h3", params.congestion_control)
        
    elif params.config == 'd':
    	tcp_server(network)
    	tcp_client(network, 'h1', params.congestion_control)
    
    network.pingAll()
    network.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run_custom_topology()
