import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-0a097723c2c17e20a').stop()