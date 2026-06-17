"""
This subpackage represents the linguistic structure.

This subpackage contains two modules. The first module, ``morphology``, represents the morphological layer in linguistic structure. The second module, ``syntax``, represents the syntactic layer.
"""

from .morphology import (
	A,
	N,
	P,
	V,
	Lemma,
	ConstituentOrder,
	DefiniteArticle,
	SemanticCategory,
	Transitivity
)

from .syntax import (
	AP,
	NP,
	PP,
	VP
)

__all__ = [
	"A",
	"AP",
	"Lemma",
	"DefiniteArticle",
	"SemanticCategory",
	"N",
	"NP"
	"P",
	"PP",
	"Transitivity",
	"ConstituentOrder",
	"V",
	"VP"
]