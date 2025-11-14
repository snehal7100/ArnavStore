from django.shortcuts import render, redirect
from ArnavStore.Product.models import ProductModel
from django.contrib import messages


def Products(request):
    # Fetch only product data (NO JOIN)
    pData = ProductModel.objects.all()

    context = {
        "pData": pData,
    }
    return render(request, "product/index.html", context)


def EditProduct(request, id):
    pData = ProductModel.objects.get(id=int(id))

    if request.method == "GET":
        return render(request, "product/edit.html", {"pData": pData})

    else:
        pData.pname = request.POST.get("pname")
        pData.hsncode = request.POST.get("hsncode")
        pData.tax = request.POST.get("tax")
        pData.qty = request.POST.get("qty")
        pData.unit = request.POST.get("unit")
        pData.rate = request.POST.get("rate")
        pData.amt = request.POST.get("amt")

        pData.save()
        return redirect(Products)


def delete(request, id):
    ProductModel.objects.get(id=int(id)).delete()
    return redirect(Products)


def AddProduct(request):
    if request.method == "GET":
        return render(request, "product/addform.html")

    else:
        name = request.POST.get("pname").strip()
        hsncode = request.POST.get("hsncode").strip()
        tax = request.POST.get("tax").strip()
        qty = request.POST.get("qty").strip()
        unit = request.POST.get("unit").strip()
        rate = request.POST.get("rate").strip()
        amt = request.POST.get("amt").strip()

        saveData = ProductModel(
            pname=name,
            hsncode=hsncode,
            tax=tax,
            qty=qty,
            unit=unit,
            rate=rate,
            amt=amt,
        )

        saveData.save()
        return redirect(Products)
