# acivity for errors

class FileManipulator:
    def __init__(self, file_name):
        self.contents = None
        self.my_file = None
        while self.contents == None:
            try:
                self.my_file = open(file_name, 'r') # Open a file for reading.
                self.contents = self.my_file.readlines() # Read in the content by line.
            except (FileNotFoundError, TypeError, OSError) as e:
                print(f"Input file not found or misconfigured. {e}")
                file_name = input("Please enter the name of the file you would like to read: ")
            else:
                print(self.contents) #print the contents of the file
                self.my_file.close() # Explicitly close the file

    def reverse(self, new_filename):
        try:
            new_file = open(new_filename, "w")
            string_contents = [self.contents[::-1] for char in self.contents]
            reversed = self.contents[::-1]
            new_file.write(reversed)
        except (FileNotFoundError, TypeError, OSError) as e:
            print(f"Input file not found or misconfigured. {e}")

f = FileManipulator("tmp.csv")
f.reverse("tmp2.txt")
'''
test code:

f = FileManipulator("tmp.txt")
print(f.contents)
f.reverse("tmp2.txt")
'''