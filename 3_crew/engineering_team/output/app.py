import gradio as gr
from accounts import Account, get_share_price

def create_account(account_id, initial_deposit):
    global account
    account = Account(account_id, float(initial_deposit))
    return f"Account '{account_id}' created with deposit: ${initial_deposit:.2f}"

def deposit(amount):
    account.deposit_funds(float(amount))
    return f"Deposited: ${amount:.2f}. New balance: ${account.balance:.2f}"

def withdraw(amount):
    if account.withdraw_funds(float(amount)):
        return f"Withdrew: ${amount:.2f}. New balance: ${account.balance:.2f}"
    return f"Error: Insufficient funds to withdraw ${amount:.2f}."

def buy_shares(symbol, quantity):
    if account.buy_shares(symbol, int(quantity)):
        return f"Bought {quantity} shares of {symbol}. Remaining balance: ${account.balance:.2f}"
    return f"Error: Unable to buy {quantity} shares of {symbol}. Check your balance."

def sell_shares(symbol, quantity):
    if account.sell_shares(symbol, int(quantity)):
        return f"Sold {quantity} shares of {symbol}. New balance: ${account.balance:.2f}"
    return f"Error: Unable to sell {quantity} shares of {symbol}. Check your holdings."

def portfolio_value():
    value = account.calculate_portfolio_value()
    return f"Total portfolio value: ${value:.2f}"

def profit_loss():
    profit_loss_value = account.calculate_profit_loss()
    return f"Profit/Loss: ${profit_loss_value:.2f}"

def holdings():
    return f"Current Holdings: {account.get_holdings()}"

def transactions():
    return f"Transactions: {account.get_transactions()}"

with gr.Blocks() as app:
    gr.Markdown("## Trading Account Management System")
    
    with gr.Group():
        account_id = gr.Textbox(label="Account ID")
        initial_deposit = gr.Number(label="Initial Deposit")
        create_button = gr.Button("Create Account")
        create_button.click(create_account, inputs=[account_id, initial_deposit], outputs="text")
    
    with gr.Group():
        deposit_amount = gr.Number(label="Deposit Amount")
        deposit_button = gr.Button("Deposit")
        deposit_button.click(deposit, inputs=deposit_amount, outputs="text")
        
        withdraw_amount = gr.Number(label="Withdraw Amount")
        withdraw_button = gr.Button("Withdraw")
        withdraw_button.click(withdraw, inputs=withdraw_amount, outputs="text")
        
    with gr.Group():
        buy_symbol = gr.Textbox(label="Buy Symbol (AAPL, TSLA, GOOGL)")
        buy_quantity = gr.Number(label="Buy Quantity")
        buy_button = gr.Button("Buy Shares")
        buy_button.click(buy_shares, inputs=[buy_symbol, buy_quantity], outputs="text")
        
        sell_symbol = gr.Textbox(label="Sell Symbol (AAPL, TSLA, GOOGL)")
        sell_quantity = gr.Number(label="Sell Quantity")
        sell_button = gr.Button("Sell Shares")
        sell_button.click(sell_shares, inputs=[sell_symbol, sell_quantity], outputs="text")
    
    with gr.Group():
        portfolio_value_button = gr.Button("Portfolio Value")
        portfolio_value_text = gr.Textbox(label="Portfolio Value", interactive=False)
        portfolio_value_button.click(portfolio_value, outputs=portfolio_value_text)
        
        profit_loss_button = gr.Button("Profit/Loss")
        profit_loss_text = gr.Textbox(label="Profit/Loss", interactive=False)
        profit_loss_button.click(profit_loss, outputs=profit_loss_text)
        
        holdings_button = gr.Button("View Holdings")
        holdings_text = gr.Textbox(label="Holdings", interactive=False)
        holdings_button.click(holdings, outputs=holdings_text)
        
        transactions_button = gr.Button("View Transactions")
        transactions_text = gr.Textbox(label="Transactions", interactive=False)
        transactions_button.click(transactions, outputs=transactions_text)

app.launch()