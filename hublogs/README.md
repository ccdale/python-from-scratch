# Writing a Hublog downloader

Things we'll need to do:
* introduce poetry
* introduce boto3
* introduce boto3 s3 client
* wrap boto3 s3 client to make usable python s3 objects
* obtain hub designator
* filter s3 data for the required hub and date range
* collect the s3 files into one tar archive
* download the tar archive to the laptop
