def file_reader(filepath):
    '''Opens a given filepath and returns file content.'''
    with open(filepath, "r") as file:
            file_content = file.read()
    return file_content

def file_line_reader(filepath):
      '''Opens a given filepath and returns the file content line by line as an iterable.'''
      with open(filepath, "r") as file:
            for line in file:
                  yield line.rstrip('\n')

      