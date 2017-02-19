from django.shortcuts import render


@login_required
def portfolio_detail(request, id, template_name="portfolio.html"):
    queryset = Portfolios.objects.all()
    portfolio = get_object_or_404(queryset, id=id)

    records_qs = portfolio.records.all()
    
    records = paginator(records_qs.order_by('-activity_at'), request)

    context = dict(user=portfolio.user,
                   value=portfolio.value)

    return render(request, template_name, context)