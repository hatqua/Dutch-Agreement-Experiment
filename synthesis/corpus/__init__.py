from ..data import adverbs, embedded_nouns, matrix_nouns, nouns, verbs
from ..structure import AP, NP, PP, VP, Transitivity, P

matrix_with_embedded: frozenset[VP] = frozenset[VP]({VP(matrix_verb, NP(matrix_subject, [VP(embedded_verb, NP(embedded_noun))])) for matrix_subject in nouns for embedded_noun in nouns for embedded_verb in verbs for matrix_verb in verbs if embedded_verb.transitivity == Transitivity.Monotransitive and matrix_verb.transitivity == Transitivity.Intransitive and matrix_subject.semantic_category == embedded_noun.semantic_category and matrix_subject != embedded_noun})
matrix_with_adverb: frozenset[VP] = frozenset[VP]({VP(sentence.verb, sentence.subject_noun_phrase, None, [AP(adverb)]) for sentence in matrix_with_embedded for adverb in adverbs})
subject_with_adjunct: frozenset[VP] = frozenset[VP]({VP(verb, NP(subject, [PP(P("van"), NP(complement))])) for subject in nouns for complement in nouns for verb in verbs if verb.transitivity == Transitivity.Intransitive and subject.semantic_category == complement.semantic_category and subject != complement})

__all__ = [
	"matrix_with_adverb",
	"matrix_with_embedded",
	"subject_with_adjunct"
]

del adverbs, embedded_nouns, matrix_nouns, nouns, verbs, AP, NP, PP, VP, Transitivity, P