Part 1
1. VPC
 -
2. Subnet
 -
3. Gateway
 -
4. Route Table
 -
5. Security Group
 -


Part 2
  - I selected Amazon Linux 2 AMI (HVM) - Kernel 5.10, and the default username is ec2-user. I selected the t2.micro instance type
  - I attached instance to my VPC in the "Configure Instance Details" tab
  - I will not be auto-assigning a public ipv4 address since we need to create an elastic one anyway. One less thing to worry about, it's dedicated to my instance.
  - I changed the default storage to 16gb and I added another 8gb using "add new volume." 
  - Under the "Add Tags" tab, I added the "Ramsey-Instance" tag.
  - Under the "Configure Security Group" tab, I selected "Select an existing security group" and chose the "	
Ramsey-sg."
  - After creating an elastic ip, I just told it to associate with the "Ramsey-Instance" as an instance not a network interface ![ proof ](/Projects/Project02/FinishedInstance.PNG)
  - I used "sudo hostnamectl set-hostname Ramsey-AMI --static" to change the hostname. ![ proof ](/Projects/Project02/HostName.PNG)
