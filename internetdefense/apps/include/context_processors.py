from include.settings import INCLUDE_URL


def include_url(request):
    """
    Context processor that adds the value of the INCLUDE_URL setting to
    template contexts.

    INCLUDE_URL - The URL to the include code for the local environment.
    """
    return {
        'INCLUDE_URL': INCLUDE_URL
    }
