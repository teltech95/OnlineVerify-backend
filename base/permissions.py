# from typing import Type

# from django.http.request import HttpRequest
# from rest_framework.permissions import BasePermission

# from users.models import Worker


# class IsWorkerUser(BasePermission):
#     """
#     Allows access only to worker users.
#     """

#     def has_permission(self, request: Type[HttpRequest], view):
#         if request.user.is_worker:
#             return bool(request.user and request.user.is_worker and request.user.is_authenticated)
#         return False


# class IsManagerUser(BasePermission):
#     """
#     Allows access only to manager users.
#     """

#     def has_permission(self, request: Type[HttpRequest], view):
#         if request.user.is_worker:
#             worker = Worker.objects.get(user=request.user.id)
#             if worker:
#                 return bool(request.user and request.user.is_worker and request.user.is_authenticated and worker.is_manager)
#         return False




# class ManagerViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     permission_classes = [IsManagerUser]