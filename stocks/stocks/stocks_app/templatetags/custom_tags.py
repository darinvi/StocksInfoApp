from django import template
from stocks.stocks_app.stock_info import get_all_data
from datetime import datetime

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

