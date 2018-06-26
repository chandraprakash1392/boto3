#!/usr/bin/env python

import boto3
import time
session = boto3.Session()

ec2 = session.resource('ec2')
instances = ec2.instances.filter(
             Filters =[{'Name': 'instance-state-name', 'Values': ['running','stopped']}])

for i in instances:
    print(i.id, i.instance_type, i.vpc.id, i.subnet.id, i.state[u'Name'], i.tags[0][u'Key'], i.tags[0][u'Value'])
    if (i.state[u'Name'] == "running"): 
       status = ec2.instances.filter(InstanceIds=[i.id]).stop()
       print(i.id,i.state[u'Name'])
