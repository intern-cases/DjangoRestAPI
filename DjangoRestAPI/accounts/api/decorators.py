from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def company_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME,
                     login_url='/accounts/login/?next=/companies/'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_company,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def dealer_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME,
                    login_url='/accounts/login/?next=/dealers/'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_dealer,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )

    if function:
        return actual_decorator(function)

    return actual_decorator


def customer_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME,
                      login_url='/accounts/login/'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_customer,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


# def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/accounts/login/?next=/admin/'):
#     actual_decorator = user_passes_test(
#         lambda u: u.is_active and u.is_superuser,
#         login_url=login_url,
#         redirect_field_name=redirect_field_name
#     )
#
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
