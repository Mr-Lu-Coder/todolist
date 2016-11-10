from django.db import models
from django.core.urlresolvers import reverse
from account.models import User, UserGroup

class List(models.Model):
    list_name = models.CharField(max_length=255, blank=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, blank=True, default=None)
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

    def __str__(self):
        return self.name


class Item(models.Model):
    item_name = models.CharField(max_length=255, default='', blank=True)
    text = models.CharField(max_length=255, default='')
    list = models.ForeignKey(List, default=None, blank=True)
    item_create_date = models.DateTimeField(blank=True, null=True)
    item_goal_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        # 唯一性约束会干扰排序
        ordering = ('id',)
        # 要求清单中的代办事项是唯一的，以后可能不需要
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text

