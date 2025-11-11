from django.contrib import admin
from django.urls import path
from ArnavStore import views, categoryview, brandview, productview, Taxview, loginvalid, customerview, Dashboardview, supplierview, posview, employee, Paymentview, rewardsview, barcodeview, posmasterview, poschildview, billlistview
from ArnavStore import settings  
from django.conf.urls.static import static  

urlpatterns = [ 
    path('save-bill/', posmasterview.save_bill, name='save_bill'),
    path('customer-report/',posmasterview.customer_report),
    path('BillList/', billlistview.BillList, name='bill_list'),
    path('bill_view/<int:id>/', billlistview.BillView, name='bill_view'),
    path('bill-report/', poschildview.bill_report),

    path('dashboard/', Dashboardview.dashboard),
    path('pos/', posview.posdashboard),
    path('barcode-print/', barcodeview.Barcodes),

    path('category-list/',categoryview.category),
    path('category-add/',categoryview.addcategory),
    path('category-view/<id>',categoryview.categoryview),
    path('category-edit/<id>',categoryview.editcategory),
    path('category-delete/<id>',categoryview.delete),

    path('admin/', admin.site.urls),
    path('', views.Login),
    path('valid/', loginvalid.login_view),
    path('index/', Dashboardview.dashboard),

    path('brand-list/', brandview.Brands),
    path('brand-edit/<id>', brandview.editBrand),
    path('brand-delete/<id>', brandview.delete),
    path('brand-add/', brandview.AddBrand),

    path('tax-list/', Taxview.TaxList),
    path('tax-view/<id>/', Taxview.TaxView),
    path('tax-edit/<id>/', Taxview.editTax),
    path('tax-delete/<id>/', Taxview.deleteTax),
    path('tax-add/', Taxview.addTax),

    path('customer-list/', customerview.Customers),
    path('customer-view/<int:id>', customerview.editCustomer),
    path('customer-edit/<int:id>', customerview.editCustomer),
    path('customer-delete/<int:id>', customerview.deleteCustomer),
    path('customer-add/', customerview.AddCustomer),

    path('product-list/', productview.Products),
    path('product-edit/<id>', productview.EditProduct),
    path('product-delete/<id>', productview.delete),
    path('product-add/', productview.AddProduct),

    path('supplier-list/', supplierview.SuppliersList),
    path('supplier-view/<id>/', supplierview.editSupplier),
    path('supplier-edit/<id>/', supplierview.editSupplier),
    path('supplier-delete/<id>/', supplierview.deleteSupplier),
    path('supplier-add/', supplierview.AddSupplier),

    path('Employee-list/', employee.emp),
    path('Employee-view/<id>/', employee.employeeview),
    path('Employee-edit/<id>/', employee.editemployee),
    path('Employee-delete/<id>/', employee.deleteemployee),
    path('Employee-add/', employee.Addemployee),

    path('rewards-list/', rewardsview.Rewards),
    path('rewards-add/', rewardsview.AddRewards),
    path('rewards-edit/<id>/', rewardsview.editRewards),
    path('rewards-delete/<id>', rewardsview.delete),

    path('Payment-list/', Paymentview.payments),
    path('Payment-edit/<id>', Paymentview.editpayment),
    path('Payment-delete/<id>', Paymentview.delete),
    path('Payment-add/', Paymentview.AddPayment),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)