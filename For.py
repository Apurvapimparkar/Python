#Exercise-1

#Program-1
for i in range(4):
    print('10'*5)

#Program-2
print('*'*10)
print('*',' '*6,'*')
print('*'*10)

#Program-3
for i in range(4):
    print('*'*(i+1))

#Program-4
print((512-282)/(47*48+5))

#Program-5
num=eval(input('Entera number: '))
print("Square of the number is", num**2, end='.')

#Program-6
num=eval(input('Entera number: '))
print(num, num*2, num*3, num*4, sep='---')

#Program-7
wt=eval(input('Enter your weight in kGs: '))
print('your weight in pounds: ', 2.2*wt)

#Program-8
num1=eval(input('Enter 1st number: '))
num2=eval(input('Enter 2nd number: '))
num3=eval(input('Enter 3rd number: '))
total = num1+num2+num3
average = total/3
print('Total of numbers is:', total, end='.')
print('Average of numbers is:', average, end='.')

#Program-9
price=eval(input('Enter price of a meal: '))
per_tip=eval(input('Enter tip in %: '))
tip=(per_tip/100)*price
total_bill=tip+price
print('tip is: ', tip,'.', 'Total bill is', total_bill, '.')


     
