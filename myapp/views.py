from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def home(request):
    # context = {}
    # context['login_success'] = user.is_authenticated()
    return render(request,'index.html')
    # return render(request,'index.html', context)
    # print()
    # message="id:%s, uasername:%s firstname:%s, lastname:%s"%(request.user.pk, request.user.username, request.user.first_name, request.user.last_name)
    # now = datetime.datetime.now()
    # html = "<html><body><p>It is now %s.</p><p>%s</p></body></html>" % (now,message)
    # return HttpResponse(html)

def contact(request):
    # context['login_success'] = False
    return render(request,'contact.html')

def detail_adaptor(request):
    return render(request,'detail_adaptor.html')

def detail_case_black(request):
    return render(request,'detail_case_black.html')

def detail_case_blue(request):
    return render(request,'detail_case_blue.html')

def detail_case_pink(request):
    return render(request,'detail_case_pink.html')

def detail_case_red(request):
    return render(request,'detail_case_red.html')

def detail_case_white(request):
    return render(request,'detail_case_white.html')

def detail_dock(request):
    return render(request,'detail_dock.html')

def detail_fabric(request):
    return render(request,'detail_fabric.html')

def detail_inhaler(request):
    return render(request,'detail_inhaler.html')

def detail_kit_black(request):
    return render(request,'detail_kit_black.html')

def detail_kit_white(request):
    return render(request,'detail_kit_white.html')

def detail_oil(request):
    return render(request,'detail_oil.html')

def detail_tool(request):
    return render(request,'detail_tool.html')

def detail_usb(request):
    return render(request,'detail_usb.html')

def faq(request):
    return render(request,'faq.html')

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def payment(request):
    return render(request,'payment.html')

def shop(request):
    return render(request,'shop.html')

def shop_accessories(request):
    return render(request,'shop_accessories.html')

def shop_filler(request):
    return render(request,'shop_filler.html')

def shop_promotion(request):
    return render(request,'shop_promotion.html')

def success(request):
    return render(request,'success.html')

def track(request):
    return render(request,'track.html')

def shop_device(request):
    return render(request,'shop_device.html')
