from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket


from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


from apps.empleados.models import Empleado


def ingresar(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard/')
    formulario = AuthenticationForm
    if request.method == 'POST':
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    empleado = Empleado.objects.filter(usuario__id=request.user.id)
                    print('******')
                    if empleado.exists():
                        print(empleado[0].categoria)
                        request.session['categoria'] = empleado[0].categoria
                        request.session['id_usuario'] = request.user.id

                    else:
                        print('******')
                        return HttpResponseRedirect('/noempleado/')
                    return HttpResponseRedirect('/dashboard/')
                else:
                    return render(request, 'noactivo.html')
            else:
                return render(request, 'noesusuario')
        else:
            return render(request, 'login.html', {'form': formulario})

    return render(request, 'login.html', {'form': formulario})


class Dashboard(LoginRequiredMixin, TemplateView):

    template_name = 'dashboard.html'


class NoEmpleado(LoginRequiredMixin, TemplateView):

    template_name = 'NoEmpleado.html'


def cerrar(request):

    logout(request)
    return HttpResponseRedirect('/')


#server = SimpleWebSocketServer('', 8000, SimpleEcho)
#server.serveforever()

class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client
        self.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')