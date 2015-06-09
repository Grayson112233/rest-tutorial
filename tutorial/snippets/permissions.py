from rest_framework import permissions

# Only owners of an object can edit that object
class IsOwnerOrReadOnly(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):
		# Read permissions are allowed to any request
		if request.method in permissions.SAFE_METHODS:
			return True

		# Write permissions are only allowed to the owner
		return obj.owner == request.user # is user the owner?