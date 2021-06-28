
import matplotlib.pyplot as plt

class Skew:

    def findMinSkewsIndices(self, chars):
        minIndices  = []
        skews = [len(chars)+1]
        skews[0] = 0
        currentMinValue = 0

        size = len(chars)
        x = range(size)
        for i in range(len(chars)):
            char = chars[i]
            if char == 'G':
                skews.append(skews[i] + 1);
            elif char  == 'C':
                last_skew = skews[i]
                skews.append(last_skew - 1);
                if skews[i+1] == currentMinValue:
                    minIndices.append(i+1)
                if skews[i+1] < currentMinValue:
                    currentMinValue = skews[i+1]
                    minIndices.clear()
                    minIndices.append(i+1)
            else:
                last_skew = skews[i]
                skews.append(last_skew)


        return minIndices, skews

    def findMinSkewsIndices(self, chars):
        minIndices  = []
        skews = [len(chars)+1]
        skews[0] = 0
        currentMinValue = 0

        size = len(chars)
        x = range(size)
        for i in range(len(chars)):
            char = chars[i]
            if char == 'G':
                skews.append(skews[i] + 1);
            elif char  == 'C':
                last_skew = skews[i]
                skews.append(last_skew - 1);
                if skews[i+1] == currentMinValue:
                    minIndices.append(i+1)
                if skews[i+1] < currentMinValue:
                    currentMinValue = skews[i+1]
                    minIndices.clear()
                    minIndices.append(i+1)
            else:
                last_skew = skews[i]
                skews.append(last_skew)


        return minIndices, skews

def main():

    text = None
    #with open("/Users/msalman/Downloads/dataset_7_10-2.txt", mode='r') as file :
    with open("/Users/msalman/Downloads/E_coli.txt", mode='r') as file :
        text = file.read()

    skew = Skew()
    # text = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
    minIndecis, skews = skew.findMinSkewsIndices(text)

    for indecis in minIndecis:
        print(indecis)

    plt.plot(skews)
    plt.show()


if __name__ == "__main__":
    main()



