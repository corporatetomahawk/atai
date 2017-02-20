from django.shortcuts import render
import django_tables2 as tables
import quandl
import os


class StockTable(tables.Table):
    date = tables.Column()
    open = tables.Column()
    high = tables.Column()
    low = tables.Column()
    close = tables.Column()
    volume = tables.Column()


def portfolio_detail(request, id, template_name="portfolio.html"):
    queryset = Portfolios.objects.all()
    portfolio = get_object_or_404(queryset, id=id)

    records_qs = portfolio.records.all()
    
    records = paginator(records_qs.order_by('-activity_at'), request)

    context = dict(user=portfolio.user,
                   value=portfolio.value)

    return render(request, template_name, context)


def profile(request):
    stock_data = [{'date': [],
                   'open': [],
                   'high': [],
                   'low': [],
                   'close': [],
                   'volume': []}]
    table = StockTable(stock_data)
    if request.method == 'POST':
        quandl.ApiConfig.api_key = os.environ.get('QUANDL_API_KEY')
        stock = request.POST.get('stock')
        req = quandl.get('XLON/{}'.format(stock))
        stock_data = []
        for data in req.iterrows():
            stock_data.append({'date': data[0],
                               'open': data[1]['Open'],
                               'high': data[1]['High'],
                               'low': data[1]['Low'],
                               'close': data[1]['Close'],
                               'volume': data[1]['Volume']})
        table = StockTable(stock_data)
    return render(request, 'profile.html', {"table": table})


def simple_list(request):
    quandl.ApiConfig.api_key = os.environ.get('QUANDL_API_KEY')
    stock = 'SXX'
    req = quandl.get('XLON/{}'.format(stock))
    table = StockTable(req)
    return render(request, "simple_table.html", {"table": table})