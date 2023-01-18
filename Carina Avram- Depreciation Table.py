#This progam is for displaying depreciation for a capital asset

def main():
    #Declare variables and initialize
    item = ""
    purYr = 0
    cost = 0.00
    numYrs = 0
    salvageVal = 0.00
    
    #Get Input
    item, purYr, cost, salvageVal, numYrs = GetInput (item, purYr, cost, salvageVal, numYrs)
    
    #Processing and output
    RestateInput(item, purYr, cost, salvageVal, numYrs)
    ShowHeadingsOutput()
    ShowDepreciationOutput(numYrs, salvageVal, cost, purYr)
    
    input("\n\nPress enter to continue...")

def GetInput (item, purYr, cost, salvageVal, numYrs):
    #This function gets the correct input from the user by utilizing the exception handling
    while True:
        try:
            print("\n\n\t***Please enter the data below. Make sure to enter numeric data and do not leave blank***")
            item = str(input("\nEnter name of item: "))
            purYr = int(input("Enter year purchased: "))
            cost = float(input("Enter cost: $"))
            salvageVal = float(input("Enter salvage value of item: $"))
            numYrs = int(input("Enter estimated life (in years): "))
        except ValueError:
            print("\n\tSOME INPUT YOU ENTERED WAS NON-NUMERIC. PLEASE ENTER INPUT AGAIN")
            continue
        else:
            break
    return item, purYr, cost, salvageVal, numYrs

def RestateInput(item, purYr, cost, salvageVal, numYrs):
    #This function restates the input entered by the user
    print("\n\n\n")#Start of output to restate input
    print("\t\t\tDescription:", item)
    print("\t\t\tYear of purchase:", purYr)
    print("\t\t\tCost: ${0:,.2f}".format(cost))
    print("\t\t\tSalvage Value: ${0:,.2f}".format(salvageVal))
    print("\t\t\tEstimated life:", numYrs, "years")
    print("\t\t\tMethod of depreciation: Straight-Line")

def ShowHeadingsOutput():
    #This function shows the headings of the depreciation table
    print("\n\t\t\t   DEPRECIATION TABLE")#Start of output for depreciation table headings
    print("\t\t\t   ------------------")
    print("{0:5s} {1:>12s} {2:>15s} {3:>18s}{4:>18s}".format("", "Beginning", "Amount of", "Total   ", " Ending"))
    print("{0:5s} {1:>12s} {2:>15s} {3:>18s}{4:>18s}".format("Year  ", "Value  ", "Depreciation", "Depreciation", "Value "))
    print("{0:5s} {1:>12s} {2:>15s} {3:>18s}{4:>18s}".format("-----", "  ----------", "    -------------", "   ---------------", "    -------------"))

def ShowDepreciationOutput(numYrs, salvageVal, cost, purYr):
    #This function gives the output of the depreciation table
    #Declare local variables
    slDep = 0.00
    beginValue = 0.00 #I initialize this variable here, so it doesn't need to be in the main function since it is not used there.
    totalDep = 0.00
    slDep = CalculateStraightLineDep(slDep, cost, salvageVal, numYrs) #This is an additional function that was not required in the assignment.
                                                                      
    beginValue = cost #This line of code needs to be written before the loop, so the beginning value starts with the cost (input from the user),
                      #and after that it is updated in the loop. 
    for i in range(numYrs):#Loop for depreciation
        
        totalDep = CalculateTotalDep(totalDep, slDep) #This function is needed to be placed here
                                                      #in order for the loop to acumulate the total depreciation for each year
                                                      #(cannot be placed inside of the format function like the 'CalculateEndingValue' function )
        print("{0:<5d} {1:12,.2f} {2:15,.2f} {3:18,.2f} {4:18,.2f}".format(purYr + i, beginValue, slDep, totalDep,
                                                                           CalculateEndingValue(beginValue, slDep))) #Loop output each time through loop
        beginValue =  beginValue - slDep #Calculate beginning value for next time through the loop

def CalculateStraightLineDep(slDep, cost, salvageVal, numYrs):
    #This function calculates the straight line depreciation
    #This function is not required in the assignment, but I thought will be good to have the straight line depreciation calculation in a function.
    slDep = (cost - salvageVal) / numYrs 
    return slDep

def CalculateTotalDep(totalDep, slDep):
    #This function calculates the total depreciation for the output table
    #In the instructions of the assignment, this function along with CalculateEndingValue function should be in the same function.
    #However, I preferred to split them in order to have a more efficient code.
    totalDep = totalDep + slDep #Calculate total depreciation each time through the loop
    return totalDep

def CalculateEndingValue(beginValue, slDep):
    #This function calculates the beginning value for the output table
    #In the instructions of the assignment, this function along with CalculateTotalDep function should be in the same function.
    #However, I preferred to split them, so I can initialize the endValue variable local to this function (since it is not needed anywhere else).
    #Declare local variables
    endValue = 0.00
    endValue = beginValue - slDep #Calculate ending value each time through the loop
    return endValue

main()



