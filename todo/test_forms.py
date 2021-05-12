from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    # Test that 'name' is a required field
    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})   # instantiate form with blank name field
        self.assertFalse(form.is_valid()) # Form is not expected to be valid
        self.assertIn('name', form.errors.keys()) # We expect that 'name' is a key in the dictionary of form errors
        self.assertEqual(form.errors['name'][0], 'This field is required.') # We expect that the first error msg for 'name' in form.errors dictionary is 'This field is required'


    def test_item_done_is_not_required(self): # Test name (name so easy to understand results)
        form = ItemForm({'name': 'Test with name only'}) # Instantiate a form with name value only (no value for 'done')
        self.assertTrue(form.is_valid()) # Expect that the form is still valid

    
    def test_fields_are_explicit_in_form_metaclass(self): # Test that form clearly identifies the fields to be displayed
        form = ItemForm() # Instantiate an empty form
        self.assertEqual(form.Meta.fields, ['name', 'done']) # Expect that the empty form has the two fields listed in meta