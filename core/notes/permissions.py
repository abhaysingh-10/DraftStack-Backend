# Manual filtering to DRF Permission System

from rest_framework.permissions import BasePermission

# obj.user is the  owner (XYZ)
# request.user is the current user (ABC)

class IsOwner(BasePermission):
    def has_object_permission(self,request,view,obj):
        return obj.user == request.user  # Match if true - allow  No match if false → block
     


