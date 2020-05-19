from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetail(models.Model):
    """Holds the detail of any donor or acceptor."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.FileField(upload_to="photo", max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    mobile = models.IntegerField()
    address = models.TextField()

    class Meta:
        """Meta definition for UserDetail."""

        verbose_name = "User Detail"
        verbose_name_plural = "User Details"

    def __str__(self):
        """Unicode representation of UserDetail."""
        return self.name


class DonationRequest(models.Model):
    """Model definition for DonationRequest."""

    type_required = models.CharField(
        choices=(("O+", "O+"), ("O-", "O-"),), max_length=50
    )
    location = models.TextField(default=None, null=True, blank=True)

    class Meta:
        """Meta definition for DonationRequest."""

        verbose_name = "DonationRequest"
        verbose_name_plural = "DonationRequests"

    def __str__(self):
        """Unicode representation of DonationRequest."""
        return self.type_required + " | " + self.location


class Donation(models.Model):
    """Model definition for Donation."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    donation_for = models.ForeignKey(
        DonationRequest, on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        """Meta definition for Donation."""

        verbose_name = "Donation"
        verbose_name_plural = "Donations"

    def __str__(self):
        """Unicode representation of Donation."""
        return self.user.username
