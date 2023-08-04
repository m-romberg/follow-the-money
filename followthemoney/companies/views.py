from django.shortcuts import render

from django.template import loader

from .models import Company


def index(request):
    companies = Company.objects.all()
    context = {
        "companies": companies,
    }
    return render(request, "companies/index.html", context)

def company(request, company):
    company = Company.objects.get(company=company)
    print("🔴🔴🔴 Company:", company)
    context = {
        "company": company,
    }
    return render(request, "companies/company.html", context)