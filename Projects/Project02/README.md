Part 1
1. VPC [ proof ](/Projects/Project02/Images/VPCCreated.PNG)
 - A private virtual cloud. 
2. Subnet [ proof ](/Projects/Project02/Images/SubnetCreated.PNG)
 - A network inside another network.
3. Gateway [ proof ](/Projects/Project02/Images/InternetGWCreated.PNG)
 - Essentially acts as a router.
4. Route Table [ proof ](/Projects/Project02/Images/RouteTableCreated.PNG)
 - A set of rules that determine where network traffic is directed.
5. Security Group [ proof ](/Projects/Project02/Images/SecurityGroupCreated.PNG)
 - Acts as a firewall


Part 2
  - I selected Amazon Linux 2 AMI (HVM) - Kernel 5.10, and the default username is ec2-user. I selected the t2.micro instance type
  - I attached instance to my VPC in the "Configure Instance Details" tab
  - I will not be auto-assigning a public ipv4 address since we need to create an elastic one anyway. One less thing to worry about, it's dedicated to my instance.
  - I changed the default storage to 16gb and I added another 8gb using "add new volume." 
  - Under the "Add Tags" tab, I added the "Ramsey-Instance" tag.
  - Under the "Configure Security Group" tab, I selected "Select an existing security group" and chose the "	
Ramsey-sg."
  - After creating an elastic ip, I just told it to associate with the "Ramsey-Instance" as an instance not a network interface ![ proof ](/Projects/Project02/Images/FinishedInstance.PNG)
  - I used "sudo hostnamectl set-hostname Ramsey-AMI --static" to change the hostname. [ proof ](/Projects/Project02/Images/HostName.PNG)
