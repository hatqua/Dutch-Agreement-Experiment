"""
This module defines a number of classes that represent various word classes.
"""

from .enum_extension import EnumExtension

class ConstituentOrder(EnumExtension):
	"""
	This enum describes the order of the constituents in a phrase.

	Each member of this enum is associated with a string value that may be used for (de)serialization.
	"""
	SOV = "SOV"
	SVO = "SVO"

class DefiniteArticle(EnumExtension):
	"""
	This enum lists the Dutch definite articles.

	Each member of this enum is associated with a string value that may be used for (de)serialization.
	"""
	Het = "het"
	De = "de"

class SemanticCategory(EnumExtension):
	"""
	This enum defines the semantic categories to which nouns belong.

	Each member of this enum is associated with a string value that may be used for (de)serialization.
	"""
	General = "algemeen"
	Family = "familie_leeftijd"
	Organization = "groep_organisatie"
	Media = "kunst_media"
	Education = "onderwijs"
	Law = "recht_bestuur"
	Relation = "relatie"
	Sport = "sport"
	Profession = "werk_dienst"
	Science = "zorg_wetenschap"

class Transitivity(EnumExtension):
	"""
	This enum defines three levels of verb transitivity.

	Each member of this enum is associated with a string value that may be used for (de)serialization.
	"""
	Intransitive = "intransitive"
	Monotransitive = "transitive"
	Ditransitive = "ditransitive"

class Lemma:
	"""
	This class represents word lemmas, and serves as the basis for various word classes, such as N (noun) and P (preposition).
	"""
	def __init__(self, lemma: str):
		"""
		The constructor takes as its only argument the lemma as a string.

		:param str lemma: The lemma associated with the object being created.
		:raises ValueError: If the given lemma string is None or an empty string.
		"""
		# Check if the lemma is given, and if not, raise an exception.
		if not lemma or lemma == "":
			raise ValueError("lemma may not be None or an empty string")

		# Assign the given string lemma to this lemma object.
		self.lemma = lemma

		# Calculate the hash of this lemma object, which is simply the hash of the string lemma associated with this object.
		self.hash = self.lemma.__hash__()

	def __hash__(self) -> int:
		"""
		This function returns the hash of this lemma.
		
		The hash of this lemma is the hash of the string lemma assigned this object in the constructor. The hash is precalculated in the constructor.

		:returns int: The hash of this lemma.
		"""
		return self.hash

	def __eq__(self, value) -> bool:
		"""
		Check if this lemma is equal to the given value.

		If the given value is not of the same type as this object, this function returns False. Otherwise, this function compares the hash of this lemma with that of the given value and returns the result of the comparison.

		:param value: The value with which this lemma is compared.
		:returns bool: True if the given value is of the same type as this object and the hash of the given value is equal to the hash of this object. False otherwise.
		"""
		# Check if the the type of this lemma object is the same as that of the given value.
		if type(self) != type(value):
			# If not, return false.
			return False
		# Otherwise, compare the hash of this object with that of the given value and return the result of the comparison.
		return self.hash == value.hash

class A(Lemma):
	"""
	This class represents adverbs.
	"""
	def __init__(self, lemma: str):
		"""
		Constructs a new adverb.

		:param str lemma: The adverb string lemma.
		:raises ValueError: If the given lemma is None or an empty string.
		"""
		# Call the super constructor to assign the string lemma and calculate the hash of the object being created. Note that the constructor of class Lemma raises an exception if the given lemma is None or an empty string.
		super().__init__(lemma)

	def generate_string(self):
		"""
		Generate a string representation of this adverb.
		"""
		return self.lemma

