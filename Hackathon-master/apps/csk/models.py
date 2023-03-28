from django.db import models

from auths.models import CustomUser

from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)


class UserCall(models.Model):
    """Call model for Users."""

    caller = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='заказчик'
    )
    personal_account = models.IntegerField()
    problem = models.TextField(
        verbose_name='причина обращения'
    )
    master_id = models.ForeignKey(
        'MasterUser',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='master_id'
    )
    datetime_created = models.DateTimeField(
        verbose_name="время создание",
        auto_now_add=True
    )

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = 'обращение'
        verbose_name_plural = 'обращения'


# class AdminCall(models.Model):
#     """Call model for Admin."""

#     user_call = models.ForeignKey(
#         UserCall,
#         on_delete=models.CASCADE
#     )
#     service_type = models.ForeignKey(
#         'Service',
#         on_delete=models.CASCADE
#     )

#     class Meta:
#         ordering = ('-datetime_created',)
#         verbose_name = 'обращение'
#         verbose_name_plural = 'обращения'


class ServiceType(models.IntegerChoices):
    ELECTRIC = 1, 'Электрик'
    SANTECHNIK = 2, 'Сантехник'
    INZHENER = 3, 'Инженер'
    ZHIL_KOMM_SLUJBA = 4, 'Жилые и коммунальные службы'
    ARCHITECTOR_DESIGNER = 5, 'Архитектор/Дизайнер'
    YURIST = 6, 'Юрист'
    OTHER = 7, 'Прочее'


class Service(models.Model):
    status_points = models.IntegerField(default=ServiceType.OTHER, choices=ServiceType.choices)


class StatusType(models.IntegerChoices):
    EMERGENCY = 1, 'Срочный запрос'
    IN_PROCESS = 2, 'Запрос в процессе'
    DONE = 3, 'Запрос осуществлен'
    DECLINED = 4, 'Запрос отклонен'


class Status(models.Model):
    status_points = models.IntegerField(default=StatusType.IN_PROCESS, choices=StatusType.choices)

class MasterUser(CustomUser):
    """MasterUser model."""

    service_master = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )

    avg_rating = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
    )

    ratings = models.ManyToManyField(
        'Rating',
        through='MasterUserRating',
        through_fields=('master_user', 'rating')
    )

    is_busy = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = 'мастер'
        verbose_name_plural = 'мастера'


class RatingType(models.IntegerChoices):
    VERY_LOW = 1, 'Очень низко'
    LOW = 2, 'Низко'
    MID = 3, 'Средне'
    GOOD = 4, 'Хорошо'
    GREAT = 5, 'Прекрасно'

    
class Rating(models.Model):
    rating_points = models.IntegerField(default=RatingType.VERY_LOW, choices=RatingType.choices)


class MasterUserRating(models.Model):
    master_user = models.ForeignKey(
        MasterUser,
        on_delete=models.CASCADE
    )
    rating = models.ForeignKey(
        Rating,
        on_delete=models.CASCADE
    )

    
