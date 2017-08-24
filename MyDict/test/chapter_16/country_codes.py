from pygal.i18n import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    # ## 返回臀的便是特定国家的国家代码。
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.
    # ## 如果这个国家没有发现,还没有。
    return None
