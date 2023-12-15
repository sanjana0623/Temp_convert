#!/usr/bin/env python
# coding: utf-8

# # Temperature Converter

# In[1]:


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    print("Welcome to Temperature Converter")
    print("Choose conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    while True:
        try:
            choice = int(input("Enter your choice (1 or 2): "))
            if choice not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Please enter 1 or 2.")

    while True:
        try:
            value = float(input("Enter the temperature value: "))
            break
        except ValueError:
            print("Please enter a valid numeric temperature.")

    if choice == 1:
        result = celsius_to_fahrenheit(value)
        print(f"{value} Celsius is equal to {result} Fahrenheit")
    else:
        result = fahrenheit_to_celsius(value)
        print(f"{value} Fahrenheit is equal to {result} Celsius")

# Run the temperature converter
temperature_converter()


# In[ ]:




