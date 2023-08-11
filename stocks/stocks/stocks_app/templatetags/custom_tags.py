from django import template
from stocks.stocks_app.stock_info import get_all_data
from datetime import datetime
from stocks.stocks_app.models import Transaction

register = template.Library()

@register.inclusion_tag('inclusions/render_chart.html')
def render_chart(ticker):
    data = get_all_data(ticker)

    dates = [datetime.fromtimestamp(d).strftime("%d-%m-%Y") for d in data['t']]
    opens = [d for d in data['o']]
    highs = [d for d in data['h']]
    lows = [d for d in data['l']]
    closes = [d for d in data['c']]

    return {
        'dates': dates,
        'opens': opens,
        'highs': highs,
        'lows': lows,
        'closes': closes,
        'ticker': ticker
    }


@register.inclusion_tag('inclusions/display_position.html')
def display_position(ticker, pk, price):
    tx = Transaction.objects.filter(user__pk=pk, ticker=ticker)
    amount = sum([t.amount for t in tx])

    return {
        'ticker':ticker,
        'amount': amount,
        'valued': amount * price
    }


@register.inclusion_tag('inclusions/profile_positions.html')
def profile_positions(pk):
    transactions = Transaction.objects.filter(user__pk=pk)
    tickers = set([t.ticker for t in transactions])

    if transactions:
        positions = {ticker:get_position_data(transactions, ticker) for ticker in tickers}  
        total_exposure = calculate_total_exposure(positions)

        return { 
            'positions': positions,
            'total': total_exposure
        }


class Tx:
    def __init__(self, amount, price):
        self.amount = amount
        self.price = price
        self.final = False

def get_position_data(tx, ticker):
    print(ticker)
    curr_tx = [t for t in tx if t.ticker == ticker]
    return get_current_position(curr_tx)

def get_current_position(tx):
    transactions = [Tx(a.amount, a.price) for a in tx]
    while len(transactions) > 1:
        if transactions[0].final:
            break
        for i in range(1,len(transactions)):
            transactions = list(filter(lambda x: x.amount != 0, transactions))
            if len(transactions) == 1:
                break
            if i > len(transactions):
                break
            curr_tx = transactions[i]
            benchmark = transactions[0]

            if benchmark.amount * curr_tx.amount > 0 and len([ t for t in transactions if t.amount * benchmark.amount > 0]) == len(transactions): 
                total_amount = sum([ t.amount for t in transactions])
                average_price = sum([ t.amount * t.price for t in transactions]) / total_amount
                last_tx = Tx(total_amount, average_price)
                last_tx.final = True
                transactions = [ last_tx ]
                break
            
            if benchmark.amount * curr_tx.amount > 0:
                continue
            
            if benchmark.amount > 0 and abs(curr_tx.amount) <= benchmark.amount:
                benchmark.amount -= -curr_tx.amount
                curr_tx.amount = 0
                break
            
            if benchmark.amount > 0 and abs(curr_tx.amount) > benchmark.amount:
                curr_tx.amount += benchmark.amount 
                benchmark.amount = 0
                break
            
            if benchmark.amount < 0 and curr_tx.amount <= abs(benchmark.amount):
                benchmark.amount += curr_tx.amount
                curr_tx.amount = 0
                break
            
            if benchmark.amount < 0 and curr_tx.amount > abs(benchmark.amount):
                curr_tx.amount += benchmark.amount
                benchmark.amount = 0
                break

    return { 
        'amount': transactions[0].amount,
        'price': transactions[0].price,
        'total': abs(transactions[0].amount) * transactions[0].price,
    }

def calculate_total_exposure(positons):
    return  sum([total['total'] for total in positons.values()])