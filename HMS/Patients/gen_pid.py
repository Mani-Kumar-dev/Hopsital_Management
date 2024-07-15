import string
import random

def generate_id():
    starts_with = 'PAT'
    ends_with = ''.join(random.choices(string.digits,k=4))

    return f'{starts_with}{ends_with}'
