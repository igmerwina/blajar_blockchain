# initiate empty blockchain list
genesis_block = {
    'previous_hash': '', 
    'index': 0, # index ini optional. metadata, dan bebas
    'transactions': []
}
blockchain = [genesis_block]
open_transaction = []
owner = 'Max'


def get_last_blockchain_value():
    """ Return the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]  # index list paling awal


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain 
    
    Argument:
        :sender: The sender of the coins.
        :recipient: The recipient of the Coins.
        :amount: The amount of coins sent with the transaction (default=1.0)
    """
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transaction.append(
        transaction)  # data di transaction dimasukin ke open_transaction


def mine_block():
    last_block = blockchain[-1]
    hashed_block = ''
    for key in last_block:
        value = last_block[key]
        hashed_block = hashed_block + str(value)

    block = {
        'previous_hash': hashed_block, 
        'index': len(blockchain), # index ini optional. mrupakan metadata blockchain, dan bebas isinya
        'transactions': open_transaction
    }
    blockchain.append(block)


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # input buat user masukin data ke bc
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return tx_recipient, tx_amount  # tuples


def get_user_choice():
    # Choice for if else menu
    user_input = input('Your Choice: ')
    return user_input


def print_blockchain_elements():
    # Output blockchain to the console
    for block in blockchain:
        print('Outputing Block')
        print(block)
    else:  # else dieksekusi setelah for selesai
        print('-' * 25)


def verify_chain():
    # Blockchain looping logic for verification
    is_valid = True  # helper variable buat ngecek apa bener last block ada di first block
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True  # ngecek last block apa ada di first block
        else:
            is_valid = False
            break
    return is_valid


waiting_for_input = True

# Loop the trasaction
while waiting_for_input:
    print('\nPlease Choose')
    print('1. Add a new transaction value')
    print('2. Mine a new Block')
    print('3. Output the Blockchain Blocks')
    print('h. Manipulate the chain')
    print('q. Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data  # extract tuple >> tx_data
        # add transaction amount to the blockchain
        add_transaction(recipient, amount=amount)
        print(open_transaction)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        # manipulate block
        if len(blockchain) > 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    # if not verify_chain():
    #     print_blockchain_elements()
    #     print('Invalid Blockhain')
    #     break

print('Done!')