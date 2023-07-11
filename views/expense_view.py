from app.enums.payed_type import PayedType
from app.enums.split_type import SplitType
from app.exceptions import UsersNotBelongToGroup
from app.models.group_model import GroupModel
from app.models.user_group_mapping_model import UserGroupMappingModel
from app.strategies.split_calculator_context import delegate_expense


class ExpenseView:
    @staticmethod
    def create_expense(**kwargs):
        user_id = kwargs.get('user_id')
        group_id = kwargs.get('group_id')
        payers = kwargs.get('payers', {})
        payees = kwargs.get('payees', [])
        split_type = kwargs.get('split_type')
        payed_type = kwargs.get('payed_type')
        desc = kwargs.get('desc')
        total_amount = kwargs.get('total_amount', 0)

        # Check if expense is associated with the group
        members = payees
        payed_users = payers
        if group_id is not None:
            group_obj = GroupModel.get_group(group_id)

            # Check if all members involved in the expense is also part of group
            if group_obj is not None:
                payed_user_ids = [user_id] if str(user_id) not in payed_users else []

                # Fetch all the group members
                if split_type == SplitType.EQUAL_SPLIT:
                    members = group_obj.members
                    members = set(map(lambda member: member.id, members))

                if payed_type == PayedType.MULTIPAY:
                    payed_user_ids.extend(list(map(int, payers.keys())))
                    belonging_check_status = UserGroupMappingModel.check_for_users(group_id, payed_user_ids)
                    if not belonging_check_status:
                        raise UsersNotBelongToGroup(f'One or more users not belong to the group: {group_obj.name}')

        split_context = delegate_expense(split_type, total_amount, user_id, payed_users)
        expense_obj = split_context.calculate_split(users=members, group_id=group_id, description=desc)

        # Save Expense object & User Expense objects
        expense_status = expense_obj.save()
        if expense_status:
            return 'SUCCESS'
        return 'FAILED'
