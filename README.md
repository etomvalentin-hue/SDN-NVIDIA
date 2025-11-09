************** NVIDIA - Ansible Documentation**************
  - **NVIDIA Documentation** : https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-44/Network-Virtualization/
  - **Fabricplane EVPN Introduction**  :  https://www.fabricplane.com/evpn/
  - **Ansible collection** https://galaxy.ansible.com/ui/repo/published/nvidia/nvue/docs/
    

************** Topology Clos Leaf and Spine -BGP Unnumbered **************

	- **2 Spines (SP)** : 
		  SP10 : L0 10.0.0.1/32 - bgp 65000 /   Interface SWp1(LEAF10): /  Interface SWp2(LEAF11):   /  Interface SWp3(LEAF20):  /   InterfaceSWp4(LEAF21):     /  Interface SWp5(BLEAF10):  /   Interface SWp6(BLEAF11): 
		  SP11 : L0 10.0.0.2/32 - bgp 65000 /   InterfaceSWp1(LEAF10):  / Interface  SWp2(LEAF11):   /  Interface SWp3(LEAF20):  /   Interface  SWp4(LEAF21):   /  Interface SWp5(BLEAF10):  /   Interface SWp6(BLEAF11):
		

	- **2 Border Leaf (BLEAF)** : 
		  BLEAF10 : L0 10.0.0.101/32 - bgp 65201 /   Interface SWp1(SP10): / Interface SWp2(SP11):    /   Interface SWp3(Rter):169.254.127.1/31   /   Interface SWp4(FW):169.254.254.1/31  
		  BLEAF11 : L0 10.0.0.102/32 - bgp 65202 /   Interface SWp1(SP10): /  Interface SWp2(SP11):   /   Interface SWp3(Rter):169.254.127.3/31  /    Interface SWp4(FW):169.254.254.3/31   	

	- **4 LEAF ** : 
		  LEAF10 : L0(BGP) 10.0.0.11/32  -- L0(TUNNEL EVPN) 10.0.127.11/32		/   Interface SWp1(SP10):    /   Interface SWp2(SP11):    /bgp 65101  / adresse IP MLAG 169.254.1.1 /MAC : 44:39:39:40:94
		  LEAF11 : L0(BGP) 10.0.0.12/32  -- L0(TUNNEL EVPN) 10.0.127.12/32		/   Interface SWp1(SP10):    /   Interface SWp2(SP11):    /bgp 65102  / adresse IP MLAG 169.254.1.2 /MAC : 44:39:39:40:95
		  LEAF20 : L0(BGP) 10.0.0.13/32  -- L0(TUNNEL EVPN) 10.0.127.13/32		/   Interface SWp1(SP10):    /   Interface SWp2(SP11):    /bgp 65103  / adresse IP MLAG 169.254.1.5 /MAC : 44:39:39:40:96
		  LEAF21 : L0(BGP) 10.0.0.14/32  -- L0(TUNNEL EVPN) 10.0.127.14/32		/   Interface SWp1(SP10):    /   Interface SWp2(SP11):    /bgp 65104  / adresse IP MLAG 169.254.1.6 /MAC : 44:39:39:40:97 

NB : la MAC sys , format reconnaissable 44:38:39:00:00:XY

                            +-------------+
                            |  External   |
                            |   Network   |
                            +-------------+
                                  |  |
                            +------------+
                            |   Router   |
                            +------------+
                                  |  |
                    +---------------------------+
                    |                           |
              +----------+                 +----------+
              | BLEAF10  |                 | BLEAF11  |
              +----------+                 +----------+
                    |                           |
                    +-------------+-------------+
                                  |
                    +---------------------------+
                    |                           |
              +----------+                 +----------+
              |  SP10    |                 |  SP11    |
              +----------+                 +----------+
                    |                           |
		    +---------------+---------------+---------------+
		    |               |               |               |              
		+---------+     +---------+     +---------+     +---------+    
		| LEAF10  |    | LEAF11  |     | LEAF20  |      | LEAF21  |     
		+---------+     +---------+     +---------+     +---------+   
		    |               |               |               |        
		+---------+     +---------+     +---------+     +---------+   
		|  VLANs  |     |  VLANs  |     |  VLANs  |     |  VLANs  |    
		+---------+     +---------+     +---------+     +---------+    



************** Paremetre VXLAN - EVPN **************

  - VLAN 12 / L2VNI 10012 (VXLAN) / 172.16.12.0 / MTU 9164
  - VLAN 13 / L2VNI 10013 (VXLAN)/ 172.16.13.0 / MTU 9164
  - VRF EVPN-VRF / L3VNI  VXLAN 4001 

************** Routage BGP **************
	
	BGP Timer 2 9 secondes
	Advertisement : 0 secondes
	Router-id : Loopback0 (L0)
	peer-group name : LEAF-BL
  
**************activer daemons bgp **************
sudo nano /etc/frr/daemons 

bgpd=yes
zebra_options="  -M cumulus_mlag -M snmp -A 127.0.0.1 -s 90000000"
bgpd_options="   -M snmp -A 127.0.0.1"
ospfd_options="  -M snmp -A 127.0.0.1"
vtysh_enable=yes
