from django.contrib.auth.decorators import user_passes_test

def is_staff(user):
    return user.is_staff

staff_member_required = user_passes_test(is_staff)
