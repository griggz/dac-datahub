from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)


class AuthSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='accounts:auth-detail',
        lookup_field='slug'
    )

    class Meta:
        model = User
        fields = [
            'email',
            'url',
            'first_name',
            'last_name',
        ]

        @staticmethod
        def create(validated_data):
            return User.objects.create(**validated_data)


class AuthSerializerDetail(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='accounts:auth-detail',
        lookup_field='slug'
    )

    class Meta:
        model = User
        fields = [
            'email',
            'url',
            'is_admin',
            'nickname',
            'first_name',
            'last_name',
            'slug'
        ]

        @staticmethod
        def create(validated_data):
            return User.objects.create(**validated_data)

    def get_staff(self, obj):
        request = self.context['request']
        if request.user:
            if request.user.is_staff:
                return True
            else:
                return False


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
                                     "input_type":   "password"})
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True, label="Confirm password")

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "password2",
            "first_name",
            "last_name",
            "meta"
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        meta = validated_data["meta"]
        if (email and User.objects.filter(email=email).exists()):
            raise serializers.ValidationError(
                {"email": "Email addresses must be unique."})
        if password != password2:
            raise serializers.ValidationError(
                {"password": "The two passwords differ."})
        user = User(email=email)
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.meta = meta
        user.is_active = False
        user.save()
        return user