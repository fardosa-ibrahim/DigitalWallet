from django.shortcuts import render

from walletapp.models import Account, Card, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Transaction, Wallet
from .forms import CustomerRegistrationForm
from .forms import WalletRegistrationForm
from .forms import AccountRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import CardRegistrationForm
from .forms import ThirdpartyRegistrationForm
from .forms import NotificationRegistrationForm
from .forms import ReceiptRegistrationForm
from .forms import LoanRegistrationForm
from .forms import RewardRegistrationForm


# Create your views here.
def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html" ,{"form":form})


def register_wallet(request):
    if request.method == "POST":
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html" ,{"form":form})

def register_account(request):
    if request.method == "POST":
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=AccountRegistrationForm()
    return render(request,"wallet/register_account.html" ,{"form":form})

def register_transaction(request):
    if request.method == "POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html" ,{"form":form})

def register_card(request):
    if request.method == "POST":
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CardRegistrationForm()
    return render(request,"wallet/register_card.html" ,{"form":form})


def register_thirdparty(request):
    if request.method == "POST":
        form = ThirdpartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ThirdpartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html" ,{"form":form})

def register_notification(request):
    if request.method == "POST":
        form = NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html" ,{"form":form})

def register_receipt(request):
    if request.method == "POST":
        form = ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html" ,{"form":form})

def register_loan(request):
    if request.method == "POST":
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=LoanRegistrationForm()
    return render(request,"wallet/register_loan.html" ,{"form":form})

def register_reward(request):
    if request.method == "POST":
        form = RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=RewardRegistrationForm()
    return render(request,"wallet/register_reward.html" ,{"form":form})



def list_customers(request):
    customers= Customer.objects.all()
    return render(request,'wallet/customers_list.html',{"customers":customers})

def list_wallets(request):
    wallets= Wallet.objects.all()
    return render(request,'wallet/wallet_list.html',{"wallets":wallets})


def list_account(request):
    accounts= Account.objects.all()
    return render(request,'wallet/account_list.html',{"accounts":accounts})

def list_transaction(request):
    transactions= Transaction.objects.all()
    return render(request,'wallet/transaction_list.html',{"transactions":transactions})


def list_card(request):
    cards= Card.objects.all()
    return render(request,'wallet/card_list.html',{"cards":cards})


def list_thirdparty(request):
    thirdpartys= Thirdparty.objects.all()
    return render(request,'wallet/thirdparty_list.html',{"thirdpartys":thirdpartys})

def list_notification(request):
    notifications= Notification.objects.all()
    return render(request,'wallet/notification_list.html',{"notifications":notifications})

def list_receipt(request):
    receipts= Receipt.objects.all()
    return render(request,'wallet/receipt_list.html',{"receipts":receipts})

def list_loan(request):
    loans= Loan.objects.all()
    return render(request,'wallet/loan_list.html',{"loans":loans})

def list_reward(request):
    rewards= Reward.objects.all()
    return render(request,'wallet/reward_list.html',{"rewards":rewards})



    


