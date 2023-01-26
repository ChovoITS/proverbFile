#Functions that open a file in read mode
import os
import sys

def fileOpen(filePath):
    with open(os.path.join(os.path.abspath('./docs'), filePath), 'r') as f:
        lines = f.readlines()
    return lines

#Functions that open a file in write mode and write the text in input
def writeToFile(filePath, textToWrite):
    #Try except to prevent not existing files
    try:
        f = open(os.path.join(os.path.abspath('./docs'), filePath), 'a')
    except FileNotFoundError:
        f = open(os.path.join(os.path.abspath('./docs'), filePath), 'x') #File is not existing
    except:
        print("Error reading file") #Generic error
    else:
        f = open(os.path.join(os.path.abspath('./docs'), filePath), 'a') #File is existing
    finally:
        f.write(textToWrite)
        f.close()
    

def main():
    linesProverb = fileOpen("proverbFile.txt")
    for line in linesProverb:
        for charIndex in range(len(line)):
            if line[charIndex] != ' ':
                if charIndex % 2 == 0: #Even
                    writeToFile("file_proverb_even.txt", line[charIndex])
                elif charIndex % 2 == 1:#Odd
                    writeToFile("file_proverb_odd.txt", line[charIndex])

#This is a condition statement that that checks whether the value of the variable __name__ is equal to the string "__main__"
#This is the case when you run your Python file as a script from the command line
if __name__ == "__main__":
    main()