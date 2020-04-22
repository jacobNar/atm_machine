"""This file tests account module methods and properties.

Run "pytest" in this folder to automatically run these tests.

Expected output:
    12 passed in 0.xx seconds

"""
import pytest
import account

account = account.Account()


def test_balance_has_zero_balance_at_start():
    assert account.balance == 0


def test_deposit_credits_the_account_correctly():
    account.deposit(600)
    assert account.balance == 600


def test_deposit_print_error_message_if_deposit_amount_is_negative(capsys):
    account.deposit(-600)
    captured = capsys.readouterr()
    assert captured.out == ("You may deposit positive amount only. $-600 is" +
                            " not valid.\n")


def test_deposit_print_error_message_if_deposit_amount_is_zero(capsys):
    account.deposit(0)
    captured = capsys.readouterr()
    assert captured.out == ("You may deposit positive amount only. $0 is " +
                            "not valid.\n")


def test_withdrawal_debits_account_correctly():
    account.withdrawal(350)
    assert account.balance == 250


def test_withdrawal_print_error_message_if_not_enough_funds_available(capsys):
    account.withdrawal(275)
    captured = capsys.readouterr()
    assert captured.out == ("You can't withdraw more funds than you have " +
                            "available. Your balance is $250. You have " +
                            "requested $275.\n")


def test_withdrawal_print_error_message_if_requested_amount_higher_than_allowed_withdrawal_limit(capsys):
    account.deposit(250)
    account.withdrawal(450)
    captured = capsys.readouterr()
    assert captured.out == ("Your withdrawal request has been denied. ATM " +
                            "daily withdrawal limit is $400.00. You have " +
                            "requested $450.\n")


def test_withdrawal_print_error_message_if_requested_amount_is_zero(capsys):
    account.withdrawal(0)
    captured = capsys.readouterr()
    assert captured.out == ("Your withdrawal amount must be a positive " +
                            "number. $0 is not valid.\n")


def test_withdrawal_print_error_message_if_requested_amount_is_negative(capsys):
    account.withdrawal(-50)
    captured = capsys.readouterr()
    assert captured.out == ("Your withdrawal amount must be a positive " +
                            "number. $-50 is not valid.\n")


# def test_withdrawal_print_error_message_if_account_balance_is_zero_or_negative(capsys):
#     account.withdrawal(100)
#     captured = capsys.readouterr()
#     assert captured.out == ("You don't have enough funds to complete the " +
#                             "transaction. Your balance is $0.\n")
