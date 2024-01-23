from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import Randevu
import requests
import re







# en son bunu yaparken yarim kaldik cunku olmadi amac basedeki tarih bilgilerini cekmekti suan bence aliyorum ama bilgiyi goremedim
# urlsinide gectim url kismini unutma eger silersen
def selecteddate(request):
    veriler = Randevu.objects.all()
    return render(request, 'field/appointment.html', {'veriler': veriler})









def send_info(request): 
    chat_id = "-4037923003" 
    bot_id = "6334160779:AAEE0b-fSGxtxFI3jdZwwWWDRixvkCjmZrA" 
    
    
    
     
    if request.method == 'POST':
            
        
        number = request.POST.get('number')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        date= request.POST.get('selectedDateInput')
        tm1=date.replace("-", ".").replace("T", '\n').replace(":00Z", "")
        tm2=date.replace("-", ".").replace("T", "  ").replace(":00Z", "")
        
        submit= request.POST.get('submit')
        reset=request.POST.get('reset')
       
        if date is not None and number is not None and name is not None and surname is not None and not Randevu.objects.filter(tarih=tm2).exists():
                newdata = Randevu(tarih=tm2, numara=number, isim=name, soyisim=surname)
                newdata.save()  
                send = requests.get( 
                            f'https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text='+'SAHA1 '+'\n' + str( 
                                tm1)+'\n' +str(number)+'\n' +str( name)+'\n' +str( surname)
                            
                            )
                
                
                            
                if send.status_code > 299: 
                        print('TELEGRAM_ALARM_PUSH_ERROR: ', send.text)
                return render (request, 'field/appointment.html')
            
        else:
            
            return render (request, 'field/appointment.html')
            
 
 
    else:
        
        return render (request, 'field/appointment.html')
    
   
   
    
    
    
def send_info1(request): 
    chat_id = "-4037923003" 
    bot_id = "6334160779:AAEE0b-fSGxtxFI3jdZwwWWDRixvkCjmZrA" 
    
    
    
     
    if request.method == 'POST':
        
        
        number = request.POST.get('number1')
        name = request.POST.get('name1')
        surname = request.POST.get('surname1')
        date= request.POST.get('selectedDateInput1')
        tm1=date.replace("-", ".").replace("T", '\n').replace(":00Z", "")
        tm2=date.replace("-", ".").replace("T", "  ").replace(":00Z", "")
        submit= request.POST.get('submit1')
        reset=request.POST.get('reset1')
       
        if date is not None and number is not None and name is not None and surname is not None and not Randevu.objects.filter(tarih=tm2).exists():
                newdata = Randevu(tarih=tm2, numara=number, isim=name, soyisim=surname)
                newdata.save()  
                send = requests.get( 
                            f'https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text=' +'SAHA 2'+'\n'+ str( 
                                tm1)+'\n' +str(number)+'\n' +str( name)+'\n' +str( surname)
                            
                            )
                            
                if send.status_code > 299: 
                        print('TELEGRAM_ALARM_PUSH_ERROR: ', send.text)
                return render (request, 'field/appointment.html')
            
        else:
            
            return render (request, 'field/appointment.html')
            
 
 
    else:
        
        return render (request, 'field/appointment.html')
    
    
    
    
    
    
#code of bot
def send_message(request): 
    chat_id = "-4037923003" 
    bot_id = "6334160779:AAEE0b-fSGxtxFI3jdZwwWWDRixvkCjmZrA" 
     
    if request.method == 'POST':
        wishes = request.POST.get('wishes')
        send = requests.get( 
                    f'https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text=' + str( 
                        wishes) + str())
        if send.status_code > 299: 
                print('TELEGRAM_ALARM_PUSH_ERROR: ', send.text)
        return render (request, 'field/index.html')
 
 
    else:
        return render (request, 'field/index.html')


def index(request): 
    return render (request, 'field/index.html')
    #rendering usage 
    #While rendering, it enters all applications. In this case, if it reaches the index.html folder of another application, it can run it too.
    #In order to prevent this situation, we created a field file in the template and put our html folder in this file.
    #write the name of path
   
   # return HttpResponse("home page")

def services(request):
    return render(request, 'field/services.html')


def subscription(request):
    return render(request, 'field/subscription.html' )



def appointment(request):
    return render(request, 'field/appointment.html' )



def photos(request):
    return render(request, 'field/photos.html' )

def wedding(request):
    return render(request, 'field/wedding.html' )
