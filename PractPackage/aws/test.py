import boto3
import json

athena = boto3.client('athena')


def execute_query():
    response = athena.start_query_execution(
        QueryString='SELECT * FROM elb_logs limit 10;',
        QueryExecutionContext={
            'Database': 'sampledb'
        },
        ResultConfiguration={
            'OutputLocation': 's3://aw-tester-junk/athena_output/'
        }
    )
    print(response)
    # return response


def get_query_result(query_execution_d):
    response = athena.get_query_results(
        QueryExecutionId=query_execution_d,
        MaxResults=20
    )
    print(json.dumps(response, indent=4))
    return response


execute_query()
# get_query_result('c35d1692-8f49-49cf-822c-3b759dbb56b4')
