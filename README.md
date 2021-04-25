# fetch_instance_metadata
Assuming your logged in to a VM (ec2 instance),

# Pre-requisites
- python 3.x - which comes by default in ec2 instances
- ec2-metadata module 

* Command to install ec2-metadata(if not installed): 
- python -m pip install ec2-metadata

# Steps to run :
Execute the python file :
- python script.py
# Input :
- Meta data key, For eg : region, instance_id ,etc.,
# Output :
- Meta data value for the key provided, For eg : us-east-2
2)It prompts for a key to fetch the meta data value, provide it 
- For eg : region, instance_id ,etc.,

# Note:
Run this command to see the instance meta data in json format :
curl http://169.254.169.254/latest/meta-data/

Use this as a reference to provide input for the python script.

