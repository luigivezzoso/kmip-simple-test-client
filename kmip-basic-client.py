import time
from kmip.pie import client
from kmip import enums
from kmip.core.factories import attributes
import string
import random




def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str





start=time.time()

## OPENING SESSION WITH EXPLICIT USERNAME&PASSWORD

#kmip_client = client.ProxyKmipClient(username="kmip-client-02", password="Thales123!", config_file="config\pykmip.conf")


kmip_client = client.ProxyKmipClient(config_file="config\pykmip.conf")

with kmip_client:
    if kmip_client._is_open:
        print ("KMIP Client Session opened")

        # Create a AES 256 key
        keyname = "kmip-client-key-" + get_random_string(10)


        
        print ("---> Creating key: " +keyname )
        key_uid = kmip_client.create(
        enums.CryptographicAlgorithm.AES,
            256,
            name= keyname,
            cryptographic_usage_mask=[
                enums.CryptographicUsageMask.ENCRYPT,
                enums.CryptographicUsageMask.DECRYPT
            ]
        )
        # activate the key
        print ("--->  Acivating key: " + keyname )
        kmip_client.activate(key_uid)
        print ("--->  Rovoking key: " + keyname )
        kmip_client.revoke(enums.RevocationReasonCode.CESSATION_OF_OPERATION, key_uid )
        print ("--->  Destroing key: " + keyname )
        end=time.time()


        kmip_client.destroy(key_uid)
    else:
        print ("KMIP Session error")

kmip_client.close()
print ("KMIP Closing session")

print ("KMIP process time: " + str(end-start)+ " seconds")

