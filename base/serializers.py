from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from base.models import *
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'company',
            'uid',
            'email',
            'role'
        )

# class ProfileSerializer(serializers.ModelSerializer):
#     user = UserSerializer(many=False, read_only=True)
#     class Meta:
#         model = Profile
#         fields = ('user', 'first_name', 'last_name', 'email')
class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = '__all__'
        # read_only_fields = ('company',)


class DepartmentSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset= Company.objects.all(),many=False)
    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'company'
        )
        depth = 1

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'company',
            'department',
            'full_name',
            'ec_number',
            'email',
            'address',
            'position',
            'year_started',
            'year_left'
        )

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'date_of_registarion',
            'registration_number',
            'address',
            'contact_person'
        )

    def create(self, validated_data):
        company = Company.objects.create(**validated_data)
        return company
    
class UserRegistrationSerializer(serializers.ModelSerializer):
    #company = serializers.PrimaryKeyRelatedField
    class Meta:
        model = User
        fields = (
            'company',
            'email',
            'password'
        )

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                'role': user.role,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")