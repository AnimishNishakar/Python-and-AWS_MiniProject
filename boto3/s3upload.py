import boto3
s3 = boto3.resource('s3')
s3.meta.client.upload_file(r"/Users/animishnishakar/VS code/boto3/s3upload.py" , 's3upload-aniii', 'hello.txt')