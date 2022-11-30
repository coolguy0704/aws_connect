# -*- coding: utf-8 -*-

import os
import sys
import json
import time

current_username = os.popen('echo %username%').read().rstrip()
json_user_list_file = open(r"C:\Users\{0}\.aws\aws_credentials.json" .format(current_username))
user_dictionary = json.loads(json_user_list_file.read())
json_user_list_file.close()
os.system("echo:")
os.chdir(r"C:\Users\{0}\.aws" .format(current_username))
os.system("echo:")

def func():
	for retry in range(5):
		user_input = int(input("Please Enter 1 to connect to AWS session or 2 to resume previous session: "))
		os.system("echo:")
		if user_input==1:
			#os.system(r'type C:\Users\{0}\.aws\com_credentials.txt > C:\Users\{0}\.aws\credentials' .format(current_username, current_username))
			com_username = user_dictionary['aws_info']['com_username'] #input("Please enter Com AWS username:")
			arn_name = user_dictionary['aws_info']['arn_name']
			session_target_vm = user_dictionary['aws_info']['session_target_vm']
			target_vm_region = user_dictionary['aws_info']['target_vm_region']
			session_validity = input("Please enter AWS session validity limit in seconds: ")
			token_code = input("Please enter AWS MFA token code: ")
			os.system("echo:")
			os.system(r'@echo [default] > C:\Users\{0}\.aws\user_list.json' .format(current_username))
			os.system(r'@echo [default] > C:\Users\{0}\.aws\credentials_com.txt' .format(current_username))
			os.system(r'@echo aws_access_key_id={0} >> C:\Users\{1}\.aws\user_list.json' .format(user_dictionary['aws_info']['com_aws_access_key_id'], current_username))
			os.system(r'@echo aws_access_key_id={0} >> C:\Users\{1}\.aws\credentials_com.txt' .format(user_dictionary['aws_info']['com_aws_access_key_id'], current_username))
			os.system(r'@echo aws_secret_access_key={0} >> C:\Users\{1}\.aws\user_list.json' .format(user_dictionary['aws_info']['com_aws_secret_access_key'], current_username))
			os.system(r'@echo aws_secret_access_key={0} >> C:\Users\{1}\.aws\credentials_com.txt' .format(user_dictionary['aws_info']['com_aws_secret_access_key'], current_username))
			os.system(r'type C:\Users\{0}\.aws\user_list.json > C:\Users\{1}\.aws\credentials' .format(current_username, current_username))
			print("changed username to {0}..." .format(user_dictionary['aws_info']['com_username']))
			print("Connecting to AWS...")
			os.system(r'aws sts get-session-token --serial-number {3}/{0} --duration-seconds {4} --token-code {1} >C:\Users\{2}\.aws\aws_temp_token.json' .format(com_username, token_code, current_username, arn_name, session_validity))
			json_file = open(r"C:\Users\{0}\.aws\aws_temp_token.json" .format(current_username))
			dictionary = json.loads(json_file.read())
			json_file.close()
			os.system(r'del C:\Users\{0}\.aws\aws_temp_token.json' .format(current_username))
			access_key_id = dictionary['Credentials']['AccessKeyId']
			secret_access_key = dictionary['Credentials']['SecretAccessKey']
			session_token = dictionary['Credentials']['SessionToken']
			os.system(r'@echo [mfa_rac] >> C:\Users\{0}\.aws\user_list.json' .format(current_username))
			os.system(r'@echo [mfa_rac] >> C:\Users\{0}\.aws\credentials_com.txt' .format(current_username))
			os.system(r'@echo aws_access_key_id={0} >> C:\Users\{1}\.aws\user_list.json' .format(access_key_id, current_username))
			os.system(r'@echo aws_access_key_id={0} >> C:\Users\{1}\.aws\credentials_com.txt' .format(access_key_id, current_username))
			os.system(r'@echo aws_secret_access_key={0} >> C:\Users\{1}\.aws\user_list.json' .format(secret_access_key, current_username))
			os.system(r'@echo aws_secret_access_key={0} >> C:\Users\{1}\.aws\credentials_com.txt' .format(secret_access_key, current_username))
			os.system(r'@echo aws_session_token={0} >> C:\Users\{1}\.aws\user_list.json' .format(session_token, current_username))
			os.system(r'@echo aws_session_token={0} >> C:\Users\{1}\.aws\credentials_com.txt' .format(session_token, current_username))
			os.system(r'type C:\Users\{0}\.aws\user_list.json > C:\Users\{1}\.aws\credentials' .format(current_username, current_username))
			print("MFA Credentials changed to Commercial...")
			os.system(r'del C:\Users\{0}\.aws\user_list.json' .format(current_username))
			#os.system('set "AWS_ACCESS_KEY_ID={0}"' .format(access_key_id))
			#os.system('set "AWS_SECRET_ACCESS_KEY={0}"' .format(secret_access_key))
			#os.system('set "AWS_SESSION_TOKEN={0}"' .format(session_token))
			os.system('aws ssm start-session --target {0} --profile mfa_rac --region {1} --document-name AWS-StartPortForwardingSession --parameters  "portNumber=22,localPortNumber=11122"' .format(session_target_vm, target_vm_region))

		if user_input == 2:
			try:
				print("Trying to resume AWS session...")
				os.system(r'type C:\Users\{0}\.aws\credentials_com.txt > C:\Users\{1}\.aws\credentials' .format(current_username, current_username))
				os.system('aws ssm start-session --target {0} --profile mfa_rac --region {1} --document-name AWS-StartPortForwardingSession --parameters  "portNumber=22,localPortNumber=11122"' .format(session_target_vm, target_vm_region))
			except Exception as e:
				print("Error: ",e)
				print("Cannot resume session please connect to the environment again..")

		print("Please make a valid choice and try again or ^c to exit.")
		
	else:
		print("you made 5 invalid choices so exiting.")
		#sys.exit(1)
		
def main():
	func()
	
if __name__ == '__main__': main()
