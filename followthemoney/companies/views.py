from django.shortcuts import render

from django.template import loader

from .models import Company, Shareholder


def index(request):
    companies = Company.objects.all()
    context = {
        "companies": companies,
    }
    return render(request, "companies/index.html", context)

def company_detail(request, company):
    company = Company.objects.get(company=company)

    shareholders = Shareholder.objects.filter(child_company=company).order_by("-share")[:5]
    print("🔴🔴🔴 Company:", company)
    print("🔴🔴🔴 shareholders:", shareholders)
    context = {
        "company":company,
        "shareholders": shareholders,
    }
    return render(request, "companies/company.html", context)