import boto3
import os


def upload_file(dir_name, object_name):
    """Upload a file to an S3 bucket
        :param dir_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
    """

    session = boto3.Session(
        aws_access_key_id="",
        aws_secret_access_key="",
    )
    # Upload the file
    s3_client = session.client('s3')
    name = f"research/{object_name}"
    s3_client.upload_file(dir_name, "coinsharesresearchbucket", name)


def upload_data(base_path):

    upload_file(f"{base_path}/aggregated_outputs/authors_pivot.csv", "authors_pivot.csv")
    upload_file(f"{base_path}/aggregated_outputs/authors_roll30_pivot.csv", "authors_roll30_pivot.csv")
    upload_file(f"{base_path}/aggregated_outputs/commits_pivot.csv", "commits_pivot.csv")
