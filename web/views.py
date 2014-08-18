from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from kumquat.utils import LoginRequiredMixin
from models import VHost, SSLCert, DefaultVHost
from forms import SSLCertForm

# VHost

class VHostList(LoginRequiredMixin, ListView):
	model = VHost

class VHostCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	model = VHost
	success_url = reverse_lazy('web_vhost_list')
	success_message = _("%(name)s was created successfully")

class VHostUpdate(LoginRequiredMixin, UpdateView):
	model = VHost
	#form_class = AccountUpdateForm
	fields = ['cert']
	success_url = reverse_lazy('web_vhost_list')

class VHostDelete(LoginRequiredMixin, DeleteView):
	model = VHost
	success_url = reverse_lazy('web_vhost_list')


# Default VHost

@require_POST
@login_required
def vhostCatchallSet(request, pk):
	v = get_object_or_404(VHost, pk = pk)
	DefaultVHost(vhost = v, domain = v.domain).save()
	return redirect('web_vhost_list')

@require_POST
@login_required
def vhostCatchallDelete(request, pk):
	get_object_or_404(DefaultVHost, pk = pk).delete()
	return redirect('web_vhost_list')


# SSL Certs

class SSLCertList(LoginRequiredMixin, ListView):
	model = SSLCert

@login_required
def sslcertCreate(request):
	form = SSLCertForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		c = SSLCert()
		c.set_cert(request.FILES['cert'].read(), request.FILES['key'].read(), request.FILES['ca'].read())
		c.save()
		messages.success(request, _("Successfull added"))
		return redirect('web_sslcert_list')
	return render(request, 'web/sslcert_form.html', {'form': form})

class SSLCertDelete(LoginRequiredMixin, DeleteView):
	model = SSLCert
	success_url = reverse_lazy('web_sslcert_list')
