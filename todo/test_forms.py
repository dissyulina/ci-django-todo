from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        # check whether the form is not valid
        self.assertFalse(form.is_valid())
        # check whether there's a name key in the dictionary of form errors
        self.assertIn('name', form.errors.keys())
        # check whether the error msg on the name field is :'This field is required.'
        self.assertEqual(form.errors['name'][0], 'This field is required.')
    
    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())
    
    # test to ensure that the only fields that are displyaed in the form are the name and done fields
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
    