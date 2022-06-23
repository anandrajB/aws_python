import boto3 as bt

new_name = bt.resource('sqs')
queue = new_name.get_sqs_name('username')
