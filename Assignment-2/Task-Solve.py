# Module 2_Assignment

fruits = ["apple","banana","cherry"]

#Adding orange at the end
fruits.append("orange")

#Removing banana from the list
fruits.remove("banana")

#Sorting the list alphabetically
fruits.sort()

#Printing the final list
print(fruits)

#Printing the length of the list
print("Length of the list is ",len(fruits))


#Dictionary
student = {
    "name":"Durjoy",
    "age":24,
    "grade":3.64
}

#new city key value pair
student["city"]="Dhaka"

#Update grade with new value
student["grade"]=3.45

#Print Keys
print(student.keys())

#Print final dictionary
print(student)


#Function to calculate discounted price
def calculate_total(price, quantity, discount=0):
    initial_price = price*quantity
    discount=((initial_price*discount)/100)
    final_price = initial_price-discount
    return final_price


print(calculate_total(100, 2, 10))