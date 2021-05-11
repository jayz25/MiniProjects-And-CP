import sys
# You may change this function parameters
def findMaxProfit(numOfPredictedDay, predictedSharePrices):
    # Participants code will be here
    print(predictedSharePrices[:numOfPredictedDay])
    m1 = min(predictedSharePrices[:numOfPredictedDay])
    m2 = max(predictedSharePrices[m1:numOfPredictedDay])
    i = predictedSharePrices.index(m1)
    #print(predictedSharePrices[i+1:numOfPredictedDay])
    
    return m2-m1


def main():
    line = input().split()
    numOfPredictedDay = int(line[0])
    predictedSharePrices = list(map(int, line[1:]))
    print(predictedSharePrices)

    answer = findMaxProfit(numOfPredictedDay, predictedSharePrices)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()