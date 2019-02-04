# initiate empty blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Return the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]  # index list paling awal


def add_transaction(transaction_ammount, last_transaction=[1]): # [1] = default value
    """ Append a new value as well as the last blockchain value to the blockchain 
    
    Argument:
        :transaction_ammount: The ammount that should be added.
        :last_transaction: The last blockchain transaction (default[1]).
    """
    # nambahin last_trx sama tx_ammount ke bc
    # blockchainnya di appen oleh last trasaction sama tx_ammount
    # last trasaction karena baru, jadi di isi [1] biar keisi dulu
    if last_transaction == None: 
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_ammount])
    


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # input buat user masukin data ke bc
    user_input = float(input('Your transaction ammount please: '))
    return user_input


def get_user_choice():
    # Choice for if else menu
    user_input = input('Your Choice: ')
    return user_input


def print_blockchain_elements():
    # Output blockchain to the console
    for block in blockchain:
        print('Outputing Block')
        print(block)


def verify_chain():
    # Blockchain looping logic for verification
    block_index = 0 # inisiasi index block 
    is_valid = True # helper variable buat ngecek apa bener last block ada di first block
    for block in blockchain:
        if block_index == 0: 
            block_index += 1 # kalau block_index = 0, data +1
            continue
        if block[0] == blockchain[block_index - 1]:
            is_valid = True # ngecek last block apa ada di first block
        else: 
            is_valid = False
            break
        block_index += 1
    return is_valid 


# Loop the trasaction   
while True:
    print('\nPlease Choose')
    print('1. Add a new transaction value')
    print('2. Output the Blockchain Blocks')
    print('h. Manipulate the chain')
    print('q. Quit')
    user_choice = get_user_choice()
    if user_choice == '1': 
        tx_ammount = get_transaction_value()
        add_transaction(tx_ammount, get_last_blockchain_value())
    elif user_choice == '2': 
        print_blockchain_elements()
    elif user_choice == 'h': 
        # manipulate block
        if len(blockchain) >1: 
            blockchain[0] = [2]
    elif user_choice == 'q':
        break # 'break' quit the loop  
    else: 
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print('Invalid Blockhain')
        break

print('Done!')