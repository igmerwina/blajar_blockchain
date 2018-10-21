# initiate blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Return the last value of the current blockchain. """
    return blockchain[-1]  # index list paling awal


def add_value(transaction_ammount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain 
    
    Argument:
        :transaction_ammount: The ammount that should be added.
        :last_transaction: The last blockchain transaction (default[1]).
    """
    # nambahin last_trx sama tx_ammount ke bc
    blockchain.append([last_transaction, transaction_ammount])


def get_user_input():
    """ Returns the input of the user (a new transaction amount) as a float. """
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