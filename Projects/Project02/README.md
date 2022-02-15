Part 1

Part 2
  - I selected Amazon Linux 2 AMI (HVM) - Kernel 5.10, and the default username is ec2-user. I selected the t2.micro instance type
  - I attached instance to my VPC in the "Configure Instance Details" tab
  - I will not be auto-assigning a public ipv4 address since we need to create an elastic one anyway. One less thing to worry about.
  - I changed the default storage to 16gb and I added another 8gb using "add new volume." 
  - Under the "Add Tags" tab, I added the "Ramsey-Instance" tag.
  - Under the "Configure Security Group" tab, I selected "Select an existing security group" and chose the "	
Ramsey-sg."
  - 
