from django.urls import path
from .views import register_account, register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet


urlpatterns =[
    path("register/", register_customer,name="registration")
]

urlpatterns=[
     path("register/", register_wallet,name="registration")
]
urlpatterns=[
     path("register/", register_account,name="registration")
]

urlpatterns=[
     path("register/", register_transaction,name="registration")
]

urlpatterns=[
     path("register/", register_card,name="registration")
]

urlpatterns=[
     path("register/", register_thirdparty,name="registration")
]

urlpatterns=[
     path("register/", register_notification,name="registration")
]

urlpatterns=[
     path("register/", register_receipt,name="registration")
]
urlpatterns=[
     path("register/", register_loan,name="registration")
]

urlpatterns=[
     path("register/", register_reward,name="registration")
]