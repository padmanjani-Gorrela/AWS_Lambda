import boto3

s3 = boto3.client('s3')
BUCKET_NAME = "projectanjani"  

def lambda_handler(event, context):
    # Get filename from pathParameters, default to 'index' if not provided
    filename = event.get('pathParameters', {}).get('filename', 'index')
     
    # Ensure it ends with .html
    if not filename.endswith(".html"):
        filename += ".html"

    try:
        # Fetch the object from S3
        obj = s3.get_object(Bucket=BUCKET_NAME, Key=filename)
        file_content = obj['Body'].read().decode('utf-8')
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': file_content
        }
    
    except s3.exceptions.NoSuchKey:
        return {
            'statusCode': 404,
            'body': f"File not found: {filename}"
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
