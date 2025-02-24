from django.db import models, transaction

class AutoIncMixin(models.Model):
    """
    Abstract model for generating an auto-incrementing field with leading zeros.
    Works for any field name specified in `AUTO_INC_FIELD`.
    """

    class Meta:
        abstract = True  # Prevents Django from creating a table for this mixin

    AUTO_INC_FIELD = None  # Define this in child classes

    def save(self, *args, **kwargs):
        if self.AUTO_INC_FIELD is None:
            raise ValueError(f"{self.__class__.__name__} must define AUTO_INC_FIELD")

        field_name = self.AUTO_INC_FIELD
        field_value = getattr(self, field_name)

        if not field_value:  # Generate only if the field is empty
            with transaction.atomic():
                last_record = self.__class__.objects.order_by("-id").first()
                next_code = int(getattr(last_record, field_name)) + 1 if last_record and getattr(last_record, field_name).isdigit() else 1
                setattr(self, field_name, f"{next_code:06d}")  # Format as "000001", "000002"

        super().save(*args, **kwargs)

# Create your models here.
class SalaryScale (AutoIncMixin,models.Model):
    SAL_GRADE_CODE = models.CharField(unique=True, primary_key=True, max_length=6)
    SAL_GRADE_NAME = models.TextField()
    AUTO_INC_FIELD = "SAL_GRADE_CODE"

    def __str__(self):
        return f"{self.category_code} - {self.name}"


class Designation (AutoIncMixin,models.Model):
    DSG_CODE = models.CharField(unique=True, primary_key=True, max_length=6)
    DSG_NAME = models.TextField()
    SAL_GRADE_CODE = models.ForeignKey(SalaryScale, on_delete=models.CASCADE, null=True)
    AUTO_INC_FIELD = "DSG_CODE"

    def __str__(self):
        return f"{self.category_code} - {self.name}"


class Employee (models.Model):
    EMP_NUMBER = models.CharField(unique=True, primary_key=True, max_length=6)
    EMP_FIRSTNAME = models.TextField()
    EMP_LASTNAME = models.TextField()
    EMP_BIRTHDAY = models.DateField()
    EMP_DATE_JOINED = models.DateField()
    DSG_CODE = models.ForeignKey(Designation, on_delete=models.CASCADE, null= True)
    AUTO_INC_FIELD = "EMP_NUMBER"

    def __str__(self):
        return f"{self.category_code} - {self.name}"