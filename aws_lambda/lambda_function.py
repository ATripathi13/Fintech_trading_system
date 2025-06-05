import boto3
import pandas as pd
from io import StringIO
from datetime import datetime

def lambda_handler(event, context):
    # Get today's date
    today = datetime.utcnow().date()
    year = today.strftime('%Y')
    month = today.strftime('%m')
    day = today.strftime('%d')
    
    # Construct S3 file paths
    bucket = 'your-bucket'
    input_key = f"{year}/{month}/{day}/trades.csv"
    output_key = f"{year}/{month}/{day}/analysis_{today}.csv"

    # Fetch the CSV from S3
    s3 = boto3.client('s3')
    try:
        csv_file = s3.get_object(Bucket=bucket, Key=input_key)['Body'].read().decode('utf-8')
        df = pd.read_csv(StringIO(csv_file))
    except Exception as e:
        return {"error": f"Failed to read input file: {input_key}", "details": str(e)}

    # Perform aggregation
    results = df.groupby('ticker').agg(
        total_volume=('quantity', 'sum'),
        avg_price=('price', 'mean')
    ).reset_index()

    # Save result to S3
    csv_buffer = StringIO()
    results.to_csv(csv_buffer, index=False)

    try:
        s3.put_object(Bucket=bucket, Key=output_key, Body=csv_buffer.getvalue())
    except Exception as e:
        return {"error": f"Failed to upload output file: {output_key}", "details": str(e)}

    return {
        "message": "Analysis saved successfully",
        "input_file": input_key,
        "output_file": output_key
    }
