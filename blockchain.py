import functools
import hashlib as hl
import json
from collections import OrderedDict

# reward mining for miners 
MINING_REWARD = 10  # reward untuk miner

# genesis block yakni bc yg pertama kali dibuat
genesis_block = {
    'previous_hash': '',
    'index': 0,  # index ini optional. metadata, dan bebas
    'transactions': [],
    'proof': 100
}

# Initializing our (empty) blockchain list
blockchain = [genesis_block]
# Unhandled transactions
open_transactions = []
# We are the owner of the Blockchain node. Hence this is our identifier
owner = 'Max'
# A set of participant, nambah otomatis selain max
# Registered participants: Ourself + other people sending/receiving coins
participants = {'Max'}  


def hash_block(block):
    """ Hash pada Block. Renturn string representation of it 
    
    Arguments: 
        :block: The block that should be hashed
    """
    # pakai SHA256 buat bkin hash | .hexdigest --> ngubah data hash (byte) jadi string
    return hl.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest( )


def valid_proof(transactions, lats_hash, proof):
    guess = (str(transactions) + str(lats_hash) + str(proof)).encode()
    guess_hash = hl.sha256(guess).hexdigest()
    print(guess_hash)
    # kode buat ngecek bener/ngga kalau PoW nya 00 dari [0:2]
    # merupakan syarat dari while di valid_proof di bawah
    return guess_hash[0:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0 
    # ngecek apakah hash dari guess_hash uda terpenuhi
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    # ngecek nilai proof nya berapa
    return proof


def get_balance(participant):
    # get balannce sender
    # masih kurang paham sama list comprehension: tx_sender, open_tx_sender
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    # kurang paham sama lambda nya: 
    amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    
    # get balance recipient
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = functools.reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient , 0)

    # return total balance
    return amount_received - amount_sent


def get_last_blockchain_value():
    """ Return the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]  # index list paling awal


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain 
    
    Argument:
        :sender: The sender of the coins.
        :recipient: The recipient of the Coins.
        :amount: The amount of coins sent with the transaction (default=1.0)
    """
    # transaction = {
    #     'sender': sender, 
    # 'recipient': recipient, 
    # 'amount': amount
    # }
    transaction = OrderedDict(
        [('sender', sender), ('recipient', recipient), ('amount', amount)]
    )
    if verify_transaction(transaction):
        open_transactions.append(transaction)  # data di transaction dimasukin ke open_transactions
        participants.add(sender)  # add
        participants.add(recipient)
        return True
    return False


def mine_block():
    """ Create new block & add open transaction to it"""
    # Get last block of the Blockchain
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    # Calculate the PoW
    proof = proof_of_work()
    # reward_transaction = {  # reward for mining
    #     'sender': 'MINING',
    #     'recipient': owner,
    #     'amount': MINING_REWARD
    # } 
    reward_transaction = OrderedDict(
        [('sender', 'MINING'), ('recipient', owner,), ('amount', MINING_REWARD)]
    )
    copied_transactions = open_transactions[:] # copy using range selector
    copied_transactions.append(reward_transaction)  # append bakal nambah uangnya sendiri
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),  # index ini optional. mrupakan metadata blockchain, dan bebas isinya
        'transactions': copied_transactions,
        'proof': proof
    }
    blockchain.append(block)
    return True  # reset open_transactions to empty list


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
    """ Verify the current Bockchain and return True if it's valid, False if not"""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            print('Proof Of Work is Invalid')
            return False 
    return True


def verify_transactions():
    # all buat ngecek semua transaksi valid atau ngga
    # list comprehension nya ngasilin True or False Only
    return all([verify_transaction(tx) for tx in open_transactions])

waiting_for_input = True

# Loop the trasaction
while waiting_for_input:
    print('\nPlease Choose')
    print('1. Add a new transaction value')
    print('2. Mine a new Block')
    print('3. Output the Blockchain Blocks')
    print('4. Output participants')
    print('5. Check transaction validity')
    print('h. Manipulate the chain')
    print('q. Quit')

    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data  # extract tuple >> tx_data
        # add transaction amount to the blockchain
        if add_transaction(recipient, amount=amount):
            print('Added Transaction!')
        else:
            print('Transaction Failed!')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []  # reset open transaction
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('Transaction is Valid')
        else: 
            print('There are invalid transactions!')
    elif user_choice == 'h':
        # manipulate block
        if len(blockchain) > 1:
            blockchain[0] = {  # dipakai buat hack verfication
                'previous_hash':'',
                'index':0,
                'transactions': [{
                    'sender': 'Christ',
                    'recipient': 'Max',
                    'amount': 100
                }]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid Blockhain')
        break
    # string formating pake {} sama .format | soo cooooll
    print('Balance of {}: {:6.2f}'.format('Max', get_balance('Max')))
else:
    print('User left!')

print('Done!')