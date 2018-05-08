import boto3
ec2 = boto3.resource('ec2')
ec2client = boto3.client('ec2')
vpc=ec2.vpcs.all()
for i in vpc:
    print i.id, i.state, i.cidr_block, i.cidr_block_association_set[0]['CidrBlockState']['State'],i.cidr_block_association_set[0]['AssociationId']

