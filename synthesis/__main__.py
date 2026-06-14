from argparse import ArgumentParser
from pathlib import Path
from .corpus import matrix_with_adverb, matrix_with_embedded, subject_with_adjunct

def main():
	parser = ArgumentParser()
	parser.add_argument("output_directory")
	args = parser.parse_args()

	output_directory = Path(args.output_directory)
	output_directory.mkdir(parents=True, exist_ok=True)

	count = 0
	with open(output_directory.joinpath("1ssss"), "w") as _1ssss, \
		open(output_directory.joinpath("1spss"), "w") as _1spss, \
		open(output_directory.joinpath("1spsp"), "w") as _1spsp, \
		open(output_directory.joinpath("1spps"), "w") as _1spps, \
		open(output_directory.joinpath("1sppp"), "w") as _1sppp:
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

			count = count + 1
			if count >= 10000:
				break

	count = 0
	with open(output_directory.joinpath("2sss"), "w") as _2sss, \
		open(output_directory.joinpath("2sps"), "w") as _2sps, \
		open(output_directory.joinpath("2spp"), "w") as _2spp:
		for phrase in subject_with_adjunct:
			_2sss.write(phrase.generate_string())
			_2sss.write("\n")

			_2sps.write(phrase.generate_string(arguments={phrase.subject_noun_phrase: {"arguments": {phrase.subject_noun_phrase.adjuncts[0]: {"singular": False}}}}))
			_2sps.write("\n")

			_2spp.write(phrase.generate_string(singular=False, arguments={phrase.subject_noun_phrase: {"arguments": {phrase.subject_noun_phrase.adjuncts[0]: {"singular": False}}}}))
			_2spp.write("\n")

			count = count + 1
			if count >= 10000:
				break

	count = 0
	with open(output_directory.joinpath("3ssss"), "w") as _3ssss, \
		open(output_directory.joinpath("3spss"), "w") as _3spss, \
		open(output_directory.joinpath("3spsp"), "w") as _3spsp, \
		open(output_directory.joinpath("3spps"), "w") as _3spps, \
		open(output_directory.joinpath("3sppp"), "w") as _3sppp:
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

			count = count + 1
			if count >= 10000:
				break

if __name__ == "__main__":
	main()