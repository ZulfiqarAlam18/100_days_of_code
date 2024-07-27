

name = "Zulfiqar Alam Jamali"
vowels = "aeiou"
count = 0
vowel_list = []

for i in name:
 if i.lower() in vowels:
        vowel_list.append(i)
        count += 1

print(count)
print(vowel_list)