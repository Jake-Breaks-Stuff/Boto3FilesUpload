# Boto3FilesUpload
A flask file to upload file(s) to an S3 bucket.

### Getting started
run 'pip install -r requirements.txt'

Next is installing AWS CLI to your system.

[Windows](https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html)

[MacOS](https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html)

[Linux](https://linuxhint.com/install_aws_cli_ubuntu/)

### Prerequisites

Must have an AWS account subscription. You wont be able to input an account access key + secret key, or create an S3 bucket otherwise.

### Final user specific tweaks.
Take the S3.py file, and modify the following line of code.

*s3.Bucket('**INPUT BUCKET NAME HERE**').put_object(Key=fileNames, Body=file_contents)*

If you have a specific location in the S3 bucket file structure you'd like to upload to, insert it as 'bucketname/location', otherwise replace it with the 'bucketname' you created in aws console. 

### Running the code.
Have your terminal open to the s3.py code location, and run python s3.py. 
A new window should open on local host, allowing for the input of files. 


## Authors
**Jake-Breaks-Stuff**

## Acknowledgements
**Anthony from PrettyPrinted** with his [youtube video](https://www.youtube.com/watch?v=7gqvV4tUxmY)


