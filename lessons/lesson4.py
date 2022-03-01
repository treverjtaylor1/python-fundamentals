# All about numbers
# numeric types are broken down into 3 distinct
# categories: int, float, & complex

# int in detail
val_int1 = 42
val_int2 = 8164888888
val_int3 = -4456889
val_int4 = 123456789123456789

# print values
print(val_int1)
print(val_int2)
print(val_int3)
print(val_int4)

# get the type of one of our values above

print(type(val_int4))
val_float1 = 3.14
val_float2 = 2.13456
val_float3 = -234.45

print(val_float1)
print(val_float2)
print(val_float3)

# scientific notation

val_float4 = 25E4
val_float5 = 42e9
val_float6 = -98.6e2

print(val_float4)
print(val_float5)
print(val_float6)

# get the type of a float value
print(type(val_float2))
val_complex = 3j
val_complex2 = -5j
print(val_complex)
print(val_complex2)

# the method below will convert an integer to different
# numeric system values
print(bin(22))
print(oct(22))
print(hex(22))

value = 0b10110
print(value)

# taking values that are strings and converting,
# while also converting
# numbers to string

value1 = float(34)
value2 = int(34.5)
value3 = str(89.3)
value4 = str(48)
value5 = int('45')
value6 = float('23.5')
print(value1,value2, value3, value4, value5, value6)

# input allows for users to provide information for us to use
name = input('What is your name')
movie = input('what is your favorite movie')

message = 'My name is {0} and my favorite movie is {1}'
print(message.format(name, movie))
