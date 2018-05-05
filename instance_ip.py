import boto3
ec2=boto3.resource("ec2")
print "Name\t\tStatus\t\tInstance_ID\t\t\tPublic_IP\t\tPrivate_IP"
print "----\t\t------\t\t-----------\t\t\t---------\t\t----------"
for i in ec2.instances.all():
    pip=i.public_ip_address
    if pip  != 'None' and len(i.tags[0]['Value'])<=6:
        print i.tags[0]['Value'],"\t\t",i.state['Name'],"\t", i.id,"\t\t", i.public_ip_address,"\t\t", i.private_ip_address
    else:
        print i.tags[0]['Value'],"\t",i.state['Name'],"\t", i.id,"\t\t", i.public_ip_address,"\t\t\t", i.private_ip_address
