#!/usr/bin/python3
import boto3
import sys
instname=raw_input("Give Instance Name: ")
ec2=boto3.resource("ec2")
instance=ec2.create_instances(
    ImageId = 'ami-467ca739',
    MinCount=1,
    MaxCount=1,
    KeyName='virg',
    InstanceType = "t2.micro",
   # SubnetId='subnet-ca8a8997',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': instname
                },
            ]
        },
      ],
        NetworkInterfaces=[
        {
            'AssociatePublicIpAddress': True,
            'DeleteOnTermination': True,
             'DeviceIndex': 0,
             'SubnetId':'subnet-ca8a8997'
                }

        ]
    #SecurityGroups=['vpcvirg1']
    #SecurityGroupIds=['sg-1df5ee6b']
)

print "Instance is creating !!!!!!!"
instance[0].wait_until_running()
for inst in ec2.instances.all():
    if (inst.tags[0]['Value'] == instname):
        print  inst.id, inst.instance_type, inst.public_ip_address, inst.private_ip_address