class N(Lemma):
	"""
	This class represents nouns.
	"""
	def __init__(
			self,
			lemma: str,
			plural_form: str | None,
			definite_article: DefiniteArticle | str,
			semantic_category: SemanticCategory | str
		):
		"""
		Construct a new noun.

		:param str lemma: The noun string lemma. This is the uninflected, underived form of the noun.
		:param str plural_form: The plural form of the noun. A None value idicates that the noun has no plural form, or that the plural form is the same as the singular form.
		:param Article | str definite_article: The definite article the noun accepts.
		:param Category | str semantic_category: The semantic category to which the noun belongs.
		:raises ValueError: If the given lemma is None or an empty string, if the given plural form is an empty string, if the given definite article is None or an empty string, or if the given semantic category is None or an empty string.
		"""
		# Call the super constructor to assign the string lemma and calculate the hash of the object being created. Note that the constructor of class Lemma raises an exception if the given lemma is None or an empty string.
		super().__init__(lemma)

		# Check if the plural form is given, and if not, raise an exception.
		if plural_form == "":
			raise ValueError("the plural form may not be an empty string")

		# Check if the definite article is given, and if not, raise an exception.
		if not definite_article or definite_article == "":
			raise ValueError("the definite article may not be None or an empty string")

		# Check if the semantic category is given, and if not, raise an exception.
		if not semantic_category or semantic_category == "":
			raise ValueError("the semantic category may not be None or an empty string")

		# Assign the plural form of the noun.
		self.plural = plural_form

		# Assign the article to the object being created.
		# If the given value is of type str, then convert the value to type DefiniteArticle and assign to the object being created.
		if type(definite_article) == str:
			self.definite_article = DefiniteArticle.find(definite_article)
		# If the given value is of type DefiniteArticle, assign the value to the object being created.
		elif type(definite_article) == DefiniteArticle:
			self.definite_article = definite_article
		# Otherwise, raise an exception.
		else:
			raise TypeError("invalid type of definite article: " + str(type(definite_article)) + ", allowed types: " + str(str) + ", " + str(DefiniteArticle))

		# Assign the semantic category to the object being created.
		# If the given value is of type str, then convert the value to type Category and assign to the object being created.
		if type(semantic_category) == str:
			self.semantic_category = SemanticCategory.find(semantic_category)
		# If the given value is of type Category, assign the value to the object being created.
		elif type(semantic_category) == SemanticCategory:
			self.semantic_category = semantic_category
		# Otherwise, raise an exception.
		else:
			raise TypeError("invalid type of semantic category: " + str(type(semantic_category)) + ", allowed types: " + str(str) + ", " + str(SemanticCategory))

	def generate_string(self, singular: bool = True) -> str:
		"""
		Generate a string representation of this noun.

		:param bool singular: A boolean value indicating whether the string representation contains the noun in the singular or the the plural form. The default form is singular.
		:returns str: A string representation of this noun.
		"""
		return self.definite_article.value + " " + self.lemma if singular else "de " + (self.lemma if not self.plural else self.plural)

class P(Lemma):
	"""
	This class represents prepositions.
	"""
	def __init__(self, lemma: str):
		"""
		Construct a new preposition.

		:param str lemma: The preposition string lemma.
		:raises ValueError: If the given lemma is None or an empty string.
		"""
		# Call the super constructor to assign the string lemma and calculate the hash of the object being created. Note that the constructor of class Lemma raises an exception if the given lemma is None or an empty string.
		super().__init__(lemma)

	def generate_string(self):
		"""
		Generate a string representation of this preposition.
		"""
		return self.lemma

class V(Lemma): # But not for Vendetta!
	"""
	This class represents verbs.
	"""
	def __init__(
			self,
			lemma: str,
			transitivity: Transitivity | str,
			present_singular_form: str,
			present_plural_form: str
		):
		"""
		Construct a new verb.

		:param str lemma: The verb string lemma. This is the infinitive form of the verb.
		:param Transitivity | str transitivity: The transitivity level of the verb.
		:param str presepresent_singular_formnt_singular: The present singular form of the verb.
		:param str present_plural_form: The present plural form of the verb.
		:raises ValueError: If the given lemma is None or an empty string, if the given transitivity is None or an empty string, if the given present singular form is None or an empty string, or if the given present plural form is None or an empty string.
		"""
		# Call the super constructor to assign the lemma and calculate the hash of the object being created. Note that the constructor of class Lemma raises an exception if the given lemma is None or an empty string.
		super().__init__(lemma)

		# Check if transitivty is given, and if not, raise an exception.
		if not transitivity or transitivity == "":
			raise ValueError("transitivity may not be None or an empty string")

		# Check if the present singular form is given, and if not, raise an exception.
		if not present_singular_form or present_singular_form == "":
			raise ValueError("the present singular form may not be None or an empty string")

		# Check if the present plural form is given, and if not, raise an exception.
		if not present_plural_form or present_plural_form == "":
			raise ValueError("the present plural form may not be None or an empty string")

		# Assign the transitivity level of the verb.
		# If the given value is of type str, then convert the value to type Transitivity and assign to the object being created.
		if type(transitivity) == str:
			self.transitivity = Transitivity.find(transitivity)
		# If the given value is of type Transitivity, assign the value to the object being created.
		elif type(transitivity) == Transitivity:
			self.transitivity = transitivity
		# Otherwise, raise an exception.
		else:
			raise TypeError("invalid type of transitivity: " + str(type(transitivity)) + ", allowed types: " + str(str) + ", " + str(Transitivity))
	
		# Assign verb forms.
		self.present_singular_form = present_singular_form
		self.present_plural_form = present_plural_form

	def generate_string(self, singular: bool = True) -> str:
		"""
		Generate a string representation of this verb.

		:param bool singular: A boolean value indicating whether the string representation contains the verb in the singular of the plural form. The default form is singular.
		:returns str: A string representation of this verb.
		"""
		return self.present_singular_form if singular else self.present_plural_form