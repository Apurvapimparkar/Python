#excercise-4

#Program-1
#length=eval(input('Enter length in centimeters: '))
#if length<0:
#    print('Entry is invalid')
#else:
#    print('length in inches is:', (length/2.54))

#Program-2
#temp=eval(input('Enter the temperature value: '))
#unit=eval(input('Which Unit? Type 1 for Celcius and 2 for Fahrenheit :'))
#if unit==1:
#    print('Temperature in Fahrenheit is: ', ((9/5)*unit+32))
#else:
#    print('Temperature in Celcius is: ', ((5/9)*(unit-32)))

#Program-3
#temp=eval(input('Enter the temperature in celcius: '))
#if temp<-273.15:
#    print('Temp is invalid')
#elif temp==(-273.15):
#    print('Temp is absolute 0')
#elif -273.15<temp<0:
#    print('Temp is below feezing')
#elif temp==0:
#    print('Temp is at the freezing point')
#elif 0<temp<100:
#    print('Temp is in the normal range')
#elif temp==100:
#    print('Temp is at the boiling point')
#elif temp>100:
#    print('Temp is above the bopiling point')


#Program-4
#from random import randint
#num=str(randint(1,10))
#guess=input('Enter your guess: ')
#if num==guess:
#    print('You got it right')
#else:
#    print('try again, the number is', num)

#Program-5
#items=eval(input('How many items are you buying: '))
#if items<10:
#    print('Total cost of items : ', items*12,'$')
#elif 10<=items<=99:
#    print('Total cost of items : ', items*10,'$')
#elif items>100:
#    print('Total cost of items : ', items*7,'$')

#Program-6
#cred=eval(input('How many credit are you taking: '))
#if cred<=23:
#    print('Student is a freshman')
#elif 24<=cred<=53:
#    print('Student is a sophomore')
#elif 54<=cred<=83:
#    print('Student is a junior')
#else:
#    print('Student is a senior')

#Program-7
#num1=eval(input('Enter first number: '))
#num2=eval(input('Enter second number: '))
#if abs((num1-num2))>0.001:
#    print('Not close!')
#else:
#    print('close')

#Program-8
#year=eval(input('Enter any year: '))
#if (year%4==0) or (year%400==0):
#    print('This year is a leap year')
#else:
#    print('This year is not a leap year')


#Program-9
#num=eval(input('Enter a number: '))
#for i in range(1,50):
#    if num%i==0:
#        print('Divisor of the given number are: ', i)

#Program-10
#from random import randint
#for i in range(1,10):
#    num1=randint(1,10)
#    num2=randint(1,10)
#    print('Question no.', i,':', (num1), 'x', (num2))
#    ans=eval(input('Enter your answer: '))
#    if ans==(num1*num2):
#        print('Right!')
#    else:
#        print('Wrong! The correct ans is :', num1*num2)
        
#Program-11
#hr=eval(input('Enter any hour between 1 to 12: '))
#am=eval(input('am (1) or pm (2) ? '))
#ahead=eval(input('How many hours ahead: '))
#newhour=((hr+ahead)-12)
#if am==1 and newhour<0:
#    print('New hour: ', (hr+ahead), 'am')
#elif am==2 and newhour<0:
#    print('New hour: ', (hr+ahead), 'pm')
#elif am==1 and newhour>0:
#    print('New hour: ', abs(newhour), 'pm')
#elif am==2 and newhour>0:
#    print('New nour: ', abs(newhour), 'am')




    





























