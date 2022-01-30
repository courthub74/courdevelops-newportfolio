from django import template
from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate
	)

from django.views import generic


from . forms import ContactForm

#IndexView
class IndexView(generic.TemplateView):
    template_name = "portfolioapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        testimonals = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        context["testimonials"] = testimonals 
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        return context
		
#ContatctView		
class ContatctView(generic.FormView):
    template_name = "portfolio/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Thank you! Will be in touch soon.")
        return super().form_valid(form)


#PortfolioView
class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "portfolioapp/portfolio.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

#PortfolioDetailView
class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "portfolioapp/portfolio-detail.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

#BlogView
class BlogView(generic.ListView):
    model = Blog
    template_name = "portfolioapp/blog.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

#BlogDetailView
class BlogDetailView(generic.DetailView):
    model  = Blog
    template_name = "portfolioapp/blog-detail.html"