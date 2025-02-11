def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

'''
What is the key difference between these implementations?

The first implementation modifies the buffer in place every time when a new
element comes in. In contrast, for the second implementation, it creates a new
buffer every time when a new element comes in.
'''