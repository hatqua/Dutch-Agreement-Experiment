"""
This package contains the facilities to synthesize a Dutch corpus.

Users of the package 'synthesis' may execute this package from the command line to generate a corpus. Execution requires two positional arguments: the path to the output directory where the corpus is to be saved, and the sample size per condition.

The package synthesizes a corpus comprising 13 files in the given output directory. The name of a file begins with a number denoting the template of the sentences in the file. The number is followed by a sequence of the letters 's' and 'p', representing the two grammatical numbers, 'singular' and 'plural', respectively. Each letter denotes the grammatical number of the content word with the same index as the letter.

For example, the file 2sps contains sentences generated from template 2. The first content word, the head of the subject noun phrase, is singular; the second content word, the complement of the preposition, is plural; and the last content word, the verb, is singular. An example sentence from this file is 'de oma van de jongetjes zucht'.

The number of sentences per file depends on the given sample size. If the given sample size is less than or equal to 0, the package generates all possible sentences from all possible permutations of the content words available in the sub-package data. Otherwise, if the given sample size is greater than 0, the package generates a number of sentences equal to the given sample size.

The sentence-synthesis mechanism resides in the subpackage 'corpus'. The mechanism is eager by nature, which causes a noticeable delay during the loading of the package. In particular, the subpackage constructs three Python sets, where each set represents a template and contains all the sentences from that template. The mechanism builds on top of the data and data structures found in the packages 'data' and 'structure', respectively.
"""