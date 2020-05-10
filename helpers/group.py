from collections import defaultdict


def group_ownership(list_: list, key: str, total_shares: int) -> dict:
    '''
    Groups investments by investor, aggregating shares, cash_paid and
    investor ownership
    '''

    rv = []
    dups = defaultdict(dict)

    for l in list_:
        cash_paid = float(l['cash_paid'])
        shares = int(l['shares'])

        if(dups[l[key]]):
            cash_paid += dups[l[key]]['cash_paid']
            shares += dups[l[key]]['shares']

        dup = {
            'cash_paid': cash_paid,
            'shares': shares,
            'ownership': round((int(shares) / int(total_shares)) * 100, 2),
        }

        dups[l[key]] = dup

    for key in dups.keys():
        owner = {
            "investor": key,
            "shares": dups[key].get('shares'),
            "cash_paid": dups[key].get('cash_paid'),
            "ownership": dups[key].get('ownership'),
        }
        rv.append(owner)

    return rv
