# aws_connect
Establishing automated connection using python to AWS in windows env. when MFA is enabled. Reduce the manual process for connecting to AWS from ~10 min to ~30 sec.

Assuming there's a use-case that the AWS should be accessed only through a Windows env. and only default python modules such as OS module is only available.

USAGE:

Fill in the credentials such as user_name, access_key_id, access_secret_key etc. in the json file "aws_credentials.json". (one time)

Execute the script "python aws_connect_mfa.py", the script will parse the json values into a dictionary and store it. 

After the script is exeecuted the script will ask for the MFA value received in the mobile and also the session validity timeout value in seconds.

