from django.db import models
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _


from core.models import TelecomCompany, Mobile
from core.utils import unique_slug_generator

class Offer(models.Model):
    mobile                  = models.ForeignKey(Mobile, 
                              verbose_name=_("Mobile"), 
                              on_delete=models.CASCADE, 
                              blank=True, null=True)
    telecom_company         = models.ForeignKey(TelecomCompany, 
                              verbose_name=_("Telecom Company"), 
                              on_delete=models.CASCADE)
    mobile_name             = models.CharField(_("Mobile Name"), 
                              max_length=50, blank=True, null=True)
    discount                = models.CharField(_("Discount"), max_length=50,
                              blank=True, null=True)
    # link to the company offer page
    offer_url               = models.URLField(_("Offer Url"), max_length=300,
                              blank=True, null=True)
    slug                    = models.SlugField(_("slug"), 
                              blank=True, null=True)
    class Meta:
        verbose_name = _("Offer")
        verbose_name_plural = _("Offers")

    def __str__(self):
        name = self.mobile_name
        if self.mobile:
            name = self.mobile.name
        if name != None:
            name = name + self.telecom_company.name
        else:
            name = self.telecom_company.name
        return name

    def get_absolute_url(self):
        return reverse("offer_detail", kwargs={"slug": self.slug})

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance=instance)

pre_save.connect(pre_save_receiver, sender=Offer)