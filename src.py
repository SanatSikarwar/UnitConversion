import csv

print("Enter the Physical Quantity's number you want to change")
choice=int(input("Length=1; Mass=2; Pressure=3\n"))



if choice==1:
    with open ('lengthConversionTable.csv')as csvfile:
        readCSV=csv.reader(csvfile,delimiter=',')

        units=[]
        factors=[]

        for row in readCSV:
              unit=row[0]
              factor=float(row[1])

              units.append(unit)
              factors.append(factor)

        print(units)

        try:
            unit1=input('Enter a unit you want to change from\n')
            unit2=input('Enter a unit you want to change to\n')
            val=float(input('Enter the magnitude\n'))

            
            undex=units.index(unit1.lower())
            thefactor=(factors[undex])
          
            undex2=units.index(unit2.lower())
            thefactor2=(factors[undex2])
            
            m=(val/thefactor)
            n=(m*thefactor2)
            print(val,unit1,"=",n,unit2)
        except Exception as e:
            print(e)


if choice == 2:
    with open ('massConversionTable.csv')as csvfile:
        readCSV=csv.reader(csvfile,delimiter=',')

        units=[]
        factors=[]

        for row in readCSV:
              unit=row[0]
              factor=float(row[1])

              units.append(unit)
              factors.append(factor)

        print(units)

        try:
            unit1=input('Enter a unit you want to change from\n')
            unit2=input('Enter a unit you want to change to\n')
            val=float(input('Enter the magnitude\n'))

            
            undex=units.index(unit1.lower())
            thefactor=(factors[undex])
          
            undex2=units.index(unit2.lower())
            thefactor2=(factors[undex2])
            
            m=(val/thefactor)
            n=(m*thefactor2)
            print(val,unit1,"=",n,unit2)
        except Exception as e:
            print(e)

if choice==3:
    with open ('pressureConversionTable.csv')as csvfile:
        readCSV=csv.reader(csvfile,delimiter=',')

        units=[]
        factors=[]

        for row in readCSV:
              unit=row[0]
              factor=float(row[1])

              units.append(unit)
              factors.append(factor)

        print(units)

        try:
            unit1=input('Enter a unit you want to change from\n')
            unit2=input('Enter a unit you want to change to\n')
            val=float(input('Enter the magnitude\n'))

            
            undex=units.index(unit1.lower())
            thefactor=(factors[undex])
          
            undex2=units.index(unit2.lower())
            thefactor2=(factors[undex2])
            
            m=(val/thefactor)
            n=(m*thefactor2)
            print(val,unit1,"=",n,unit2)
        except Exception as e:
            print(e)

        else:
            print("Invalid Conversion")
