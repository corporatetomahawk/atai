from decimal import Decimal as D
from logging import getLogger

from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.generic import RedirectView
from moneyed import Money


LOG = getLogger(__name__)


@login_required
def dashboard(request,
              template_name="dashboard.html",
              success_url=None):

    user = get_object_or_404(request.user.portfolios.all())

    return render(request, template_name, context)
