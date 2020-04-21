import boto3
from boto3.dynamodb.conditions import Key, Attr
import json
# pip install requests
import requests


env = "test"
table_name_postfix = "Test"
old_tenant = 'old tenant name'
new_tenant = "qqqqqqqqqqqqqqqqq"
table_name = 'dynamoDbTableName'
dynamodb = boto3.resource("dynamodb", region_name='us-east-1')


# ***************** this section for AwIfmADLServiceParquetConversionHistoryTest table *******************

orgnal_output_json_file = "C:\\Users\\mlodhi\\Desktop\\IFM\\DynamoDb JSOn files\\" + env + "_" + "AwIfmADLServiceParquetConversionHistory" + table_name_postfix + ".json"
new_tenant_json = "C:\\Users\\mlodhi\\Desktop\\IFM\\DynamoDb JSOn files\\" + env + "_" + new_tenant + "_" + "AwIfmADLServiceParquetConversionHistory" + ".json"

def create_orgnal_db_json():
    AwIfmADLServiceParquetConversionHistory = dynamodb.Table(
        table_name + table_name_postfix)
    response = AwIfmADLServiceParquetConversionHistory.scan(
        FilterExpression=Attr('TenantId').eq(old_tenant)
    )
    items = response['Items']
    json_file = json.dumps(items, indent=4)
    f = open(orgnal_output_json_file, "w")
    f.write(json_file)
    f.close()


def get_path(tenant):
    root_loc_url_path = 'https://root-location.' + env + '.actimize-afcm.cloud/root-location/v1/' + tenant + '/s3/AW_IFM/1'
    return requests.get(root_loc_url_path).json()['Location']


def replace_tenant_and_io_path():
    rf = open(orgnal_output_json_file, "r")
    new_items = rf.read().replace(get_path(old_tenant), get_path(new_tenant)).replace(old_tenant, new_tenant)
    rf.close()
    wf = open(new_tenant_json, "w")
    wf.write(new_items)
    wf.close()


# create_orgnal_db_json()
# replace_tenant_and_io_path()

# ****************** END *************************


# ***************** this section for AwIfmADLServiceTenantServiceRegistrationTest table *****************

orgnal_output_f1 = "C:\\Users\\mlodhi\\Desktop\\IFM\\DynamoDb JSOn files\\" + env + "_" + "AwIfmADLServiceTenantServiceRegistration" + table_name_postfix + ".json"
new_tenant_f1 = "C:\\Users\\mlodhi\\Desktop\\IFM\\DynamoDb JSOn files\\" + env + "_" + new_tenant + "_" + "AwIfmADLServiceTenantServiceRegistration" + ".json"


def create_orgnal_db_json_m1(tenant):
    AwIfmADLServiceTenantServiceRegistration = dynamodb.Table(
        table_name + table_name_postfix)
    response = AwIfmADLServiceTenantServiceRegistration.scan(
        FilterExpression=Attr('TenantId').eq(tenant)
    )
    items = response['Items']
    # print(items)
    json_file_f1 = json.dumps(items, indent=4)
    f = open(orgnal_output_f1, "w")
    f.write(json_file_f1)
    f.close()


def replace_tenant_m1():
    rf = open(orgnal_output_f1, "r")
    new_items = rf.read().replace(old_tenant, new_tenant)
    rf.close()
    wf = open(new_tenant_f1, "w")
    wf.write(new_items)
    wf.close()


# create_orgnal_db_json_m1(old_tenant)
# replace_tenant_m1()

# ****************** END *************************


# ***************** this section for AwIfmADLServiceTenantDetailsTest table *****************

orgnal_output_f2 = "C:\\Users\\mlodhi\\Desktop\\IFM\\DynamoDb JSOn files\\" + env + "_" + "AwIfmADLServiceTenantDetails" + table_name_postfix + ".json"
new_tenant_f2 = "C:\\Users\\mlodhi\\Desktop\\IFM\\DynamoDb JSOn files\\" + env + "_" + new_tenant + "_" + "AwIfmADLServiceTenantDetails" + ".json"


def create_orgnal_db_json_m2():
    AwIfmADLServiceTenantDetails = dynamodb.Table(table_name + table_name_postfix)
    response = AwIfmADLServiceTenantDetails.scan(
        FilterExpression=Attr('TenantId').eq(old_tenant)
    )
    items = response['Items']
    json_file_f2 = json.dumps(items, indent=4)
    f = open(orgnal_output_f2, "w")
    f.write(json_file_f2)
    f.close()


def replace_tenant_m2():
    rf = open(orgnal_output_f2, "r")
    new_items = rf.read().replace(old_tenant, new_tenant)
    rf.close()
    wf = open(new_tenant_f2, "w")
    wf.write(new_items)
    wf.close()


# create_orgnal_db_json_m2()
# replace_tenant_m2()

# ****************** END *************************


# ****************** Update Table *************************

def update_db(table_name, json_file):
    table = dynamodb.Table(table_name)
    with open(json_file) as json_file:
        datatypes = json.load(json_file)
        for datatype in datatypes:
            table.put_item(
                Item=datatype
            )


# update_db("", "")

# ****************** END ************************
