def findmaxprofit(numOfPredictedTimes, predictedSharePrices):
    # [100,10,12,5,6,14,5,6]
    # [5,1,6,3,2,5,6,1,3,6,2,5,5,10]
    res=0
    r=predictedSharePrices[0]
    for i in range(numOfPredictedTimes):
        if(predictedSharePrices[i]>r and predictedSharePrices[i+1]<predictedSharePrices[i]):
            s+= predictedSharePrices[i] - r
            r = predictedSharePrices[i+1]

        

            











def find_min_days(prices,profit):
    for i in profit:
        for j in prices:
            if((prices.index(j+i)-prices.index(j))<min):
                min = (prices.index(j+i)-prices.index(j))