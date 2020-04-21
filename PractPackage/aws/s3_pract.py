import os
import boto3

s3_resource = boto3.resource("s3", region_name="us-east-1")

def upload_objects(keyObj):
    try:
        bucket_name = "my-test-us-east-1" #s3 bucket name
        root_path = 'C:\\Users\\mlodhi\\OneDrive - Nice Systems Ltd\\Desktop\\extra EDA solutions\\' # local folder for upload

        my_bucket = s3_resource.Bucket(bucket_name)

        for path, subdirs, files in os.walk(root_path):
            print("Path : ", path)
            print("subdirs : ", subdirs)

            path = path.replace("\\","/")
            # print("Path : ", path)

            for file in files:
                print("File : ", file)
                my_bucket.upload_file(os.path.join(path, file),
                                      keyObj + file,
                                      ExtraArgs={'ServerSideEncryption': 'AES256'})

    except Exception as err:
        print(err)


if __name__ == '__main__':
    print("Starting the upload...")
    s3_prefix = "EDAService/SchemaConfigFiles/"

    tenantList = ["11ea2d50-00a1-d1a0-905b-0242ac110002", "11ea2d67-4de5-0ec0-905b-0242ac110002",
                  "11ea2d67-7385-c750-9a4d-0242ac110002"]
    for tenantId in tenantList:
        print(tenantId)
        destination = s3_prefix + tenantId + "/"
        upload_objects(s3_prefix+tenantId+"/")
