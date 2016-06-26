from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	'''
	Custom permission to only allow the owners of an object to edit it
	'''

	def has_object_permission(self, request, view, obj):
		''' 
		Read permissions are allowed to any request.
		Write permissions are only allowed to the owner.
		'''
		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.owner == request.user
