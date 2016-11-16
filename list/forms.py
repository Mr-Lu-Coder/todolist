from django import forms
from django.core.exceptions import ValidationError
from django.contrib.admin import widgets
from list.models import Item
from datetimewidget.widgets import DateTimeWidget

EMPTY_ITEM_ERROR = "You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You've already got this in your list"


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
        #self.fields['mydate'].widget = widgets.AdminDateWidget()
        #self.fields['mytime'].widget = widgets.AdminTimeWidget()
        #self.fields['item_goal_date'].widget = widgets.AdminSplitDateTime()

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

