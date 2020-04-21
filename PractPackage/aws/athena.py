import boto3
import json

athena = boto3.client('athena')


def execute_query(query, database_name):
    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': database_name
        },
        ResultConfiguration={
            'OutputLocation': 's3://aw-tester-junk/athena_output/'
        }
    )
    print(response)
    print(type(response))
    return response['QueryExecutionId']


def get_query_result(query_execution_d):
    response = athena.get_query_results(
        QueryExecutionId=query_execution_d,
        MaxResults=20
    )
    print(json.dumps(response, indent=4))
    return response


# get_query_result('c35d1692-8f49-49cf-822c-3b759dbb56b4')
# execute_query('SELECT * FROM elb_logs limit 10;', 'sampledb')
execute_query('SHOW TABLES IN sampledb', 'sampledb')
get_query_result('c9095e36-9ae3-4b54-9b09-73002a8ec931')

