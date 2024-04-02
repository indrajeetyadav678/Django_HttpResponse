from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

# def landingpage(request):
#    return HttpResponse("this is the landing page ....");

# def ILOveyou(request):
#    a=5;
#    b=40;
#    return HttpResponse(a+b);
# def landingpage(request):
#    return render(request, 'home.html');

def landingpage(request):
   data1= {
         'name':'indrajeet',
         'lacture':'python',
         'active':True
      }
   
   return render(request, 'home.html',{"data":data1})

# def landingpage(request):
  
   
#    return redirect('https://colorlib.com/wp/portfolio-tag/free-templates/' )

# def landingpage(request):
#    data= [
#        {
#         'name':'indrajeet',
#         'lacture':'python',
#         'active':True
#        },
#        {
#         'name':'yes',
#         'lacture':'html',
#         'active':False
#        }
#       ]
   
#    return JsonResponse(data,)