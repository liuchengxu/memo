#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging

from util import get_table, push_action, unlock_default_wallet


# return: string 0.0000
def get_account_available(account):
    out_bytes = get_table(['eosio', 'accounts', '-k', account])
    rows = json.loads(out_bytes)['rows']
    try:
        available = rows[0]['available'].replace(' EOS', '')
        return available
    except Exception:
        logging.error('account: ' + str(rows) + ' does not exist')


#  amount: string 12.0000
def transfer(sender, receiver, amount):
    generate_data = lambda sender, receiver, amount, memo="memo": {
        'from': sender,
        'to': receiver,
        'quantity': amount + ' EOS',
        'memo': memo
    }
    data = generate_data(sender, receiver, amount)
    out_bytes = push_action(['transfer', json.dumps(data), '-p', data['from']])
    return out_bytes


def tests():
    #  normal transfer
    #  biosbpa.available - 1 - 0.1, xlc.available + 1
    before = [get_account_available('biosbpa'), get_account_available('xlc')]
    out_bytes = transfer('biosbpa', 'xlc', '1.0000')
    assert b'executed transaction' in out_bytes
    after = [get_account_available('biosbpa'), get_account_available('xlc')]
    print('biosbpa ==> xlc 1.0000 EOS')
    print('before: ' + str(before))
    print('after: ' + str(after))

    #  tranfer to a non-exist account
    out_bytes = transfer('biosbpa', 'doesnotexist', '10.0000')
    print('transfer to a non-exist account')
    assert b'account is not found' in out_bytes

    #  invalid quantity
    out_bytes = transfer('biosbpa', 'xlc', '1.00001')
    print('invalid quantity 1.00001 EOS')
    assert b'only support EOS' in out_bytes


def main():
    unlock_default_wallet()
    tests()


main()
