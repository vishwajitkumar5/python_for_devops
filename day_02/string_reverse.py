str = "kumar"
def reverse_string_without_function(str):
    str1 = ""
    for i in str:
        str1 = i+str1
    return str1    
    
def reverse_string_with_inbuild_function(str):
    str2 = ""
    str2 = str[::-1]
    return str2
print(str[::-1])
print(reverse_string_with_inbuild_function(str))
print(reverse_string_without_function(str))

