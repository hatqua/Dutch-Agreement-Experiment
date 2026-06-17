"""
This module defines an extension to Python's ``Enum``.
"""

from enum import Enum

class EnumExtension(Enum):
	"""
	This enum extends Python's Enum by defining a number of functions that operate on descendants of this enum. There is currently only one function in this enum.
	"""
	@classmethod
	def find(cls, value):
		"""
		Return the member that is associated with the given value.
		"""
		# Iterate over the members of the enum.
		for _, member in cls.__members__.items():
			# Check if the value associated with the member in the current iteration equals the given value.
			if member.value == value:
				# Return the member in the current iteration.
				return member
		# If no member is found having a value equal to the given value, return None.
		return None