class ListingTextsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['club'].required = True
        self.fields['club'].label = "Отбор"
        self.fields['club'].widget.attrs.update({
            'placeholder': "Въведи името на отбора...",
            'class': 'wide-input'
        })
        self.fields['club'].error_messages = {
            'required': 'Полето "Отбор" е задължително.',
            'invalid': 'Въведете валидно име за отбора.'
        }

        self.fields['experience_needed'].label = "Необходими години опит "
        self.fields['experience_needed'].widget.attrs.update({
            'placeholder': "пример: 2",
            'class': 'wide-input'
        })
        self.fields['experience_needed'].error_messages = {
            'invalid': 'Въведете валидно число за години опит.'
        }

        self.fields['licence_required'].required = True
        self.fields['licence_required'].label = "Необходим лиценз"
        self.fields['licence_required'].widget.attrs.update({
            'class': 'wide-input'
        })
        self.fields['licence_required'].error_messages = {
            'required': 'Изберете необходим лиценз.',
            'invalid': 'Невалиден лиценз.'
        }

        self.fields['for_age_group'].label = "За възрастова група "
        self.fields['for_age_group'].widget.attrs.update({
            'class': 'wide-input'
        })
        self.fields['for_age_group'].error_messages = {
            'required': 'Полето "За възрастова група" е задължително.'
        }

        self.fields['salary'].label = "Заплата "
        self.fields['salary'].widget.attrs.update({
            'placeholder': "Въведи заплата....",
            'class': 'wide-input'
        })
        self.fields['salary'].error_messages = {
            'invalid': 'Въведете валидно число за заплата.',
            'min_value': 'Заплатата трябва да бъде по-голяма от 0.'
        }

        self.fields['telephone_number'].required = True
        self.fields['telephone_number'].label = "Телефон"
        self.fields['telephone_number'].widget.attrs.update({
            'placeholder': "Въведи телефонен за контакт....",
            'class': 'wide-input'
        })
        self.fields['telephone_number'].error_messages ={
            'required':'Полето "Телефон" е задължително.'
        }

        self.fields['contact_person'].required = True
        self.fields['contact_person'].label = "Лице за контакт"
        self.fields['contact_person'].widget.attrs.update({
            'placeholder': "Въведи лице за контант....",
            'class': 'wide-input'
        })
        self.fields['contact_person'].error_messages = {
            'required': 'Полето "Лице за контакт" е задължително.',
            'invalid': 'Полете "Лице за контакт" е невалидно.'
        }

        self.fields['position'].label = "Позиция на лице за контакт "
        self.fields['position'].widget.attrs.update({
            'placeholder': "пример: администратор....",
            'class': 'wide-input'
        })


