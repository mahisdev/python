import boto3
ec2=boto3.resource("ec2")
import function
function.list_instances();

while True:
    print "\n 1. Create \n 2. Start \n 3. Stop \n 4. Terminate \n 5. Exit \n"
    inp=input("Choose options shown above: ")
    print ""
    if inp == 1:
        function.create();
    elif inp == 2:
        function.start();
    elif inp == 3:
        function.stop();
    elif inp == 4:
        function.terminate();
    elif inp == 5:
        function.list_instances();
        print "\n!!! Thank you !!! See you Again !!!\n"
        break
    else:
        print "!!!  Dear Customer Kindly Choose correct option  !!!!!"

    
