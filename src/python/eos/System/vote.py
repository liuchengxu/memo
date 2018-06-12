#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from util import get_table, push_action, unlock_default_wallet


#  return: [staked, unstaking], [10.0000, 0.0000]
def get_account_votes(account, bp):
    out_bytes = get_table([account, 'votes', '-k', bp])
    rows = json.loads(out_bytes)['rows']
    try:
        staked = rows[0]['staked'].replace(' EOS', '')
        unstaking = rows[0]['unstaking'].replace(' EOS', '')
        print(account + ":" + bp + ', staked: ' + staked + ',unstakeing: ' +
              unstaking)
        return [staked, unstaking]
    except Exception:
        print(account + 'has not voted ' + bp)
        return [0, 0]


def get_bp_info(bp):
    out_bytes = get_table(['eosio', 'bps', '-k', bp])
    rows = json.loads(out_bytes)['rows']
    try:
        total_staked = rows[0]['total_staked'].replace(' EOS', '')
        rewards_pool = rows[0]['rewards_pool'].replace(' EOS', '')
        total_voteage = rows[0]['total_voteage']
        return [total_staked, rewards_pool, total_voteage]
    except Exception:
        print(bp + 'is not a bp')
        return [0, 0, 0]


#  change: string 1.0000
def vote(voter, bp, change):
    generate_data = lambda voter, bp, change: {'voter': voter, 'bpname': bp,
                                               'change': change}
    data = generate_data(voter, bp, change)
    out_bytes = push_action(['vote', json.dumps(data), '-p', data['voter']])
    return out_bytes


def tests():
    #  vote: xlc ==>  biosbpa 1.0000 EOS
    before = get_account_votes('xlc', 'biosbpa')
    out_bytes = vote('xlc', 'biosbpa', '1.0000 EOS')
    assert b'executed transaction' in out_bytes
    after = get_account_votes('xlc', 'biosbpa')
    print("vote: xlc ==> biosbpa 1.0000 EOS")
    print('before: ' + str(before))
    print(' after: ' + str(after))

    before = get_bp_info('biosbpa')
    after = get_bp_info('biosbpa')
    print('before: ' + str(before))
    print(' after: ' + str(after))


def main():
    unlock_default_wallet()
    tests()


main()
