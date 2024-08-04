import os
from time import time

YES_NO_MAYBE = {
    0: 'no',
    1: 'yes',
    9: 'maybe',
}

COMMON_IMAGE_URL = os.path.join('static', 'images')

YES_NO_MAYBE_LOCAL_URLS = {
    'no': os.path.join(COMMON_IMAGE_URL, 'no.gif'),
    'yes': os.path.join(COMMON_IMAGE_URL, 'yes.gif'),
    'maybe': os.path.join(COMMON_IMAGE_URL, 'maybe.gif'),
}


def generate_answer() -> dict[str, str]:
    answer = get_yes_or_no_locally()
    url = YES_NO_MAYBE_LOCAL_URLS[answer]
    return {
        'answer': answer,
        'image': url,
    }


def get_yes_or_no_locally(use_maybe=True) -> str:
    t = time()

    if use_maybe and int(t % 10) == 9:
        answer = YES_NO_MAYBE[int(t % 10)]
    else:
        answer = YES_NO_MAYBE[int(t % 2)]
    return answer
