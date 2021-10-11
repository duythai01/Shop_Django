from rest_framework.serializers import ModelSerializer

from user.models import CustomerUser


class CustomerUserSerializer(ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ['id', 'first_name', 'last_name',
                  'username', 'password', 'email', 'phone_number', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = CustomerUser(**validated_data)
        user.set_password(user.password)
        user.save()

        return user
