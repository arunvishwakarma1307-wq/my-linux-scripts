import boto3
from moto import mock_aws
import datetime

@mock_aws
def aws_manager():
    print("=== AWS Resource Manager ===")
    print("Date:", datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
    
    # S3 Setup
    s3 = boto3.client('s3', region_name='us-east-1')
    s3.create_bucket(Bucket='my-project-bucket')
    s3.put_object(Bucket='my-project-bucket', Key='report.txt', Body='AWS Report')
    print("\n✅ S3 Bucket bana: my-project-bucket")
    
    # EC2 Setup
    ec2 = boto3.client('ec2', region_name='us-east-1')
    instance = ec2.run_instances(
        ImageId='ami-12345678',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro'
    )
    instance_id = instance['Instances'][0]['InstanceId']
    print("✅ EC2 Server bana:", instance_id)
    
    # IAM Setup
    iam = boto3.client('iam', region_name='us-east-1')
    iam.create_user(UserName='project-user')
    print("✅ IAM User bana: project-user")
    
    # Report
    print("\n=== Final Report ===")
    print("S3 Buckets:")
    for b in s3.list_buckets()['Buckets']:
        print(" -", b['Name'])
    
    print("EC2 Instances:")
    for r in ec2.describe_instances()['Reservations']:
        for i in r['Instances']:
            print(" -", i['InstanceId'], "|", i['State']['Name'])
    
    print("IAM Users:")
    for u in iam.list_users()['Users']:
        print(" -", u['UserName'])
    
    print("\n✅ AWS Resource Manager Complete!")

aws_manager()