import numpy as np
import binanceDataGathering
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

def PairsTradingChecker(cryptocurrency_1, cryptocurrency_2, interval):
    assetOne = np.zeros(500)
    assetTwo = np.zeros(500)
    hedgeRatio = 0.0


    ####################
    #Fill arrays "assetOne" and "assetTwo" with Close-Data of the cryptocurrencies
    binanceDataGathering.close_data(assetOne, cryptocurrency_1, interval)
    binanceDataGathering.close_data(assetTwo, cryptocurrency_2, interval)
    ####################


    ####################
    #Add constant value to array "assetTwo" to every value to make an OLS possible
    assetTwo = sm.add_constant(assetTwo)
    ####################


    ####################
    #Calculate beta of OLS between both arrays (is the hedge ratio)
    model = sm.OLS(assetOne,assetTwo)
    result = model.fit()
    #result.params[0] is alpha and result.params[1] is beta - we need only beta
    hedgeRatio = result.params[1]
    ####################


    ####################
    #Make an array "spreads"
    spreads = assetOne - hedgeRatio*assetTwo[:,1]
    ####################


    ####################
    #Test the array "spreads" for stationarity using ADF test
    adfResult = adfuller(spreads)
    if adfResult[0] < adfResult[4]["1%"]:
        print(cryptocurrency_1, "and", cryptocurrency_2, "are co-integrated (99% confidence interval).")
    elif adfResult[0] < adfResult[4]["5%"]:
        print(cryptocurrency_1, "and", cryptocurrency_2, "are co-integrated (only 95% confidence interval).")
    elif adfResult[0] < adfResult[4]["10%"]:
        print(cryptocurrency_1, "and", cryptocurrency_2, "are co-integrated (only 90% confidence interval).")
    else:
        print(cryptocurrency_1, "and", cryptocurrency_2, "are not co-integrated.")
    ####################


    ####################
    #Plotting both graphs in one window
    plt.plot(assetOne)
    #"assetTwo" is a 2 dim array because of the constant added before
    #But for plotting reasons we only need the second element (index 1) of every entry
    plt.plot(assetTwo[:,1]*hedgeRatio)
    plt.title(cryptocurrency_1 + " and " + cryptocurrency_2)
    plt.show()

    plt.plot(spreads)
    plt.hlines(y=np.mean(spreads), xmin=0, xmax=499)
    plt.title("Spread of " + cryptocurrency_1 + " and " + cryptocurrency_2)
    plt.show()
    ####################
