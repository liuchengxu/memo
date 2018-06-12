#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os

from util import unlock_default_wallet

parser = argparse.ArgumentParser()

parser.add_argument(
    '-u',
    '--url',
    dest='url',
    action='store',
    default='http://localhost:8888',
    help='the http/https URL where nodeos is running')

parser.add_argument(
    '--cleos',
    dest='cleos',
    action='store',
    default='cleos',
    help='where is cleos')

args = parser.parse_args()

url = args.url
cleos = os.path.expanduser(args.cleos)

cleos = [cleos, '--url', url]


def transfer_test():
    unlock_default_wallet()
    from transfer import get_account_available, transfer
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


transfer_test()
