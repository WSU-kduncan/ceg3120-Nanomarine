# Project 3 Rubric

11.5 / 12

## CloudFormation template submitted (1 / 1)

## Modifications required for credit (10.5 / 11)

1. description of template
2. ami replaced to AMI selected in project 2
3. VPC range to 10.0.0.0/24
4. subnet range to 10.0.0.0/28
5. resources tagged with names
6. security group setting for inbound SSH within VPC
7. security group setting for inbound SSH from home / trusted network(s) (-0.5)
   - 98.29.0.0/16 From this rule, any IP that starts with 98.29 can attempt to connect, not just the public IP you specifically use
   - you could connect because of another rule you have that opens all ports from any IP
8. security group setting for inbound SSH from WSU
9. instance setting to set "Tag" "Name" to "CF-instance"
10. instance setting to set a private IP in your subnet range
11. instance setting to change the configuration script built into the cf-template to do the following:
    - TODO: need `-y` for python3 and git in the apt install commands
    - Install git, python3, pip3
    - Change hostname
