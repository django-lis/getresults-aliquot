from django.db import models


class AliquotConditionManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)
