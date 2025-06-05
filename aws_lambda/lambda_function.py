import boto3
import pandas as pd
from io import StringIO
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def lambda_handler(event, context):
    today = datetime.utcnow().date()
    year = today.strftime('%Y')
    month = today.strftime('%m')
    day = today.strftime('%d')

    bucket = os.getenv("S3_BUCKET")
    if not bucket:
        return {"error": "S3_BUCKET not set in environment variables"}

    input_key = f"{year}/{month}/{day}/trades.csv"
    output_key = f"{year}/{month}/{day}/analysis_{today}.csv"

    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION")
    )

    try:
        csv_file = s3.get_object(Bucket=bucket, Key=input_key)['Body'].read().decode('utf-8')
        df = pd.read_csv(StringIO(csv_file))
    except Exception as e:
        return {"error": f"Failed to read input file: {input_key}", "details": str(e)}

    results = df.groupby('ticker').agg(
        total_volume=('quantity', 'sum'),
        avg_price=('price', 'mean')
    ).reset_index()

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
