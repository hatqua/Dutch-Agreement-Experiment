"""
This module defines a number of classes that represent various syntactic phrases.
"""

from __future__ import annotations
from .morphology import A, N, P, V, ConstituentOrder, DefiniteArticle

class AP:
	"""
	This class represents adverb phrases.
	"""
	def __init__(
			self,
			head: A
	):
		"""
		Construct a new adverb phrase.

		:param A head: The head of the adverb phrase.
		:raises ValueError: If the given head adverb is None.
		"""
		# Check if the head adverb is given, and if not, raise an exception.
		if not head:
			raise ValueError("the head may not be None")

		# Assign the head to the adverb phrase being created.
		self.head = head

		# Calcualte the hash of the adverb phrase being created.
		self.hash = self.head.hash

	def __hash__(self) -> int:
		"""
		Return the hash of this adverb phrase. The hash is precalculated in the constructor.

		:returns int: The hash of this adverb phrase.
		"""
		return self.hash

	def __eq__(self, value) -> bool:
		"""
		Check if this adverb phrase is equal to the given value.

		If the given value is not of type AP, this function returns False. Otherwise, this function compares the hash of this adverb phrase with that of the given value and returns the result of the comparison.

		:param value: The value with which this adverb phrase is compared.
		:returns bool: True if the given value is of type AP and the hash of the given value is equal to the hash of this adverb phrase. False otherwise.
		"""
		if type(value) != AP:
			return False
		return self.hash == value.hash

	def generate_string(self) -> str:
		"""
		Generate a string representation of this adverb phrase.

		:returns str: A string representation of this adverb phrase.
		"""
		return self.head.generate_string()

class NP:
	"""
	This class represents noun phrases.
	"""
	def __init__(
			self,
			head: N,
			adjuncts: list[PP | VP] | None = None
		):
		"""
		Construct a new noun phrase.

		:param N head: The head of the noun phrase.
		:param list[PP | VP] adjuncts: A list of adjuncts. The list may be empty or None, indicating that the noun phrase contains no adjuncts.
		:raises ValueError: If the given head is None.
		"""
		if not head:
			raise ValueError("the head may not be None")

		# Assign the head noun to the object being created.
		self.head = head

		# Assign the list of adjuncts to the noun phrase.
		self.adjuncts = adjuncts

		# Calculate the hash of the noun phrase being created.
		self.hash = (head.hash, tuple([adjunct.hash for adjunct in self.adjuncts]) if self.adjuncts else ()).__hash__()

	def __hash__(self) -> int:
		"""
		Return the hash of this noun phrase. The hash is precalculated in the constructor.

		:returns int: The hash of this noun phrase
		"""
		return self.hash

	def __eq__(self, value) -> bool:
		"""
		Check if this noun phrase is equal to the given value.

		If the given value is not of type NP, this function returns False. Otherwise, this function compares the hash of this noun phrase with that of the given value and returns the result of the comparison.

		:param value: The value with which this noun phrase is compared.
		:returns bool: True if the given value is of type NP and the hash of the given value is equal to the hash of this noun phrase. False otherwise.
		"""
		if type(value) != NP:
			return False
		return self.hash == value.hash

	def generate_string(
			self,
			singular: bool = True,
			arguments: dict = None
		) -> str:
		"""
		Generate a string representation of this noun phrase.

		:param bool singular: A boolean value indicating whether the string representation contains the head in the singular or the the plural form. The default form is singular.
		:param dict arguments: A set of key-value pairs, where the key in the pair is an adjunct, and the value in the pair contains the arguments for the associated adjunct's generate_string(...) function call.
		:returns str: A string representation of this noun phrase.
		"""
		if not arguments:
			arguments = {}
		return self.head.generate_string(singular) + \
			(" " + " ".join([(("dat " if self.head.definite_article == DefiniteArticle.Het else "die ") if type(adjunct) == VP else "") + adjunct.generate_string(**arguments.get(adjunct, {})) for adjunct in self.adjuncts]) if self.adjuncts else "")

