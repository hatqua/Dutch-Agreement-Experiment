"""
This subpackage contains the sentence-synthesis mechanism.

This subpackage exports three Python sets. Each set represents a template and contains all the sentences from that template. The choice of Python set results in eager loading, which, in turn, results in a noticeable delay during the loading of the package. However, this choice of Python set ensures a random order of the sentences (which is required in the main function of the package 'synthesis').
"""

from ..data import adverbs, embedded_nouns, matrix_nouns, nouns, verbs
from ..structure import AP, NP, PP, VP, Transitivity, P

matrix_with_embedded: frozenset[VP] = frozenset[VP]({VP(matrix_verb, NP(matrix_subject, [VP(embedded_verb, NP(embedded_noun))])) for matrix_subject in nouns for embedded_noun in nouns for embedded_verb in verbs for matrix_verb in verbs if embedded_verb.transitivity == Transitivity.Monotransitive and matrix_verb.transitivity == Transitivity.Intransitive and matrix_subject.semantic_category == embedded_noun.semantic_category and matrix_subject != embedded_noun})
"""
A set of verb phrases where the subject contains a subordinate clause.

The matrix verb in each sentence is intransitive. That is, the verb in each sentence has one argument in the subject position.

The subject noun phrase in each sentence contains a subordinate clause, where the verb is monotransitive. However, the verb in the subordinate clause is constructed with its subject argument only, with its object position elided and coreferring with the subject of the matrix clause.

In each sentence, both nouns in both subject positions belong to the same semantic category.
"""
matrix_with_adverb: frozenset[VP] = frozenset[VP]({VP(sentence.verb, sentence.subject_noun_phrase, None, [AP(adverb)]) for sentence in matrix_with_embedded for adverb in adverbs})
"""
Similar to ``synthesis.corpus.matrix_with_embedded``. However, a matrix clause contains an adverb.
"""
subject_with_adjunct: frozenset[VP] = frozenset[VP]({VP(verb, NP(subject, [PP(P("van"), NP(complement))])) for subject in nouns for complement in nouns for verb in verbs if verb.transitivity == Transitivity.Intransitive and subject.semantic_category == complement.semantic_category and subject != complement})
"""
A set of verb phrases where the subject contains a prepositional phrase.

The verb in each sentence is intransitive. That is, the verb in each sentence has one argument in the subject position.

In each sentence, both nouns, the subject and the complement of the preposition, belong to the same semantic category.
"""

__all__ = [
	"matrix_with_adverb",
	"matrix_with_embedded",
	"subject_with_adjunct"
]

del adverbs, embedded_nouns, matrix_nouns, nouns, verbs, AP, NP, PP, VP, Transitivity, P