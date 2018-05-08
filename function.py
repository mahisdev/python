import boto3
ec2=boto3.resource("ec2")
import subprocess

def list_instances():
    print "\nList of Instances \n"
    cmd=['python','instance_ip.py']
    subprocess.Popen(cmd).wait()

def start():
    print "*****Copy the Instance ID from the above list*****"
    print ""
    inid=raw_input("Enter instance ID which you want to start: ")
    inst=ec2.Instance(inid)
    rep=inst.start()
    print "Starting Instance !!!....."
    inst.wait_until_running()
    for i in ec2.instances.all():
        if i.id==inid:
            print "Server ",i.tags[0]['Value'],"is ",i.state['Name']
    return

def stop():
    print "*****Copy the Instance ID from the above list*****"
    print ""
    inid=raw_input("Enter instance ID which you want to stop: ")
    inst=ec2.Instance(inid)
    rep=inst.stop()
    print "Stopping instance !!! ......"
    inst.wait_until_stopped()
    for i in ec2.instances.all():
        if i.id==inid:
            print "Server ",i.tags[0]['Value'],"is ",i.state['Name']
    return

def terminate():
    print "*****Copy the Instance ID from the above list*****"
    print ""
    inid=raw_input("Enter instance ID which you want to Terminate: ")
    inst=ec2.Instance(inid)
    rep=inst.terminate()
    print "Terminating instance !!! ......"
    inst.wait_until_terminated()
    for i in ec2.instances.all():
        if i.id==inid:
            print "Server ",i.tags[0]['Value'],"is ",i.state['Name']
    return

def create():
    instname=raw_input("Give Instance Name: ")
    instance=ec2.create_instances(
        ImageId = 'ami-467ca739',
        MinCount=1,
        MaxCount=1,
        KeyName='virg',
        InstanceType = "t2.micro",
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
    ) 
    for i in ec2.instances.all():
        if i.state['Name']=='pending':
            print "Server ",i.tags[0]['Value'],"is ",i.state['Name']
    return    
