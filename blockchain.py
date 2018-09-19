blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_ammount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_ammount])


add_value(2) 
add_value(last_transaction=get_last_blockchain_value(), transaction_ammount=0.9) 
add_value(10.89, get_last_blockchain_value()) 

print(blockchain)