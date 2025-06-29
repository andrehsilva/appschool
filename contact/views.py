from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada com sucesso!")
            return redirect('contact')  # Redireciona para a mesma página
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})

