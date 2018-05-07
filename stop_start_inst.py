import boto3
ec2=boto3.resource("ec2")
import subprocess
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
x=0
while True and x<3:
    print ""
    userinput=raw_input("Please write What you want to do with instances stop or start: ")
    if (userinput != 'start' and userinput != 'stop'):
        print ""
        print "Caution!!!! ***Please Enter valid inputs***"
        print "For Example start or stop"
    elif userinput == 'start':
        start();
        break
    else:
        stop();
        break
    x=x+1
    print ""
    print x,"Attempts Failed !!"
    print "Max attempts '3' only"
    