class PP:
	"""
	This class represents prepositional phrases.
	"""
	def __init__(
		self,
		head: P,
		complement: NP
	):
		"""
		Construct a new prepositional phrase.

		:param P head: The head of the prepositional phrase.
		:param NP complement: The complement of the preposition.
		:raises ValueError: If the given head is None, or if the given complement is None.
		"""
		# Check if the preposition is given, and if not, raise an exception.
		if not head:
			raise ValueError("the head may not be None")

		# Check if the complement is given, and if not, raise an exception.
		if not complement:
			raise ValueError("the cmplmenet of the preposition may not be None")

		# Assign the head and the complement of the preposition to the prepositional phrase.
		self.preposition = head
		self.complement = complement

		# Calculate the hash of the prepositional phrase being created.
		self.hash = (self.preposition.hash, complement.hash).__hash__()

	def __hash__(self) -> int:
		"""
		Return the hash of this prepositional phrase. The hash is precalculated in the constructor.

		:returns int: The hash of this prepositional phrase.
		"""
		return self.hash

	def __eq__(self, value) -> bool:
		"""
		Check if this prepositional phrase is equal to the given value.

		If the given value is not of type PP, this function returns False. Otherwise, this function compares the hash of this prepositional phrase with that of the given value and returns the result of the comparison.

		:param value: The value with which this prepositional phrase is compared.
		:returns bool: True if the given value is of type PP and the hash of the given value is equal to the hash of this prepositional phrase. False otherwise.
		"""
		if type(value) != PP:
			return False
		return self.hash == value.hash

	def generate_string(
			self,
			singular: bool = True,
			arguments: dict = None
		) -> str:
		"""
		Generate a string representation of this prepositional phrase.

		:param bool singular: Whether the noun in the noun phrase, that is the complement of the preposition, is in the singular or the plural form. The default form is the singular form.
		:param dict arguments: A set of key-value pairs, where the key in the pair is an adjunct in the noun phrase, that is the complement of the preposition, and the value in the pair contains the arguments for the associated adjunct's generate_string(...) function call. See the function generate_string(...) in class NP.
		"""
		return self.preposition.lemma + " " + self.complement.generate_string(singular, arguments)

class VP:
	"""
	This class represents verb phrases.
	"""
	def __init__(
		self,
		verb: V,
		subject_noun_phrase: NP | None = None,
		object_noun_phrase: NP | None = None,
		adjuncts: list[AP | PP] | None = None
	):
		"""
		Construct a new verb phrase.

		:param V verb: The head of the verb phrase.
		:param NP subject_noun_phrase: The subject of the verb.
		:param NP object_noun_phrase: The object of the verb.
		:param list[Lemma | PP] adjuncts: A list of adjuncts.
		:raises ValueError: If the given verb is None.
		"""
		# Check if the verb is given, and if not, raise an exception.
		if not verb:
			raise ValueError("the verb may not be None")

		# Assign the constituents to this object.
		self.verb = verb
		self.subject_noun_phrase = subject_noun_phrase
		self.object_noun_phrase = object_noun_phrase
		self.adjuncts = adjuncts

		# Calculate the hash of this object.
		self.hash = ((verb.hash, subject_noun_phrase.hash if subject_noun_phrase else subject_noun_phrase.__hash__(), object_noun_phrase.hash if object_noun_phrase else object_noun_phrase.__hash__()) + (tuple([adjunct.hash for adjunct in adjuncts]) if adjuncts else ())).__hash__()
	
	def __hash__(self) -> int:
		"""
		This function returns the hash of this verb phrase. The hash is precalculated in the constructor.

		:returns int: The hash of this verb phrase.
		"""
		return self.hash
	
	def __eq__(self, value) -> bool:
		"""
		Check if this verb phrase is equal to the given value.

		If the given value is not of type VP, this function returns False. Otherwise, this function compares the hash of this verb phrase with that of the given value and returns the result of the comparison.

		:param value: The value with which this verb phrase is compared.
		:returns bool: True if the given value is of type VP and the hash of the given value is equal to the hash of this verb phrase. False otherwise.
		"""
		if type(value) != VP:
			return False
		return self.hash == value.hash
	
	def generate_string(
			self,
			constituent_order: ConstituentOrder = ConstituentOrder.SOV,
			singular: bool = True,
			arguments: dict = None
	) -> str:
		"""
		Generate a string representation of this verb phrase.

		:param ConstituentOrder constituent_order: The order of the constituents in the generated string. The default order of the constituents is SOV.
		:param bool singular: Whether the verb is in the singular or the plural form. The default form is the singular form.
		:param dict arguments: A set of key-value pairs, where the key in the pair is an complement/adjunct, and the value in the pair contains the arguments for the associated complement/adjunct's generate_string(...) function call.
		:returns str: A string representation of this verb phrase.
		"""
		if not arguments:
			arguments = {}
		if constituent_order == ConstituentOrder.SOV:
			return (self.subject_noun_phrase.generate_string(**arguments.get(self.subject_noun_phrase, {})) + " " if self.subject_noun_phrase else "") + \
				(self.object_noun_phrase.generate_string(**arguments.get(self.object_noun_phrase, {})) + " " if self.object_noun_phrase else "") + \
				(" ".join([adjunct.generate_string(**arguments.get(adjunct, {})) for adjunct in self.adjuncts]) + " " if self.adjuncts and len(self.adjuncts) > 0 else "") + \
				self.verb.generate_string(singular)
		else:
			return (self.subject_noun_phrase.generate_string(**arguments.get(self.subject_noun_phrase, {})) + " " if self.subject_noun_phrase else "") + \
				self.verb.generate_string(singular) + \
				(" " + self.object_noun_phrase.generate_string(**arguments.get(self.object_noun_phrase, {})) + " " if self.object_noun_phrase else "") + \
				(" " + " ".join([adjunct.generate_string(**arguments.get(adjunct, {})) for adjunct in self.adjuncts]) if self.adjuncts and len(self.adjuncts) > 0 else "")