from django.contrib.auth import authenticate
from drf_registration.utils.socials import enable_has_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from .models import CustomerUser

from drf_registration.settings import drfr_settings
from drf_registration.utils.common import import_string, import_string_list
from drf_registration.utils.users import (
    get_user_model,
    get_user_profile_data,
    has_user_verified,
    set_user_verified, get_all_users,
)
from drf_registration.utils import socials
from drf_registration.exceptions import (
    NotActivated,
    LoginFailed,
    InvalidProvider,
    MissingEmail,
    InvalidAccessToken,
)


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """

    if 'email' in drfr_settings.USER_FIELDS:
        email = serializers.EmailField(
            validators=[UniqueValidator(queryset=get_all_users(), message=('User with this email already exists.'))]
        )

    if 'username' in drfr_settings.USER_FIELDS:
        username = serializers.CharField(validators=[UniqueValidator(
            queryset=get_all_users(),
            message=('User with this username already exists.')
        )])

    if enable_has_password():
        has_password = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()

        # Check to reponse has password field in the case enable
        # Facebook or Google login

        fields = drfr_settings.USER_FIELDS + \
                 ('has_password',) if enable_has_password() else drfr_settings.USER_FIELDS
        read_only_fields = drfr_settings.USER_READ_ONLY_FIELDS
        extra_kwargs = {'password': {'write_only': True}}

    def get_has_password(self, user):
        """
        Custom reponse field to check user has password or not
        """
        return True if user.password else False


#
# class CustomerUserSerializer(ModelSerializer):
#     class Meta:
#         model = CustomerUser
#         fields = ['id', 'first_name', 'last_name',
#                   'username', 'password', 'email', 'phone_number', 'date_joined']
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }
#         # if CustomerUser.objects.filter(username=username)
#
#     def create(self, validated_data):
#         user = CustomerUser(**validated_data)
#         user.set_password(user.password)
#         user.save()
#
#         return user

# Login
class LoginSerializer(serializers.ModelSerializer):
    """
    User login serializer
    """

    # username = serializers.CharField()
    # password = serializers.CharField()

    class Meta:
        model = CustomerUser
        fields = ('username', 'password')

    def validate(self, data):
        user = authenticate(**data)
        if user:

            # Check user is activated or not
            if has_user_verified(user):
                # added user model to OrderedDict that serializer is validating
                data['user'] = user

                return data
            raise NotActivated()
        raise LoginFailed()
