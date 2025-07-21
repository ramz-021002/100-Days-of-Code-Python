student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
#print(range(1, 10))

# sum = 0
# for score in student_scores:
#     sum =+ score
#
# print(sum)
ma = student_scores[0]
mi = student_scores[0]
for score in student_scores:
    if ma < score:
        ma = score

    if mi > score:
        mi = score

print(f"{ma} and {mi}")
