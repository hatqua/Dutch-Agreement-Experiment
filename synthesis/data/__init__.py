"""
This subpackage constructs sets of lemmas.

This subpackage contains a number of CSV files. Each CSV file corresponds to one word class. For each word class, this subpackage constructs a set of lemmas based on the content of the CSV files.
"""

from csv import reader
from ..structure import A, N, V, Transitivity
from importlib.resources import read_text

adverbs: frozenset[A] = frozenset[A]({A(record[0]) for record in reader(read_text(__name__, "adverbs.csv").split("\n")[1:]) if record})
"""
This set contains the adverbs found in the CSV file ``adverbs.csv``.
"""
nouns: frozenset[N] = frozenset[N]({N(record[0], record[1], record[2], record[4]) for record in reader(read_text(__name__, "nouns.csv").split("\n")[1:]) if record})
"""
This set contains the nouns found in the CSV file ``nouns.csv``.
"""
matrix_nouns: frozenset[N] = frozenset[N]({N(record[0], record[1], record[2], record[4]) for record in reader(read_text(__name__, "nouns.csv").split("\n")[1:]) if record and record[3] == "matrix"})
"""
This set contains the nouns found in the CSV file ``nouns.csv`` marked as ``matrix``.
"""
embedded_nouns: frozenset[N] = frozenset[N]({N(record[0], record[1], record[2], record[4]) for record in reader(read_text(__name__, "nouns.csv").split("\n")[1:]) if record and record[3] == "embedded"})
"""
This set contains the nouns found in the CSV file ``nouns.csv`` marked as ``embedded``.
"""
verbs: frozenset[V] = frozenset[V]({V(record[0], Transitivity.Intransitive, record[1], record[2]) for record in reader(read_text(__name__, "verbs_intransitive.csv").split("\n")[1:]) if record} | {V(record[0], Transitivity.Monotransitive, record[1], record[2]) for record in reader(read_text(__name__, "verbs_transitive.csv").split("\n")[1:]) if record})
"""
This set contains the verbs found in the CSV file ``verbs.csv``.
"""

__all__ = [
	"adverbs",
	"embedded_nouns",
	"matrix_nouns",
	"nouns",
	"verbs"
]

del reader, read_text, A, N, V, Transitivity