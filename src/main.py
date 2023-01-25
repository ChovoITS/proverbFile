def fileOpen(filePath):
    with open(filePath, 'r') as f:
        lines = f.readlines()
    return lines

def main():
    linesProverb = fileOpen("proverbFile/proverb.txt")

if __name__ == "__main__":
    main()