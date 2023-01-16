"""
Complete the script.
"""
temp1 = int(input('Enter a temperature: '))
temp2 = int(input('Enter another temperature: '))
temp3 = int(input('Enter a third temperature: '))
sum = temp1 + temp2 + temp3
avg = round(sum / 3)
pro = temp1 * temp2 * temp3
minimum = min(temp1, temp2, temp3)
maximum = max(temp1, temp2, temp3)

print('The sum of the three tempertures is ', sum)
print('The average temperature is ', avg)
print('The product of the three temperatues is ', pro)
print("The minimum temperature is", minimum)
print('The maximum temperature is ', maximum)
print('The range of temperatures is ', minimum, '-', maximum)

if temp3 < 0:
    print('Watch for ice')
elif temp3 in range(0,22):
    print('Bring a jacket')
elif temp3 in range(23-26):
    print("It's beautiful today")
elif temp3 > 23:
    print('Bring sunscreen')