if __name__ == '__main__': 
    numDays = int(input('number of days?\n')) 
    total = 0
    strInput =  str(numDays)
    temperatures = []
    totalDays = 0
    for i in range(1, numDays+1):
        nextDay = int(input('enter day'+str(i)+'high temp: '))
        temperatures.append(nextDay)
        total = total + nextDay
    averageTemp = round(total/numDays, 2)
    print('Avg temp is ' + str(averageTemp))  
    for temp in temperatures:
        if temp > averageTemp:
            totalDays += 1

    print(str(totalDays) +"day(s) exceed the avg temp")


