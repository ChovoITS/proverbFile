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
    writeToFile("proverbFile/file_proverb_even.txt", "Test")

if __name__ == "__main__":
    main()