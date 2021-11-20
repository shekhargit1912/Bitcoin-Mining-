from hashlib import sha256
MAX_NONCE = 100000000000
def SHA256(data):
    return sha256(data.encode('ascii')).hexdigest()

def mine(block_number, transaction, previous_hash,prefix_zero):
    pref_str='0' * prefix_zero
    for nounce in range(2**256):
        text=str(block_number)+transaction+previous_hash+str(nounce)
        newHash=SHA256(text)
        if newHash.startswith(pref_str):
            print(f"Yay! Successfully mined bitcoins with nonce value:{nounce}")
            return newHash
    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")
    return newHash
    pass

if __name__ == '__main__':
    transaction = '''
    
    Rohit ->Shekhar -> 20,
    Siddhesh ->Tejas > 45
    '''
    import time
    start=time.time()
    print("start time")
    difficult=4 #leading zeros 
    newHash=mine(5,transaction,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7',difficult) #min will take transaction 
    total_time=time.time()-start
    print(f"Total time taken to mine bitcoins:{total_time}")
    print(newHash)


