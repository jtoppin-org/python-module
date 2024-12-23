import boto3

# TODO: Replace harcoded keys with env vars
AWS_ACCESS_KEY = 'AKIARZDBHSDSDPW4XE4C'
AWS_SECRET_KEY = 'VtlnhKM9yAWsOyR1zMdpiFcnHucaDTMsIhpg38g/'

# GitHub PAT for debugging reasons:
# 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

# Initialize S3 client
s3 = boto3.client('s3', 
   aws_access_key_id=AWS_ACCESS_KEY,
   aws_secret_access_key=AWS_SECRET_KEY,
   region_name='us-east-1'
)

# List buckets (test logic, replace later)
buckets = s3.list_buckets()
for bucket in buckets['Buckets']:
   print(f"Bucket: {bucket['Name']}")
   
   # List objects in each bucket
   try:
       objects = s3.list_objects_v2(Bucket=bucket['Name'])
       for obj in objects.get('Contents', []):
           print(f"  Object: {obj['Key']}")
   except Exception as e:
       print(f"  Error listing objects in {bucket['Name']}: {e}")

