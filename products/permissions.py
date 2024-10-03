from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # GET
            return True  # hammaga Get uchun OK

        return obj.owner == request.user  # quyidagi obyektini egasi request tashlagan odam bolsa OK


class IsStaffOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff   #agar requestni egasi admin bolsa OK yomasa faqat oqiy oladi
