from xml.etree.ElementInclude import include
from django.urls import path
from .views import account_profile, card_profile, customer_profile, edit_account, edit_card, edit_profile, edit_receipt, edit_transaction, edit_wallet, list_account, list_card, list_customers, list_loan, list_notification, list_receipt, list_reward, list_thirdparty, list_transaction, list_wallets, receipt_profile, register_account, register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet, transaction_profile, wallet_profile


urlpatterns =[
    path("register/", register_customer,name="registration"),
    path("wallet/", register_wallet,name="wallet"),
    path("account/", register_account,name="account"),
    path("transaction/", register_transaction,name="transaction"),
    path("card/", register_card,name="card"),
    path("thirdparty/", register_thirdparty,name="thirdparty"),
    path("notification/", register_notification,name="notification"),
    path("receipt/", register_receipt,name="receipt"),
    path("loan/", register_loan,name="loan"),
    path("reward/", register_reward,name="reward"),
    path("customers/",list_customers,name="customers"),
    path("wallets/",list_wallets,name="wallets"),
    path("accounts/",list_account,name="accounts"),
    path("cards/",list_card,name="cards"),
    path("thirdpartys/",list_thirdparty,name="thirdpartys"),
    path("notifications/",list_notification,name="notifications"),
    path("receipts/",list_receipt,name="receipts"),
    path("loans/",list_loan,name="loans"),
    path("rewards/",list_reward,name="rewards"),
    path("transactions/",list_transaction,name="transactions"),
    path("customers/<int:id>/", customer_profile,name="customer_profile"),
    path("customers/edit/<int:id>/", edit_profile,name="edit_profile"),
    path("wallets/<int:id>/", wallet_profile,name="wallet_profile"),
    path("wallets/edit/<int:id>/", edit_wallet,name="edit_wallet"),
    path("accounts/<int:id>/",account_profile,name="account_profile"),
    path("accounts/edit/<int:id>/", edit_account,name="edit_account"),
    path("transactions/<int:id>/",transaction_profile,name="transaction_profile"),
    path("transactions/edit/<int:id>/", edit_transaction,name="edit_transaction"),
    path("cards/<int:id>/",card_profile,name="card_profile"),
    path("cards/edit/<int:id>/", edit_card,name="edit_card"),
    path("receipts/<int:id>/",receipt_profile,name="receipt_profile"),
    path("receipts/edit/<int:id>/",edit_receipt,name="edit_receipt"),
    ]