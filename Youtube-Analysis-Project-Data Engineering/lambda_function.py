import awswrangler as awr
import pandas as pd
import urllib.parse
import os

s3_cleansed_layer_path = os.environ['S3_CLEANSED_LAYER_PATH']
glue_db_name = os.environ['GLUE_DB_NAME']
glue_table_name = os.environ['GLUE_TABLE_NAME']
data_write_mode = os.environ['DATA_WRITE_MODE']

def process_s3_event(event, context):
    # Extract the bucket name and object key from the event
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_object_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:
        # Read the JSON content from the S3 object into a DataFrame
        raw_df = awr.s3.read_json(f's3://{s3_bucket}/{s3_object_key}')

        # Normalize and extract required columns from the DataFrame
        normalized_df = pd.json_normalize(raw_df['items'])

        # Write the DataFrame to the cleansed S3 layer as Parquet
        write_response = awr.s3.to_parquet(
            df=normalized_df,
            path=s3_cleansed_layer_path,
            dataset=True,
            database=glue_db_name,
            table=glue_table_name,
            mode=data_write_mode
        )

        return write_response
    except Exception as error:
        print(error)
        print(f'Error processing object {s3_object_key} from bucket {s3_bucket}. Ensure the object exists and the bucket is in the correct region.')
        raise error
