from csv import reader
from ..structure import A, N, V, Transitivity
from importlib.resources import read_text

adverbs: frozenset[A] = frozenset[A]({A(record[0]) for record in reader(read_text(__name__, "adverbs.csv").split("\n")[1:]) if record})

nouns: frozenset[N] = frozenset[N]({N(record[0], record[1], record[2], record[4]) for record in reader(read_text(__name__, "nouns.csv").split("\n")[1:]) if record})
matrix_nouns: frozenset[N] = frozenset[N]({N(record[0], record[1], record[2], record[4]) for record in reader(read_text(__name__, "nouns.csv").split("\n")[1:]) if record and record[3] == "matrix"})
embedded_nouns: frozenset[N] = frozenset[N]({N(record[0], record[1], record[2], record[4]) for record in reader(read_text(__name__, "nouns.csv").split("\n")[1:]) if record and record[3] == "embedded"})

verbs: frozenset[V] = frozenset[V]({V(record[0], Transitivity.Intransitive, record[1], record[2]) for record in reader(read_text(__name__, "verbs_intransitive.csv").split("\n")[1:]) if record} | {V(record[0], Transitivity.Monotransitive, record[1], record[2]) for record in reader(read_text(__name__, "verbs_transitive.csv").split("\n")[1:]) if record})

__all__ = [
	"adverbs",
	"embedded_nouns",
	"matrix_nouns",
	"nouns",
	"verbs"
]

del reader, read_text, A, N, V, Transitivity