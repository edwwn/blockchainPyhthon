# Initializing our blockchain List
genenis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}

blockchain = [genenis_block]
open_transactions = []
owner = 'Edu'


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):

    transaction = {
        'sender': sender,
        'recipeint': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = ''
    # last_block['previous_hash']
    for keys in last_block:
        value = last_block[keys]
        hashed_block = hashed_block + str(value)

    block = {
        'previous_hash': 'XYX',
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    """Returns the input of the user (a new transaction amount) as a float"""
    tx_recipient = input('Enter the Recipeint of  the tranasaction  ')
    tx_amount = float(input('Your Transaction Amount Please'))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input('Your Choice:  ')
    return user_input


def print_blockchain_elements():
    # Output the blockchain
    for block in blockchain:
        print('Outputing Block')
        print(block)
    else:
        print('-' * 30)


def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break

    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     elif block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print("Please Choose")
    print("1. Add new Transaction ")
    print("2. Mine new Block ")
    print("3. Output the Blockchain Blocks ")
    print("h. Manipulate the Chain ")
    print("q: To Qiut ")

    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, Please pick a value ')
    # if not verify_chain():
    #     print_blockchain_elements()
    #     print('Invalid Blockchain')
    #     break
else:
    print('User Left')

print("Done")
