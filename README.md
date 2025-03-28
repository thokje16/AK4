# SW1 | CISCO 3650
	### VLAN1 
		172.16.0.4 

	## GigabitEthernet1/0/1 -> R1_STUD2
		trunk
	## GigabitEthernet1/0/2 -> R2_STUD2
		trunk
	
# R1_STUD1 | CISCO 4221

	gig0/0/0 | SW1_STUD2
		172.16.0.2/24
	gig 0/0/1 -> SW2_STUD2
		trunk

	gig 0/0/1.20
		10.10.20.2/24
		
	gig 0/0/1.99
		10.10.99.12/24

	HSRP
		prio 110
		preempt
		standby 1 ip 172.16.0.1
		standby 2 ip 10.10.20.1
		standby 3 ip 10.10.99.1

	DHCP
		pool STUD2
		10.10.20.1-255
		excluded 10.10.20.1 10.10.20.99
		excluded 10.10.20.150 10.10.20.255


R2_STUD2 | CISCO 4221
	gig0/0/0 -> SW1_STUD2
		172.16.0.3/24

	gig0/0/1 -> SW2_STUD2
		trunk
	
	gig0/1.20
		10.10.20.3/24
	gig 0/1.99
		10.10.99.13/24
	HSRP
		prio 101
		standby 1 ip 172.16.0.1
		standby 2 ip 10.10.20.1
		standby 3 ip 10.10.99.1

	DHCP
		pool STUD2
		10.10.20.1-255
		excluded 10.10.20.1 10.10.20.149
		excluded 10.10.20.201 10.10.20.255

SW2 | CISCO 3650

	VLAN 99
		10.10.99.201 255.255.255.0
	gig1/0/1 -> R1_STUD2
		trunk

	gig1/0/2 -> R2_STUD2
		Trunk

SW3 | CISCO 2960

	VLAN99
		10.10.99.202 255.255.255.0

	fa0/1 -> SW2_STUD2
		TRUNK 

	fa0/2-3 -> S3_STUD1
	ETHERCHANNEL group 1

	fa0/4-12
		ACCESS VLAN 20 

	fa0/13-24
		ACCESS VLAN 10
