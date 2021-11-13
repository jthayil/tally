from django.db import models


class Drs(models.Model):
    pickup = models.DateField(null=True, blank=True)
    vehical_No = models.CharField(max_length=8, null=True, blank=True)
    party_Name = models.CharField(max_length=250, null=True, blank=True)
    container_No = models.CharField(max_length=250, null=True, blank=True)
    size = models.CharField(max_length=250, null=True, blank=True)
    from_One = models.CharField(max_length=250, null=True, blank=True)
    uploading = models.CharField(max_length=250, null=True, blank=True)
    to_One = models.CharField(max_length=250, null=True, blank=True)
    to_Two = models.CharField(max_length=250, null=True, blank=True)
    bill_No = models.CharField(max_length=250, null=True, blank=True)
    bill_Amt = models.PositiveBigIntegerField(null=True, blank=True)
    advance = models.PositiveBigIntegerField(null=True, blank=True)
    balance = models.PositiveBigIntegerField(null=True, blank=True)
    detain_Day = models.CharField(max_length=250, null=True, blank=True)
    remark = models.CharField(max_length=250, null=True, blank=True)
    inserted_On = models.DateTimeField(auto_now_add=True)
    updated_On = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.party_Name

    class Meta:
        verbose_name = "DRS"
        verbose_name_plural = "DRS Report"
        ordering = ["-id"]
