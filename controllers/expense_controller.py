from flask import Blueprint

from app.enums.payed import PayedType
from app.views.expense_view import ExpenseView

expense_api = Blueprint('expense_api', __name__, url_prefix='/expense')


def add_expense(**kwargs):
    user_id = kwargs.get('user_id')
    payed_type = kwargs.get('payed_type')
    payers = kwargs.get('payers')
    payees = kwargs.get('payees', '')
    split_type = kwargs.get('split_type')
    desc = kwargs.get('desc')

    # validate and parse payees
    user_ids = []
    group_id = None
    if payees.strip().lower().startswith('g'):
        group_id = int(payees.lstrip('g'))
    else:
        # It is user id(s)
        payees_split = payees.split(' ')

        for payee in payees_split:
            if payee.lower().startswith('u'):
                uid = int(payee.lstrip('u'))
                user_ids.append(uid)
    
    # Validate and Parse payers
    payers_list = []
    if payed_type == PayedType.IPAY:
        payer = int(payers.lower().strip().lstrip('u'))
        payers.append(payer)
    elif payed_type == PayedType.MULTIPAY:
        payers_split = payers.split(' ')
        for payer in payers_split:
            payer = int(payer.lower().strip().lstrip('u'))
            payers_list.append(payer)

    return ExpenseView.create_expense(
        user_id=user_id,
        group_id=group_id,
        user_ids=user_ids,
        payers=payers,
        split_type=split_type,
        desc=desc,
    )
