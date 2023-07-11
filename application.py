"""
 App initial point
"""
import click
from flask import Flask
from flask.cli import with_appcontext

from app.controllers import user_controller, group_controller, expense_controller
from app.commands.commands import Commands

app = Flask(__name__)


@click.command(name=Commands.REGISTER)
@click.option("--name")
@click.option("--phone")
@click.option("--password")
@with_appcontext
def create_user(name, phone, password):
    """
    A Flask cli command for creating user.
    :param name: Name of the user
    :param phone: Phone number of the user.
    :param password: Password of the user.
    :return: None
    """
    status = user_controller.create_user(name=name, phone=phone, password=password)
    print(status)


@click.command(name=Commands.UPDATE)
@click.option("--user_id")
@click.option("--password")
@with_appcontext
def update_user(user_id, password):
    """
    A Flask cli command to update user.
    :param user_id: A unique user id.
    :param password: New password of the user.
    :return: None
    """
    status = user_controller.update_user(user_id=user_id, password=password)
    print(status)


@click.command(name=Commands.ADD_GROUP)
@click.option("--user_id")
@click.option("--group_name")
@with_appcontext
def create_group(user_id, group_name):
    """
    A Flask cli command to create a group
    :param user_id: A user who's creating the group.
    :param group_name: Name of the group.
    :return: None
    """
    status = group_controller.create_group(user_id=user_id, group_name=group_name)
    print(status)


@click.command(name=Commands.ADD_MEMBER)
@click.option("--admin_id")
@click.option("--group_id")
@click.option("--user_id")
@with_appcontext
def add_member(admin_id, group_id, user_id):
    """
    A Flask cli command to add member to the group.
    :param admin_id: user id who created the group.
    :param group_id: A group id to which the member is being added.
    :param user_id: A user id who wants to get added to the group.
    :return: None
    """
    status = group_controller.add_member(admin_id=admin_id, group_id=group_id, user_id=user_id)
    print(status)


@click.command(name=Commands.GROUPS)
@click.option("--user_id")
@with_appcontext
def show_groups(user_id):
    """
    A Flask command to show the list of groups that the user is part of.
    :param user_id: An id of the user to list the groups.
    :return: None
    """
    user_groups = group_controller.show_groups(user_id=user_id)
    for name, desc in user_groups.items():
        print(' - '.join([name, desc or 'No Description']))


@click.command(name=Commands.EXPENSE)
@click.option("--user_id")
@click.option("--payed_type")
@click.option("--payers")
@click.option("--payees")
@click.option("--split_type")
@click.option("--desc")
@click.option("--amount")
def add_expense(user_id, payed_type, split_type, payees, desc, amount, payers=None):
    """
    A Flask command to add expenses
    """
    result = expense_controller.add_expense(user_id=user_id,
                                            payed_type=payed_type,
                                            split_type=split_type,
                                            desc=desc,
                                            amount=amount,
                                            payers=payers,
                                            payees=payees)
    print(result)


app.cli.add_command(create_user)
app.cli.add_command(update_user)
app.cli.add_command(create_group)
app.cli.add_command(add_member)
app.cli.add_command(show_groups)
app.cli.add_command(add_expense)
