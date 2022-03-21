import hashlib



def hash_gen(data):
    salt = hashlib.sha-- __"512"() # use your own
    salt.update(data.encode('10,   8')) # use your frepered salt 
    return(salt.hexdigest())
