from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from base.models import User, Company, Department, Employee
import io
import pandas

import pandas as pd
from base.serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    CompanySerializer,
    DepartmentSerializer,
    EmployeeSerializer,
    FileUploadSerializer,
    UserSerializer
)

# from base.serializer import ProfileSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token['role'] = user.role
        #token['comp'] = user.company_set.all()



        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#uploads employees
class EmployeeUploadView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request):
        
        
        if request.data['file'] is None:
            return Response({"error": "No File Found"},
                            status=status.HTTP_400_BAD_REQUEST)
        
        if request.FILES:
            print("===============here==============")
            file_sent = str(request.data['file'])
            if file_sent.endswith('.csv'):
                for file in request.FILES.values():
                # reading the CSV file
                    csvFile = pandas.read_csv(file)
                    columns = list(csvFile.columns.values)
                    

                    full_name, ec_number, email, address, position , year_started, year_left, company, department = columns[0], columns[1], columns[2], columns[3], columns[4], columns[5], columns[6], columns[7], columns[8]
                    objects = []
                    for index, row in csvFile.iterrows():
                        company = Company.objects.get(id=row[7])
                        department = Department.objects.get(id=row[8])

                        #Employee(name=row[name],company=company)
                        objects.append(Employee(
                                        full_name=row[full_name],
                                        company=company,
                                        ec_number=row[ec_number],
                                        email=row[email],
                                        address=row[address],
                                        position=row[position],
                                        year_started=row[year_started],
                                        year_left=row[year_left],
                                        department=department


                                        ))
                    Employee.objects.bulk_create(objects)
            
            elif file_sent.endswith('.xlsx'):
                # for file in request.FILES.values():
                # # reading the CSV file
                #     xl = pandas.read_excel(file)
                #     columns = list(xl.columns.values)
                #     name, company = columns[0], columns[1]
                #     objects = []
                #     for index, row in xl.iterrows():
                #         company = Company.objects.get(id=row[1])
                #         Department(name=row[name],company=company)
                #         objects.append(Department(
                #                         name=row[name],
                #                         company=company
                #                         ))
                #     Department.objects.bulk_create(objects)
                pass
            else:
                print('invalid format=====================')
            
            return Response(
                    {"message": "Upload Successfull",
                    "data": ''}, status=status.HTTP_200_OK) 

        return Response({"success": "Good job, buddy"})
    
#upload departments
class FileUploadView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request):
        
        if request.data['file'] is None:
            return Response({"error": "No File Found"},
                            status=status.HTTP_400_BAD_REQUEST)
        if request.FILES:
            file_sent = str(request.data['file'])
            if file_sent.endswith('.csv'):
                for file in request.FILES.values():
                # reading the CSV file
                    csvFile = pandas.read_csv(file)
                    columns = list(csvFile.columns.values)
                    name, company = columns[0], columns[1]
                    objects = []
                    for index, row in csvFile.iterrows():
                        company = Company.objects.get(id=row[1])
                        Department(name=row[name],company=company)
                        objects.append(Department(
                                        name=row[name],
                                        company=company
                                        ))
                    Department.objects.bulk_create(objects)
            
            elif file_sent.endswith('.xlsx'):
                # for file in request.FILES.values():
                # # reading the CSV file
                #     xl = pandas.read_excel(file)
                #     columns = list(xl.columns.values)
                #     name, company = columns[0], columns[1]
                #     objects = []
                #     for index, row in xl.iterrows():
                #         company = Company.objects.get(id=row[1])
                #         Department(name=row[name],company=company)
                #         objects.append(Department(
                #                         name=row[name],
                #                         company=company
                #                         ))
                #     Department.objects.bulk_create(objects)
                pass
            else:
                print('invalid format=====================')
            
            return Response(
                    {"message": "Upload Successfull",
                    "data": ''}, status=status.HTTP_200_OK) 

        return Response({"success": "Good job, buddy"})
    

class EmployeeView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (AllowAny, )

class EmployeeViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (AllowAny, )

class DepartmentView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (AllowAny, )

class DepartmentViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (AllowAny, )

class CompanyView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (AllowAny, )

class CompanyViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (AllowAny, )
    
# class CompanyView(APIView):
#     serializer_class = CompanySerializer
#     permission_classes = (AllowAny, )

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         valid = serializer.is_valid(raise_exception=True)

#         if valid:
#             serializer.save()
#             status_code = status.HTTP_201_CREATED

#             response = {
#                 'success': True,
#                 'statusCode': status_code,
#                 'message': 'Company successfully registered!',
#                 'company': serializer.data
#             }

#             return Response(response, status=status_code)
        
class AuthUserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'user': serializer.data
            }

            return Response(response, status=status_code)
        
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_profile(request):
#     user = request.user
#     profile = user.profile
#     serializer = ProfileSerializer(profile, many=False)
#     return Response(serializer.data)

class AuthUserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role']
                }
            }

            return Response(response, status=status_code)

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

# class UserListView(APIView):
#     serializer_class = UserSerializer
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         user = request.user
#         if user.role != 1:
#             response = {
#                 'success': False,
#                 'status_code': status.HTTP_403_FORBIDDEN,
#                 'message': 'You are not authorized to perform this action'
#             }
#             return Response(response, status.HTTP_403_FORBIDDEN)
#         else:
#             users = User.objects.all()
#             serializer = self.serializer_class(users, many=True)
#             response = {
#                 'success': True,
#                 'status_code': status.HTTP_200_OK,
#                 'message': 'Successfully fetched users',
#                 'users': serializer.data

#             }
#             return Response(response, status=status.HTTP_200_OK)