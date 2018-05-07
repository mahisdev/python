import boto3
ec2=boto3.resource("ec2")
import function

x=0
while True and x<3:
    print ""
    userinput=raw_input("Please write What you want to do with instances create|start|stop|terminate: ")
    if (userinput != 'start' and userinput != 'stop'and userinput != 'create' and userinput != 'terminate'):
        print ""
        print "Caution!!!! ***Please Enter valid inputs***"
        print "For Example type create or start or stop or terminate "
    elif userinput == 'create':
        function.create();
        break
    elif userinput == 'start':
        function.start();
        break
    elif userinput == 'terminate':
        function.terminate();
        break
    else:
        function.stop();
        break
    x=x+1
    print ""
    print x,"Attempts Failed !!"
    print "Max attempts '3' only"
    
