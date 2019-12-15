import boto3

session = boto3.Session(profile_name='pythonAutomation')

# s3=session.resource('s3')

# for bucket in s3.buckets.all():
#     print(bucket)

# new_bucket=s3.create_bucket(Bucket='automatingawsmayank-boto3', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})    

ec2_client = session.client('ec2')
# ec2_client