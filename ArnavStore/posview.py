from django.shortcuts import render
from ArnavStore.Customer.models import Customer
from ArnavStore.Product.models import ProductModel
from ArnavStore.payment.models import Payment  # Import the Payment model
from ArnavStore.category.models import Category
from ArnavStore.Brand.models import BrandForm
from ArnavStore.Taxes.models import Taxs  # Import your models for category, brand, and taxes

def posdashboard(request):
    # Fetch data for customers, products, and payment terms
    cData = Customer.objects.all()  # Fetch all customer records
    pData = ProductModel.objects.all()  # Fetch all product records
    paymentData = Payment.objects.all()  # Fetch all payment terms

    # Fetch data for the modal
    categoryData = Category.objects.all()  # Fetch all categories
    brandData = BrandForm.objects.all()  # Fetch all brands
    taxData = Taxs.objects.all()  # Fetch all tax types

    return render(request, "Pos/posindex.html", {
        "customerData": cData,
        "productData": pData,
        "paymentData": paymentData,  # Pass payment terms to the template
        "categoryData": categoryData,  # Pass category data to the template
        "brandData": brandData,  # Pass brand data to the template
        "taxData": taxData  # Pass tax data to the template
    })
