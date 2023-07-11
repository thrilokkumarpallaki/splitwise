from flask import Blueprint

from app.enums.payed_type import PayedType
from app.enums.split_type import SplitType
from app.views.expense_view import ExpenseView
from app.utilities.helpers import split_equal_share_users, split_other_share_users, multi_payers_split

expense_api = Blueprint('expense_api', __name__, url_prefix='/expense')


def add_expense(**kwargs):
    user_id = kwargs.get('user_id')
    payed_type = kwargs.get('payed_type')
    payers = kwargs.get('payers', '')
    payees = kwargs.get('payees', '')
    split_type = kwargs.get('split_type')
    total_amount = float(kwargs.get('amount', 0))
    desc = kwargs.get('desc', '')

    # validate and parse payees
    group_id = None
    payees_list = []
    payees_dict = {}
    if payees.strip().lower().startswith('g'):
        group_id = int(payees.lstrip('g'))
    else:
        if split_type == SplitType.EQUAL_SPLIT:
            payees_list = split_equal_share_users(payees)
        else:
            payees_dict = split_other_share_users(payees)

    # Validate and Parse payers
    user_id = int(user_id.strip())
    payers_dict = {}
    if payed_type == PayedType.MULTIPAY:
        payers_dict = multi_payers_split(payers)

    return ExpenseView.create_expense(
        user_id=user_id,
        group_id=group_id,
        payers=payers_dict,
        payees=payees_dict or payees_list,
        split_type=split_type,
        payed_type=payed_type,
        desc=desc,
        total_amount=total_amount
    )
