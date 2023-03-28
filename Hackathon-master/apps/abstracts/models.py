from typing import Optional

from django.db import models
from django.utils import timezone
from django.db.models import QuerySet


class AbstractQuerySet(models.QuerySet):
    """Pre-setup QuerySet for AbstractManager."""

    def delete(self, *args, **kwargs) -> None:
        self.update(
            datetime_deleted=timezone.now()
        )


class AbstractManager(models.Manager):
    """Manager for AbstractModel class."""

    def get_not_deleted(self) -> QuerySet:
        return self.filter(
            datetime_deleted__isnull=True
        )

    def get_deleted(self) -> QuerySet:
        return self.filter(
            datetime_deleted__isnull=False
        )

    def get_queryset(self) -> QuerySet['AbstractQuerySet']:
        return AbstractQuerySet(
            self.model,
            using=self._db
        )

    def get_by_id_or_none(self, id: int) -> Optional[object]:
        try:
            return self.get(id=id)
        except:
            return None

    


class AbstractModel(models.Model):
    """Abstract model.
    
    For desription all custom models."""

    datetime_created = models.DateTimeField(
        verbose_name="время создание",
        auto_now_add=True
    )
    datetime_updated = models.DateTimeField(
        verbose_name="время обновления",
        auto_now=True
    )
    datetime_deleted = models.DateTimeField(
        verbose_name="время удаления",
        null=True,
        blank=True
    )
    objects = AbstractManager()

    class Meta:
        abstract = True
