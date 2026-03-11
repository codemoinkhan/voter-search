from django.db import models


class Location(models.Model):

    district = models.CharField(max_length=200)
    block = models.CharField(max_length=200)

    gram_panchayat = models.CharField(max_length=200)
    ward = models.CharField(max_length=50)

    village = models.CharField(max_length=200)

    polling_station = models.CharField(max_length=200)
    polling_booth = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.village} - Ward {self.ward}"


class Voter(models.Model):

    serial_number = models.IntegerField()
    house_number = models.CharField(max_length=50)
    name_hindi = models.CharField(max_length=200)
    voter_id = models.CharField(max_length=20) #unique=True
    father_name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="voters"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["name_hindi"]),
        ]

    def __str__(self):
        return self.name_hindi