import boto3
from moto import mock_aws
import json

@mock_aws
def test_iam_policy():
    iam = boto3.client('iam')

    # User create karo
    iam.create_user(UserName='arun-developer')

    # Policy banao (sirf EC2 access)
    policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "ec2:*"
                ],
                "Resource": "*"
            }
        ]
    }

    iam.put_user_policy(
        UserName='arun-developer',
        PolicyName='EC2OnlyAccess',
        PolicyDocument=json.dumps(policy_document)
    )

    print("User bana diya: arun-developer")
    print("Permission: Sirf EC2 access")

test_iam_policy()