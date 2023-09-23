"""
The client
Estimated Time: 15 mins
Actual Time: 20 mins
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [python, ruby, visual_basic]

for language in languages:
    if language.is_dynamic():
        print(language)

new_languages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
for new_language in new_languages:
    if new_language.is_dynamic():
        print(new_language.name)
