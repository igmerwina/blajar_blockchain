blockchain = []


def get_last_blockchain_value():
    return blockchain[-1] # index list paling awal 


def add_value(transaction_ammount, last_transaction=[1]):
    # nambahin last_trx sama tx_ammount ke bc
    blockchain.append([last_transaction, transaction_ammount])


def get_user_input():
    # input buat user masukin data ke bc
    return float(input('Your transaction ammount please: '))


tx_ammount = get_user_input()
add_value(tx_ammount)  # transaksi pertama

tx_ammount = get_user_input()
# transaksi sebelumnya , transaksi sekarang
add_value(
    last_transaction=get_last_blockchain_value(),
    transaction_ammount=tx_ammount)

tx_ammount = get_user_input()
add_value(tx_ammount, get_last_blockchain_value())

print(blockchain)