from django.db import models
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

from core.utils import unique_slug_generator


class MobileBrand(models.Model):
    """Represents the mobile manufacturers"""
    name            = models.CharField(_("Name"), max_length=50)
    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse("mobile_detail", kwargs={"slug": self.name})

#TODO make sure the image is deleted on deleting the record
class Mobile(models.Model):
    name                    = models.CharField(_("name"), max_length=50)
    # full name will be Brand name + name
    full_name               = models.CharField(_("Full Name"), max_length=50, 
                                  blank=True, null=True)
    brand                   = models.ForeignKey('MobileBrand', 
                                  verbose_name=_("Brand"),
                                  related_name=_("mobiles"),
                                  on_delete=models.SET_NULL, 
                                  null=True, blank=True)
    cash_price              = models.FloatField(_("Cash Price"), 
                                  blank=True, null=True)    
    slug                    = models.SlugField(_("slug"), unique=True,
                                  blank=True, null=True)
    image                   = models.ImageField(_("Image"), upload_to='mobiles/',
                                  blank=True, null=True)
    # url for the mobile on a website for further details of the mobile                              
    url                     = models.URLField("Url", blank=True, null=True)

    class Meta:
        unique_together = (
            ('name', 'brand')
        )
    def __str__(self):
        if self.full_name:
            return self.full_name
        return self.name
    def get_absolute_url(self):
        return reverse("mobiles:mobile-detail", kwargs={"slug": self.slug})


class MobileTechnicalSpecification(models.Model):
    mobile                      = models.ForeignKey("Mobile", 
                                  on_delete=models.CASCADE)
    two_g                       = models.BooleanField(blank=True, null=True)
    three_g                     = models.BooleanField(blank=True, null=True) 
    four_g                      = models.BooleanField(blank=True, null=True)
    five_g                      = models.BooleanField(blank=True, null=True)
    WiFi                        = models.BooleanField(blank=True, null=True)
    dual_sim                    = models.BooleanField(blank=True, null=True)
    dimensions                  = models.CharField(_("Dimensions"), 
                                  max_length=50, blank=True, null=True)
    weight                      = models.CharField(_("Weight"), 
                                  max_length=50, blank=True, null=True)
    screen_type                 = models.CharField(_("Screen Type"), 
                                  max_length=50, blank=True, null=True)
    screen_size                 = models.CharField(_("Screen Size"), 
                                  max_length=50, blank=True, null=True)
    screen_resolution           = models.CharField(_("Screen Resolution"), 
                                  max_length=50, blank=True, null=True)
    ip_certification            = models.CharField(_("IP Certification"), 
                                  max_length=50, blank=True, null=True)
    internal_storage            = models.CharField(_("Internal Storage"), 
                                  max_length=50, blank=True, null=True)
    external_storage            = models.CharField(_("External Storage"), 
                                  max_length=50, blank=True, null=True)
    WLAN                        = models.CharField(_("WLAN"), 
                                  max_length=50, blank=True, null=True)
    bluetooth                   = models.CharField(_("Bluetooth"), 
                                  max_length=50, blank=True, null=True)
    NFC                         = models.BooleanField(default=False)
    USB                         = models.CharField(_("USB"), 
                                  max_length=50, blank=True, null=True)
    wireless_charging           = models.CharField(_("Wireless Charging"), 
                                  max_length=50, blank=True, null=True)
    fast_charging               = models.CharField(_("Fast Charging"), 
                                  max_length=50, blank=True, null=True)
    chipset                     = models.CharField(_("Chipset"), 
                                  max_length=50, blank=True, null=True)
    operating_system            = models.CharField(_("Operating System"), 
                                  max_length=50, blank=True, null=True)
    ram                         = models.CharField(_("RAM"), 
                                  max_length=50, blank=True, null=True)

    def __str__(self):
        return self.mobile.name


class MobileCameraSpecification(models.Model):
    mobile                      = models.ForeignKey("Mobile", 
                                  on_delete=models.CASCADE)
    rear_cam_lenses             = models.IntegerField(_("rear_camera_lenses"), 
                                  blank=True, null=True)
    rear_cam_megapixel          = models.CharField(_("rear_camera_megapixel"), 
                                  max_length=255, blank=True, null=True)
    back_cam_aperture           = models.CharField(_("Rear Camera Aperture"), 
                                  max_length=30, blank=True, null=True)
    rear_cam_video_resolution   = models.CharField(_("rear_camera_video_resolution"), 
                                  max_length=30, blank=True, null=True)
    front_cam_lenses            = models.IntegerField(_("front_camera_lenses"),
                                  blank=True, null=True)
    front_cam_megapixel         = models.CharField(_("front_camera_megapixel"), 
                                  max_length=255, blank=True, null=True)
    front_cam_aperture          = models.CharField(_("front_camera_aperture"), 
                                  max_length=30, blank=True, null=True)
    front_cam_video_resolution  = models.CharField(_("front_camera_video_resolution"), 
                                  max_length=30, blank=True, null=True) 

    def __str__(self):
        return self.mobile.name


class Variation(models.Model):
    """Store different variations of a mobile device. e.g. 
       Variation on color, memory. Price is dependent on variation
       """
    name            = models.CharField(_("Name"), max_length=50)
    mobile          = models.ForeignKey("Mobile", on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ('name', 'mobile')
        )
    def __str__(self):
        return self.name


class MobileVariation(models.Model):
    """Store the actual values for each variation. e.g. Color of a 
    mobile can be blue, red, green. Memory can be 32, 64, 128."""
    variation   = models.ForeignKey(Variation, on_delete=models.CASCADE)
    value       = models.CharField(_("value"), max_length=50)  # S, M, L
    # attachment = models.ImageField(blank=True)

    class Meta:
        unique_together = (
            ('variation', 'value')
        )
    def __str__(self):
        return self.value


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance=instance)

pre_save.connect(pre_save_receiver, sender=Mobile)
