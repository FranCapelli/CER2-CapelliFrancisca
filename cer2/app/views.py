from django.shortcuts import render
from app.models import entidad,comunicado
from django.db.models import Q

# Create your views here.
def inicio(request):
    dataCom = comunicado.objects.all()
    dataEnt = entidad.objects.all()
    
    buscar=request.GET.get("filter")
    if buscar:
        dataCom=comunicado.objects.filter(Q(entidad=buscar)).distinct()
    context = {'dataEnt': dataEnt,
               'dataCom': dataCom}
    
    return render(request, "app/inicio.html",context)




