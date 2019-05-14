#!/usr/bin/env python3

import json
import hashlib


def hash_function(k):
    """
    Hashes our transaction.

    Without encryption, the blockchain will be easily manipulable
    and transactions will be able to be fraudulently inserted.
    """
    if type(k) is not str:
        k = json.dumps(k, sort_keys=True)

    return hashlib.sha256(k).hexdigest()


def update_state(transaction, state):
    '''
    The ‘state’ is the record of who owns want.
    For example, I have 10 coins and I give 1 to Medium,
    then the state will be the value of the dictionary below.
    The important thing to note is that overdrafts cannot exist.
    '''
    state = state.copy()

    for key in transaction:
        if key in state.keys():
            state[key] += transaction[key]
        else:
            state[key] = transaction[key]

    return state


def valid_transaction(transaction, state):
    """
    A valid transaction must sum to 0.

    Now, we can make our block. The information from the
    previous block is read, and used to link it to the new
    block. This, too, is central to the idea of blockchain.
    Seemingly valid transactions can be attempted to
    fraudulently be inserted into the blockchain, but
    decrypting all the previous blocks is computationally
    (nearly) impossible, which preserves the integrity of
    the blockchain.
    """
    if sum(transaction.values()) is not 0:
        return False

    for key in transaction.keys():
        if key in state.keys():
            account_balance = state[key]
        else:
            account_balance = 0

        if account_balance + transaction[key] < 0:
            return False

    return True


def make_block(transactions, chain):
    """
    Make a block to go into the chain.
    """
    parent_hash = chain[-1]['hash']
    block_number = chain[-1]['contents']['block_number'] + 1

    block_contents = {
        'block_number': block_number,
        'parent_hash': parent_hash,
        'transaction_count': block_number + 1,
        'transaction': transactions
    }

    return {'hash': hash_function(block_contents),
            'contents': block_contents
            }


def check_block_hash(block):
    '''
    a small helper function to check
    the hash of the previous block:
    '''
    expected_hash = hash_function(block['contents'])

    if block['hash'] is not expected_hash:
        raise

    return


def check_block_validity(block, parent, state):
    '''
    update the blockchain
    '''
    parent_number = parent['contents']['block_number']
    parent_hash = parent['hash']
    block_number = block['contents']['block_number']

    for transaction in block['contents']['transaction']:
        if valid_transaction(transaction, state):
            state = update_state(transaction, state)
        else:
            raise

    check_block_hash(block)  # Check hash integrity

    if block_number is not parent_number + 1:
        raise

    if block['contents']['parent_hash'] is not parent_hash:
        raise

    return state


def check_chain(chain):
    """Check the chain is valid."""
    if type(chain) is str:
        try:
            chain = json.loads(chain)
            assert (type(chain) == list)
        except ValueError:
            # String passed in was not valid JSON
            return False
    elif type(chain) is not list:
        return False

    state = {}

    for transaction in chain[0]['contents']['transaction']:
        state = update_state(transaction, state)

    check_block_hash(chain[0])
    parent = chain[0]

    for block in chain[1:]:
        state = check_block_validity(block, parent, state)
        parent = block

    return state


def add_transaction_to_chain(transaction, state, chain):
    '''
    need a transaction function, which hangs
    all of the above together:
    '''
    if valid_transaction(transaction, state):
        state = update_state(transaction, state)
    else:
        raise Exception('Invalid transaction.')

    my_block = make_block(state, chain)
    chain.append(my_block)

    for transaction in chain:
        check_chain(transaction)

    return state, chain


# Genesis Block. This is the inception of our new
# coin (or stock inventory, etc). For the purposes
# of this article, I will say that I, Tom, will
# start off with 10 coins.
genesis_block = {
    'hash': hash_function({
        'block_number': 0,
        'parent_hash': None,
        'transaction_count': 1,
        'transaction': [{'Brian': 10}]
    }),
    'contents': {
        'block_number': 0,
        'parent_hash': None,
        'transaction_count': 1,
        'transaction': [{'Brian': 10}]
    },
}

block_chain = [genesis_block]
chain_state = {'Brian': 10}

# Now, look what happens when I
# give some coin to Medium:
chain_state, block_chain = \
    add_transaction_to_chain(transaction={'Brian': -1, 'Chris': 1},
                             state=chain_state,
                             chain=block_chain
                             )


