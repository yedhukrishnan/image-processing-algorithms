import math
from bitarray import bitarray

class LZ77Compressor:
	MAX_WINDOW_SIZE = 400

	def __init__(self, window_size=20):
		self.window_size = min(window_size, self.MAX_WINDOW_SIZE)
		self.lookahead_buffer_size = 15 # length of match is at most 4 bits

	def compress(self, data, output_file_path=None, verbose=False):
		i = 0
		output_buffer = bitarray(endian='big')

		while i < len(data):
			#print i
			match = self.findLongestMatch(data, i)

			if match:
				# Add 1 bit flag, followed by 12 bit for distance, and 4 bit for the length
				# of the match
				(bestMatchDistance, bestMatchLength) = match

				output_buffer.append(True)
				output_buffer.frombytes(chr(bestMatchDistance >> 4))
				output_buffer.frombytes(chr(((bestMatchDistance & 0xf) << 4) | bestMatchLength))

				print "<1, %i, %i>\n" % (bestMatchDistance, bestMatchLength),

				i += bestMatchLength

			else:
				# No useful match was found. Add 0 bit flag, followed by 8 bit for the character
				output_buffer.append(False)
				output_buffer.frombytes(data[i])

				print "<0, 0, %s>\n" % data[i],

				i += 1

		# fill the buffer with zeros if the number of bits is not a multiple of 8
		output_buffer.fill()

		# write the compressed data into a binary file if a path is provided
		try:
			with open('output.txt', 'wb') as output_file:
			    	output_file.write(output_buffer.tobytes())
			    	return None
		except IOError:
		    	print 'Could not write to output file path. Please check if the path is correct ...'
		    	raise

		# an output file path was not provided, return the compressed data
		return output_buffer


        def decompress(self, input_file_path='output.txt', output_file_path=None):
		data = bitarray(endian='big')
		output_buffer = []

		# read the input file
		try:
			with open(input_file_path, 'rb') as input_file:
				data.fromfile(input_file)
		except IOError:
			print 'Could not open input file ...'
			raise

		while len(data) >= 9:

			flag = data.pop(0)

			if not flag:
				byte = data[0:8].tobytes()

				output_buffer.append(byte)
				del data[0:8]
			else:
				byte1 = ord(data[0:8].tobytes())
				byte2 = ord(data[8:16].tobytes())

				del data[0:16]
				distance = (byte1 << 4) | (byte2 >> 4)
				length = (byte2 & 0xf)

				for i in range(length):
					output_buffer.append(output_buffer[-distance])
		out_data =  ''.join(output_buffer)

		if output_file_path:
			try:
				with open(output_file_path, 'wb') as output_file:
					output_file.write(out_data)
					print 'File was decompressed successfully and saved to output path ...'
					return None
			except IOError:
				print 'Could not write to output file path. Please check if the path is correct ...'
				raise
                print out_data
		return out_data


	def findLongestMatch(self, data, current_position):
		"""
		Finds the longest match to a substring starting at the current_position
		in the lookahead buffer from the history window
		"""
		end_of_buffer = min(current_position + self.lookahead_buffer_size, len(data) + 1)

		best_match_distance = -1
		best_match_length = -1

		# Optimization: Only consider substrings of length 2 and greater, and just
		# output any substring of length 1 (8 bits uncompressed is better than 13 bits
		# for the flag, distance, and length)
		for j in range(current_position + 2, end_of_buffer):

			start_index = max(0, current_position - self.window_size)
			substring = data[current_position:j]

			for i in range(start_index, current_position):

				repetitions = len(substring) / (current_position - i)

				last = len(substring) % (current_position - i)

				matched_string = data[i:current_position] * repetitions + data[i:i+last]

				if matched_string == substring and len(substring) > best_match_length:
					best_match_distance = current_position - i
					best_match_length = len(substring)

		if best_match_distance > 0 and best_match_length > 0:
			return (best_match_distance, best_match_length)
		return None


compressor = LZ77Compressor()
data = 'wabba wabba wabba wabba woo woo woo'
print "Compresing data: %s" % data

print "Compressed output: "
compressor.compress(data, verbose = True)

print "Decompressed output: "
compressor.decompress()
