#!/usr/bin/python3

"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if the given data set represents a valid UTF-8 encoding.
    """
    num_bytes = 0

    for byte in data:
        # Get the 8 least significant bits of the byte
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7) != 0:  # 1-byte character (0xxxxxxx) should start with 0
                return False
        else:
            # Check if the byte is a continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If num_bytes is not 0, then we have an incomplete character
    return num_bytes == 0
