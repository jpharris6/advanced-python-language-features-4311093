# Example file for Advanced Python: Language Features by Joe Marini
# demonstrate template string functions
from string import Template


# Usual string formatting with f-strings
str1 = "Advanced Python: Language Features"
str2 = "Joe Marini"
outputstr = f"You're watching {str1} by {str2}"
print(outputstr)

# TODO: create a template with placeholders
temp1 = Template("You're watching ${title} by ${author}")

# TODO: use the substitute method with keyword arguments
str2 = temp1.substitute(title="Advanced Python: Language Features",
                        author="Joe Marini")
print(str2)

# TODO: use the substitute method with a dictionary
data = {
    "author": "Joe Marini",
    "title": "Advanced Python: Language Features"
}
str3 = temp1.substitute(data)
print(str3)