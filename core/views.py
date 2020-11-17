from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


from .models import MobileBrand, TelecomCompany, Mobile
from telecompanies.spider import ThreeSpider, TelenorSpider, TeliaSpider
from telecompanies.models import Offer

class HomeView(View):
    def get(self, *args, **kwargs):
        context = {}
        return render(self.request, 'home.html', context)


class MobileManufacturersView(ListView):
    template_name = 'core/mobile_brands.html'
    queryset = MobileBrand.objects.all()
    # mobiles = Mobile.objects.all()
    # import pdb; pdb.set_trace()
    # for m in mobiles:
    #     m.full_name = m.brand.name + " " + m.name
    #     m.save()

class TelecomCompaniesView(ListView):
    template_name = 'core/telecom_companies.html'
    queryset = TelecomCompany.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TelecomCompaniesView, self).get_context_data(**kwargs)
        # TeliaSpider().get_telia_offers()
        offers = Offer.objects.all()
        context["offers"] = offers
        return context
    

def change_language(request):
    response = HttpResponseRedirect('/')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
                redirect_path = f'/{language}/'
            elif language == settings.LANGUAGE_CODE:
                redirect_path = '/'
            else:
                return response
            from django.utils import translation
            translation.activate(language)
            response = HttpResponseRedirect(redirect_path)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response