import boto3

# Create IAM client
iam = boto3.client('iam')

# Update a user name
iam.update_user(
    UserName='Zoro',
    NewUserName='Luffy'
)



#Documentation : https://docs.aws.amazon.com/boto3/latest/guide/iam-example-managing-users.html