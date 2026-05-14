from django.http import HttpResponse

tax_rate = 0.15

def home(request):
    return HttpResponse("<h1>This is a site to calculate tax</h1>")

def calculate_tax(request, number):
    total = number + (number * tax_rate)
    return HttpResponse(f"<h1>{total}</h1>")

def show_tax_rate(request):
    return HttpResponse(f"<h1>{tax_rate * 100}%</h1>")