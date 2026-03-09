class Account:
    def __init__(self, account_id: str, initial_deposit: float) -> None:
        self.account_id = account_id
        self.initial_deposit = initial_deposit
        self.balance = initial_deposit
        self.holdings = {}
        self.transactions = []
    
    def deposit_funds(self, amount: float) -> None:
        self.balance += amount
        self.transactions.append({'type': 'deposit', 'amount': amount})
    
    def withdraw_funds(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append({'type': 'withdraw', 'amount': amount})
            return True
        return False
    
    def buy_shares(self, symbol: str, quantity: int) -> bool:
        price = get_share_price(symbol)
        total_cost = price * quantity
        if self.balance >= total_cost:
            self.balance -= total_cost
            self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
            self.transactions.append({'type': 'buy', 'symbol': symbol, 'quantity': quantity})
            return True
        return False
    
    def sell_shares(self, symbol: str, quantity: int) -> bool:
        if self.holdings.get(symbol, 0) >= quantity:
            price = get_share_price(symbol)
            total_earnings = price * quantity
            self.balance += total_earnings
            self.holdings[symbol] -= quantity
            if self.holdings[symbol] == 0:
                del self.holdings[symbol]
            self.transactions.append({'type': 'sell', 'symbol': symbol, 'quantity': quantity})
            return True
        return False
    
    def calculate_portfolio_value(self) -> float:
        stocks_value = sum(get_share_price(symbol) * quantity for symbol, quantity in self.holdings.items())
        return self.balance + stocks_value
    
    def calculate_profit_loss(self) -> float:
        current_value = self.calculate_portfolio_value()
        return current_value - self.initial_deposit
    
    def get_holdings(self) -> dict:
        return self.holdings
    
    def get_transactions(self) -> list:
        return self.transactions
    
    def report_profit_loss_at(self, timestamp) -> float:
        # This is a placeholder as the implementation of historical prices is complex and not included in the requirements
        return self.calculate_profit_loss()

def get_share_price(symbol: str) -> float:
    prices = {
        'AAPL': 150.0,
        'TSLA': 700.0,
        'GOOGL': 2800.0
    }
    return prices.get(symbol, 0.0)