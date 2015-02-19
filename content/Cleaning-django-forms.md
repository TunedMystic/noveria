Title: Cleaning django forms
Date: 2015-02-18 02:03
Category: Django
Tags: django, python, web, forms
Slug: cleaning-django-forms
Authors: Sandeep Jadoonanan
Summary: How to implement your own form-cleaning methods.

A quick example of working with forms (ModelForms) in Django. In this example, I have a simple Snippet model. Snippets have a unique url, can be made by logged-in or anonymous Users and can be publicly visible or private.

## My model
`models.py`:

    :::python
    class Snippet(models.Model):
      # This model describes the data of a 'Snippet'.
      # A Snippet can hold any supported code/text.
      PRIVACY_CHOICES = (
        ("private", "Private"),
        ("public", "Public"),
      )
      PRIVACY_DEFAULT = PRIVACY_CHOICES[1][0]

      # Title of the Snippet.
      title = models.CharField(max_length = 50, default = "Untitled", blank = True)
      # The content of the Snippet.
      content = models.TextField(blank = False)
      # The (programming) language the Snippet is written in.
      language = models.CharField(max_length = 20, default = "text", blank= False)
      # Will the Snippet be public or private?
      visibility = models.CharField(max_length = 20, choices = PRIVACY_CHOICES, default = PRIVACY_DEFAULT, blank = False)
      # The password for the (private) Snippet.
      password = models.CharField(max_length = 40, blank = True)
      # The User that wrote the snippet. (Can be an Anonyous user).
      author = models.ForeignKey(settings.AUTH_USER_MODEL, blank = True, null = True)
      # Uniquely generated hash for the Snippet.
      url_code = models.CharField(max_length = 80, unique = True, blank = False)
      # The tags associated with the Snippet (via django-taggit).
      tags = TaggableManager(blank = True)
      # The date the Snippet was posted.
      date_added = models.DateTimeField(auto_now_add = True)


So with that out of the way, I want to create Snippets through a form. Django makes this really easy by providing a ModelForm. All I have to do is include the model (Snippet) in my form's Meta class and thats pretty much it. But here I want some added functionality with my snippet form. I want to check certain fields to see if they contain valid data. This is known as 'cleaning the fields'. To clean a certain field, I have to define a function **clean_(field_name)**, where *field_name* is the actual name of my model field. For example, if i wanted to clean the **language** field in my Snippet model, I would define the function **def clean_language(...)** in my form. You can see a proper example below.

## My form 
`forms.py`:

    :::python
    class SnippetForm(forms.ModelForm):

      MAX_TAGS = 10

      class Meta:
        model = Snippet
        exclude = ["author", "date_added_raw", "url_code"]

      def clean_title(self, *args, **kwargs):
        # Checks is the title is an empty string.
        # If it is, then change it to 'Untitled'.
        data = self.cleaned_data.get("title", None)
        if not data:
          return "Untitled"

      def clean_tags(self, *args, **kwargs):
        # Checks if the number of tags is within the allowed limit.
        data = self.cleaned_data.get("tags", None)
        # Do the number of tags exceed the maximum?
        if len(data) > MAX_TAGS:
          raise forms.ValidationError("Maximum of %s tags allowed per Snippet." %(MAX_TAGS))

        # Turn all tags into lower case.
        data = [tag.lower() for tag in data]
        return data

      def clean(self, *args, **kwargs):
        # If visibility is private, Snippet must gave a password.
        cleaned_data = super(SnippetForm, self).clean(*args, **kwargs)
        # Private snippets must contain a password.
        if (cleaned_data.get("visibility", None) == "private") and (cleaned_data.get("password", None) == ""):
          raise forms.ValidationError("You must provide a password for private Snippets.")

As you can see here, I also defined a **clean(...)** function. According to the Django [docs](https://docs.djangoproject.com/en/1.7/ref/forms/validation/#form-and-field-validation), you must define the **clean_(field_name)** when you need to validate that specific field, and you must implement **clean(...)** when you need field validation that depends on other fields (ex. making sure two emails match, etc).
