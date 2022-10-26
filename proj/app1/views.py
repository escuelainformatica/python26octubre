from django.shortcuts import render

# Create your views here.
def pagina1(request):
    return render(request,"pagina1.html",
                  {
                      "num1":1,
                      "num2":2,
                      'nombre':'John Doe'
                      ,'paises':['chile','argentina','peru']
                  })

