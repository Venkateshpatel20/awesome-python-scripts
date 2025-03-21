# f-strings useful for string formating
letter  = "Hey there iam {} and i love my counntry {}"
name = "venkatesh"
country = "India"
print(letter.format(country,name))
"""which gives 
Hey there iam India and i love my counntry venkatesh
which is  wrong 
so we use index here """
about ="Hey iam {0} and iam from {1}"
name = "venkatesh"
city = "Hyderabad"
print(about.format(city,name))#prints Hey iam Hyderabad and iam from venkatesh
#to avoid complex index based we can write like this
print(f"Hey iam from {country}  native of {city} and my name is {name}")
#Hey iam from India  native of Hyderabad and my name is venkatesh
price = 78.993
total = f"my price total price id {price:.0f} dollers"
print(total)
print(f"{2 * 60}",type(f"{{}}"))#120,<class 'str'>
# to print the {} in print statement
print(f"we can print curly braces also {{}}")
