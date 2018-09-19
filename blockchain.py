blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_ammount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_ammount])


tx_ammount=float(input('Your transaction ammount plesase: '))
add_value(tx_ammount) # transaksi pertama  

tx_ammount=float(input('Your transaction ammount plesase: '))
# transaksi sebelumnya , transaksi sekarang
add_value(last_transaction=get_last_blockchain_value(), transaction_ammount=tx_ammount) 

tx_ammount=float(input('Your transaction ammount plesase: '))
add_value(tx_ammount, get_last_blockchain_value()) 

print(blockchain)