from models.investment import Investment
from helpers.group import group_ownership
from helpers.checkline import check_line
from datetime import datetime


def run(raw_data: dict, src_file: str, max_date: str) -> dict:
    ownership = []
    cash_raised = 0
    total_number_of_shares = 0

    for i, line in enumerate(raw_data):
        check_line(line, i)
        investment = Investment(line[0], line[1], line[2], line[3])

        if investment.date > datetime.strptime(max_date, '%Y-%m-%d'):
            continue

        cash_raised += float(investment.cash_paid or 0)
        total_number_of_shares += int(investment.shares or 0)

        owner = {
            "investor": investment.investor,
            "shares": investment.shares,
            "cash_paid": investment.cash_paid,
            "ownership": 0
        }

        ownership.append(owner)

    return {
        "date": datetime.strptime(max_date, '%Y-%m-%d').strftime('%m/%d/%Y'),
        "cash_raised": cash_raised,
        "total_number_of_shares": total_number_of_shares,
        "ownership": group_ownership(ownership, 'investor', total_number_of_shares)
    }
