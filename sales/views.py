# Create your views here.
from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime, timedelta
import calendar
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from invoices.models import Invoice  # 👈 ye import zaruri hai


def sales_overview(request):
    # Get selected year and month from GET parameters
    selected_year = int(request.GET.get('year', now().year))
    selected_month = request.GET.get('month')
    selected_month = int(selected_month) if selected_month else now().month

    # Years list for dropdown
    years_list = list(Invoice.objects.values_list('date__year', flat=True).distinct().order_by('date__year'))

    # Summary totals for selected year
    total_sales = Invoice.objects.filter(date__year=selected_year).aggregate(Sum('total_amount'))[
                      'total_amount__sum'] or 0
    total_paid = Invoice.objects.filter(date__year=selected_year, status='Paid').aggregate(Sum('total_amount'))[
                     'total_amount__sum'] or 0
    total_unpaid = Invoice.objects.filter(date__year=selected_year, status='Unpaid').aggregate(Sum('total_amount'))[
                       'total_amount__sum'] or 0
    total_overdue = Invoice.objects.filter(date__year=selected_year, status='Overdue').aggregate(Sum('total_amount'))[
                        'total_amount__sum'] or 0

    # Months list for dropdown
    months_list = [{'num': m, 'name': calendar.month_name[m]} for m in range(1, 13)]
    selected_month_name = calendar.month_name[selected_month]

    # Monthly Sales for selected year
    monthly_qs = Invoice.objects.filter(date__year=selected_year) \
        .values('date__month') \
        .annotate(total=Sum('total_amount'))
    monthly_dict = {m['date__month']: m['total'] for m in monthly_qs}
    monthly_sales = [{'date__month': m, 'total': monthly_dict.get(m, 0)} for m in range(1, 13)]

    # Weekly / Daily Sales for selected month
    first_day = datetime(selected_year, selected_month, 1)
    last_day = datetime(selected_year, selected_month, calendar.monthrange(selected_year, selected_month)[1])

    week_qs = Invoice.objects.filter(date__range=(first_day, last_day)) \
        .values('date') \
        .annotate(total=Sum('total_amount'))
    week_dict = {ws['date']: ws['total'] for ws in week_qs}

    week_sales = []
    current_day = first_day
    while current_day <= last_day:
        week_sales.append({
            'date': current_day.date(),
            'total': week_dict.get(current_day.date(), 0)
        })
        current_day += timedelta(days=1)

    context = {
        'title': 'Total Sales',
        'total_sales': total_sales,
        'total_paid': total_paid,
        'total_unpaid': total_unpaid,
        'total_overdue': total_overdue,
        'monthly_sales': monthly_sales,
        'week_sales': week_sales,
        'years_list': years_list,
        'months_list': months_list,
        'selected_year': selected_year,
        'selected_month': selected_month,
        'selected_month_name': selected_month_name,
    }
    return render(request, 'overview.html', context)