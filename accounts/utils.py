import os
import json
from pathlib import Path
import pendulum
from dataHub.settings import BASE_DIR, PROJECT_ROOT
import pandas as pd
import random
import string
from django.utils.text import slugify


# Convert json file to dictionary
def json_to_dict(JSON):

    if Path(JSON).is_file():
        try:
            if Path(JSON).name.endswith('json'):
                with open(JSON) as file:
                    return json.load(file)

        except Exception as exc:
            formatted = "Unable to locate files! Please ensure you have provided accurate file paths. {}".format(
                repr(exc))
            raise Exception(formatted)

    else:
        raise Exception('Please pass a valid file path.')


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator_auth(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and an email character (char) field.
    """
    email_name = str(instance).split('@')[0]


    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(email_name)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
