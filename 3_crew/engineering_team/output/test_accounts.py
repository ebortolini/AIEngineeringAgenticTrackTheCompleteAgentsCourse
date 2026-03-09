import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(account_id="12345", initial_deposit=1000.0)

    def test_initialization(self):
        self.assertEqual(self.account.account_id, "12345")
        self.assertEqual(self.account.initial_deposit, 1000.0)
        self.assertEqual(self.account.balance, 1000.0)
        self.assertEqual(self.account.holdings, {})
        self.assertEqual(self.account.transactions, [])

    def test_deposit_funds(self):
        self.account.deposit_funds(500.0)
        self.assertEqual(self.account.balance, 1500.0)
        self.assertEqual(len(self.account.transactions), 1)
        self.assertEqual(self.account.transactions[0], {'type': 'deposit', 'amount': 500.0})

    def test_withdraw_funds(self):
        result = self.account.withdraw_funds(300.0)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 700.0)
        self.assertEqual(len(self.account.transactions), 1)
        self.assertEqual(self.account.transactions[0], {'type': 'withdraw', 'amount': 300.0})

    def test_withdraw_funds_insufficient_balance(self):
        result = self.account.withdraw_funds(1100.0)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, 1000.0)
        self.assertEqual(len(self.account.transactions), 0)

    def test_buy_shares(self):
        result = self.account.buy_shares('AAPL', 3)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 850.0)
        self.assertEqual(self.account.holdings, {'AAPL': 3})
        self.assertEqual(len(self.account.transactions), 1)
        self.assertEqual(self.account.transactions[0], {'type': 'buy', 'symbol': 'AAPL', 'quantity': 3})

    def test_buy_shares_insufficient_balance(self):
        result = self.account.buy_shares('AAPL', 10)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, 850.0)
        self.assertEqual(self.account.holdings, {'AAPL': 3})

    def test_sell_shares(self):
        self.account.buy_shares('AAPL', 3)
        result = self.account.sell_shares('AAPL', 2)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 950.0)
        self.assertEqual(self.account.holdings, {'AAPL': 1})
        self.assertEqual(len(self.account.transactions), 2)
        self.assertEqual(self.account.transactions[1], {'type': 'sell', 'symbol': 'AAPL', 'quantity': 2})

    def test_sell_shares_insufficient_holdings(self):
        result = self.account.sell_shares('AAPL', 2)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, 950.0)
        self.assertEqual(self.account.holdings, {'AAPL': 1})

    def test_calculate_portfolio_value(self):
        self.account.deposit_funds(500.0)
        self.account.buy_shares('AAPL', 3)
        value = self.account.calculate_portfolio_value()
        self.assertEqual(value, 850.0 + (3 * 150.0))

    def test_calculate_profit_loss(self):
        value = self.account.calculate_profit_loss()
        self.assertEqual(value, (1000.0 + (3 * 150.0) - 1000.0))

    def test_get_holdings(self):
        self.account.buy_shares('AAPL', 3)
        holdings = self.account.get_holdings()
        self.assertEqual(holdings, {'AAPL': 3})

    def test_get_transactions(self):
        self.account.deposit_funds(200.0)
        transactions = self.account.get_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0], {'type': 'deposit', 'amount': 200.0})

    def test_report_profit_loss_at(self):
        self.account.deposit_funds(200.0)
        loss = self.account.report_profit_loss_at('2023-01-01')
        self.assertEqual(loss, (1000.0 + (0 * 150.0) - 1000.0))

if __name__ == '__main__':
    unittest.main()