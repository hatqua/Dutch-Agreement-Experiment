"""
This script provides the command-line interface for the package 'synthesis'.

Users of the package 'synthesis' may execute this package from the command line to generate a corpus. Execution requires two positional arguments: the path to the output directory where the corpus is to be saved, and the sample size per condition.

The package synthesizes a corpus comprising 13 files in the given output directory. The name of a file begins with a number denoting the template of the sentences in the file. The number is followed by a sequence of the letters 's' and 'p', representing the two grammatical numbers, 'singular' and 'plural', respectively. Each letter denotes the grammatical number of the content word with the same index as the letter.

For example, the file 2sps contains sentences generated from template 2. The first content word, the head of the subject noun phrase, is singular; the second content word, the complement of the preposition, is plural; and the last content word, the verb, is singular. An example sentence from this file is 'de oma van de jongetjes zucht'.

The number of sentences per file depends on the given sample size. If the given sample size is less than or equal to 0, the package generates all possible sentences from all possible permutations of the content words available in the sub-package data. Otherwise, if the given sample size is greater than 0, the package generates only a number of sentences equal to the given sample size.
"""

from argparse import ArgumentParser
from pathlib import Path
from .corpus import matrix_with_adverb, matrix_with_embedded, subject_with_adjunct

def main():
	# Parse CLI arguments
	parser = ArgumentParser()
	parser.add_argument("output_directory")
	parser.add_argument("sample_size", type=int)
	args = parser.parse_args()

	# Get the path to the output directory, and create the missing directories on the path.
	output_directory = Path(args.output_directory)
	output_directory.mkdir(parents=True, exist_ok=True)

	# Get sample size.
	sample_size = args.sample_size

	# Condition 1.
	# Keep count of generated sentences in this variable.
	sentence_counter = 0
	# Open output files for writing, creating any missing file, and truncating any existing file.
	with open(output_directory.joinpath("1ssss"), "w") as _1ssss, \
		open(output_directory.joinpath("1spss"), "w") as _1spss, \
		open(output_directory.joinpath("1spsp"), "w") as _1spsp, \
		open(output_directory.joinpath("1spps"), "w") as _1spps, \
		open(output_directory.joinpath("1sppp"), "w") as _1sppp:
		# Iterate over all sentences in condition 1, and write to the output file.
		for phrase in matrix_with_embedded:
			_1ssss.write(phrase.generate_string())
			_1ssss.write("\n")

			_1spss.write(phrase.generate_string(arguments={phrase.subject_noun_phrase: {"arguments": {phrase.subject_noun_phrase.adjuncts[0]: {"arguments": {phrase.subject_noun_phrase.adjuncts[0].subject_noun_phrase: {"singular": False}}}}}}))
			_1spss.write("\n")

			_1spsp.write(phrase.generate_string(singular=False, arguments={phrase.subject_noun_phrase: {"arguments": {phrase.subject_noun_phrase.adjuncts[0]: {"arguments": {phrase.subject_noun_phrase.adjuncts[0].subject_noun_phrase: {"singular": False}}}}}}))
			_1spsp.write("\n")

			_1spps.write(phrase.generate_string(arguments={phrase.subject_noun_phrase: {"arguments": {phrase.subject_noun_phrase.adjuncts[0]: {"singular": False, "arguments": {phrase.subject_noun_phrase.adjuncts[0].subject_noun_phrase: {"singular": False}}}}}}))
			_1spps.write("\n")

			_1sppp.write(phrase.generate_string(singular=False, arguments={phrase.subject_noun_phrase: {"arguments": {phrase.subject_noun_phrase.adjuncts[0]: {"singular": False, "arguments": {phrase.subject_noun_phrase.adjuncts[0].subject_noun_phrase: {"singular": False}}}}}}))
			_1sppp.write("\n")

			# Check if the number of sentences is limited,
			if sample_size > 0:
				# and if so, increase the sentecne counter.
				sentence_counter = sentence_counter + 1
				# If the sentence counter reached the sample size, stop iterating over the sentences and writing the sentences.
				if sentence_counter >= sample_size:
					break

	# Condition 2.
	# Reset counter.
	sentence_counter = 0
	# Open output files for writing, creating any missing file, and truncating any existing file.
	with open(output_directory.joinpath("2sss"), "w") as _2sss, \
		open(output_directory.joinpath("2sps"), "w") as _2sps, \
		open(output_directory.joinpath("2spp"), "w") as _2spp:
		# Iterate over all sentences in condition 2, and write to the output file.
		for phrase in subject_with_adjunct:
			_2sss.write(phrase.generate_string())
			_2sss.write("\n")

			_2sps.write(phrase.generate_string(arguments={phrase.subject_noun_phrase: {"arguments": {phrase.subject_noun_phrase.adjuncts[0]: {"singular": False}}}}))
			_2sps.write("\n")

			_2spp.write(phrase.generate_string(singular=False, arguments={phrase.subject_noun_phrase: {"arguments": {phrase.subject_noun_phrase.adjuncts[0]: {"singular": False}}}}))
			_2spp.write("\n")

			# Check if the number of sentences is limited,
			if sample_size > 0:
				# and if so, increase the sentecne counter.
				sentence_counter = sentence_counter + 1
				# If the sentence counter reached the sample size, stop iterating over the sentences and writing the sentences.
				if sentence_counter >= sample_size:
					break

	# Condition 3.
	# Reset counter.
	sentence_counter = 0
	# Open output files for writing, creating any missing file, and truncating any existing file.
	with open(output_directory.joinpath("3ssss"), "w") as _3ssss, \
		open(output_directory.joinpath("3spss"), "w") as _3spss, \
		open(output_directory.joinpath("3spsp"), "w") as _3spsp, \
		open(output_directory.joinpath("3spps"), "w") as _3spps, \
		open(output_directory.joinpath("3sppp"), "w") as _3sppp:
		# Iterate over all sentences in condition 3, and write to the output file.
		for phrase in matrix_with_adverb:
			_3ssss.write(phrase.generate_string())
			_3ssss.write("\n")

			_3spss.write(phrase.generate_string(arguments={phrase.subject_noun_phrase: {"arguments": {phrase.subject_noun_phrase.adjuncts[0]: {"arguments": {phrase.subject_noun_phrase.adjuncts[0].subject_noun_phrase: {"singular": False}}}}}}))
			_3spss.write("\n")

			_3spsp.write(phrase.generate_string(singular=False, arguments={phrase.subject_noun_phrase: {"arguments": {phrase.subject_noun_phrase.adjuncts[0]: {"arguments": {phrase.subject_noun_phrase.adjuncts[0].subject_noun_phrase: {"singular": False}}}}}}))
			_3spsp.write("\n")

			_3spps.write(phrase.generate_string(arguments={phrase.subject_noun_phrase: {"arguments": {phrase.subject_noun_phrase.adjuncts[0]: {"singular": False, "arguments": {phrase.subject_noun_phrase.adjuncts[0].subject_noun_phrase: {"singular": False}}}}}}))
			_3spps.write("\n")

			_3sppp.write(phrase.generate_string(singular=False, arguments={phrase.subject_noun_phrase: {"arguments": {phrase.subject_noun_phrase.adjuncts[0]: {"singular": False, "arguments": {phrase.subject_noun_phrase.adjuncts[0].subject_noun_phrase: {"singular": False}}}}}}))
			_3sppp.write("\n")

			# Check if the number of sentences is limited,
			if sample_size > 0:
				# and if so, increase the sentecne counter.
				sentence_counter = sentence_counter + 1
				# If the sentence counter reached the sample size, stop iterating over the sentences and writing the sentences.
				if sentence_counter >= sample_size:
					break

if __name__ == "__main__":
	main()