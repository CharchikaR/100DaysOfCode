# Input a list of student scores
# eg 78 65 89 86 55 91 64 89
student_scores = input().split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

score_max = 0
index = 0

for x in student_scores:
  
  if score_max > student_scores[index]:
    score_max = score_max
  else: 
    score_max = student_scores[index]
  index += 1
  
print(f"The highest score in the class is: {score_max}")
 