import boto3
ec2=boto3.resource("ec2")
import subprocess
cmd=['python','instance_ip.py']
subprocess.Popen(cmd).wait()

print ""

userinput=raw_input("Please write What you want to do with instances stop or start: ")
print ""
print "********Select instance ID's from above list********"
print ""
if userinput == 'start':
    inid=raw_input("Enter instance ID which you want to start: ")
    inst=ec2.Instance(inid)
    rep=inst.start()
    print "Starting Instance !!!....."
    inst.wait_until_running()
    for i in ec2.instances.all():
        if i.id==inid:
            print "Server ",i.tags[0]['Value'],"is ",i.state['Name']


else:
    inid=raw_input("Enter instance ID which you want to stop: ")
    inst=ec2.Instance(inid)
    rep=inst.stop()
    print "Stopping instance !!! ......"
    inst.wait_until_stopped()
    for i in ec2.instances.all():
        if i.id==inid:
            print "Server ",i.tags[0]['Value'],"is ",i.state['Name']

