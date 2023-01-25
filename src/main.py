def fileOpen(filePath):
    with open(filePath, 'r') as f:
        lines = f.readlines()
    return lines

def writeToFile(filePath, textToWrite):
    try:
        f = open(filePath, 'a')
    except FileNotFoundError:
        f = open(filePath, 'x')
    except:
        print("Error reading file")
    else:
        f = open(filePath, 'a')
    finally:
        f.write(textToWrite)
        f.close()

def main():
    linesProverb = fileOpen("proverbFile/proverb.txt")
    for line in linesProverb:
        for charIndex in range(len(line)):
            if line[charIndex] != ' ':
                if charIndex % 2 == 0:
                    writeToFile("proverbFile/file_proverb_even.txt", line[charIndex])
                elif charIndex % 2 == 1:
                    writeToFile("proverbFile/file_proverb_odd.txt", line[charIndex])

if __name__ == "__main__":
    main()