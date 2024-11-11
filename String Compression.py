class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0  # Where to write the compressed result
        read_index = 0  # Pointer to read through the input characters
        
        while read_index < len(chars):
            current_char = chars[read_index]  # Character being processed
            count = 0  # Count occurrences of the current character
            
            # Count the number of consecutive occurrences of current_char
            while read_index < len(chars) and chars[read_index] == current_char:
                read_index += 1
                count += 1
            
            # Write the character to the compression position
            chars[write_index] = current_char
            write_index += 1
            
            # If the count is greater than 1, write the count as individual digits
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1
        
        return write_index