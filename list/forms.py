from django import forms
from django.core.exceptions import ValidationError
from django.contrib.admin import widgets
from list.models import Item,List
from datetimewidget.widgets import DateTimeWidget

EMPTY_ITEM_ERROR = "You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You've already got this in your list"

EMPTY_LIST_ERROR = "You can't have an empty list name"
DUPLICATE_LIST_ERROR = "You've already got this in your lists"
class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item
        fields = ('text', 'item_goal_date',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': '事项内容',
                'class': 'form-control input-lg',
            }),

            'item_goal_date':DateTimeWidget(attrs={'id': 'datetimeid','placeholder': '提醒日期',},
                usel10n = True, bootstrap_version = 3
            ),
        }
        error_messages = {
            'item_name': {'required': EMPTY_ITEM_ERROR},
            'text': {'required': EMPTY_ITEM_ERROR}
        }

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)

    def save(self, for_list):
        self.instance.list = for_list
        return super().save()


class ExistingListItemForm(ItemForm):

    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.list = for_list

    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {'text': [DUPLICATE_ITEM_ERROR]}
            self._update_errors(e)

    def save(self):
        return forms.models.ModelForm.save(self)








class ListForm(forms.models.ModelForm):
    class Meta:
        model = List
        fields = ('list_name', )
        widgets = {
            'list_name': forms.fields.TextInput(attrs={
                'placeholder': '清单名字',
                'class': 'form-control input-lg',
            }),
        }
        error_messages = {
            'list_name': {'required': EMPTY_LIST_ERROR},
        }
    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
    def save(self, for_user):
        self.instance.user = for_user
        return super().save()


class ExistingUserListForm(ListForm):

    def __init__(self, for_user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.user = for_user

    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {'list_name': [DUPLICATE_LIST_ERROR]}
            self._update_errors(e)

    def save(self):
        return forms.models.ModelForm.save(self)

