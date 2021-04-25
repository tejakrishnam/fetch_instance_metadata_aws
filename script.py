from ec2_metadata import ec2_metadata

# Function to print the meta data for the key provided
def retrieve_metadata(data_key):
    print("Meta data for the key provided is")
    print(getattr(ec2_metadata, data_key))

data_key = raw_input("Provide the key to be fetched from instance metadata: ")
print("The key provided by the user is ", data_key)
retrieve_metadata(data_key)