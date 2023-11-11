Team members:
Meet Hariyani (21110072)
Divyanshu Borana (21110059)

How to run:

Part I:
step 1- Install Mininet:
Open a terminal and install Mininet using the following commands
"sudo apt-get update
sudo apt-get install mininet"

step 2:Download the provided Python script:
Copy and paste the provided Python script into a file named Part_I.py, using a text editor or download it from your source.

step 3:Navigate to the directory:
Open a terminal and navigate to the directory where the Python script is located, using the "cd" command.

step 4:Run the script:
Execute the script using the following command "sudo python Part_I.py"

step 5:Interact with the Mininet CLI:
Once the script has run successfully, it will launch the Mininet CLI. You'll see the Mininet command prompt (mininet>).

step 6:Capture Wireshark:
Open a new terminal and launch Wireshark to capture packets on one of the routers. For example, to capture packets on r1, run
"sudo wireshark -i any -k -f 'host 10.0.1.1'"
This command opens Wireshark, captures packets on all interfaces (-i any), and filters packets only from host 10.0.1.1.

step 7:Check connectivity:
Within the Mininet CLI, you can check if the hosts can communicate with each other using the command "pingall"

step 8:Test different routes and measure latency:
You can modify the routing tables within the Mininet CLI to change the route. For instance, you can modify the script to uncomment the line no.95 i.e
"info(net['r1'].cmd("ip route add 10.0.3.0/24 via 10.100.1.2"))" 
and comment the line no.94 i.e.
"info(net['r1'].cmd("ip route add 10.0.3.0/24 via 10.100.3.1"))"
Then, run the Mininet CLI and check the latency using ping or iperf.

Step 9:Dump routing tables:
To dump the routing tables from the Mininet CLI, use the following commands:
"mininet> r1 route -n
 mininet> r2 route -n
 mininet> r3 route -n "

Step 10:Exit Mininet:
Once you are done, you can exit the Mininet CLI by command "mininet> exit"





Part II:
step 1- Install Mininet:
Open a terminal and install Mininet using the following commands
"sudo apt-get update
sudo apt-get install mininet"

step 2:Download the provided Python script:
Copy and paste the provided Python script into a file named Part_I.py, using a text editor or download it from your source.

step 3:Navigate to the directory:
Open a terminal and navigate to the directory where the Python script is located, using the "cd" command.

step 4:Run the script:
Execute the script using the following command "sudo python Part_II.py --config=b --congestion-control=Reno"
This command will run the Mininet topology with the specified configuration (b) and default congestion control (Reno).

step 5:Analyze throughput with Wireshark:
While the script is running, open Wireshark in another terminal to capture packets on the H4 system using the command
"sudo wireshark -i any -k -f 'host [IP_of_H4]'" Replace [IP_of_H4] with the actual IP address of H4.

step 6:Modify configuration:
You can try modifying the configuration by changing the --config and --congestion-control parameters in the command. 
For example, to run configuration (c) with BBR congestion control with "sudo python Part_II.py --config=c --congestion-control=BBR"

step 7:Run different configurations:
Repeat steps 4-6 for configurations (c) and (d) by changing the --config parameter accordingly.

step 8:Configure link loss:
If you want to test link loss, modify the --link_loss parameter. For example, you can set link loss to 1% with 
"sudo python Part_II.py --config=b --congestion-control=Reno --link_loss=1.0"

step 9:Analyze and compare throughput:
Observe the throughput over time in Wireshark for each configuration and congestion control scheme. Compare the results based on your analysis.

step 10:Exit Mininet:
Once you are done, you can exit the Mininet CLI by command "mininet> exit"








**follow the comments in the code** to run the file