# Problem statement   - 1

  

A three-tier architecture is a software architecture pattern where the application is broken down into three logical tiers: the presentation layer, the business logic layer and the data storage layer.

  

# Approach

  I will be desiging the infrastuture with one **VPC with 4 **subnets** with combination of private and public for various layers. 
  In addition to that there will be a bastion host and a NAT gateway for the admins to have access to the infrastructure. 
  I am also going to create a Auto scaling group across two availbality zones for fault tolerance and high availablity (Real SLA of 99.99%). 
  Below is the proposed architecture
  

# What we need?

 1. Virtual private cloud 
 2. Internet gateway
 3. 4 Subnets (2 public and 2 private in 2 Avalbility Zones)
 4. Create two Route tables (public for internet and private for the traffic through NAT Gateway)
 5. Create NAT Gateway
 6.  ELB (Internet and the Internal Load balancer)
 7. Auto Scaling group
 8. Bastion Host

# Options
Terraform , I would be using the DSC IAC tool to define these modules and build the immutable infrastructure.


