import pandas as pd 
from recommendation_system import recommend 
 
students = pd.read_csv("students.csv") 
courses = pd.read_csv("courses.csv") 
hits = 0 
total_students = len(students) 
 
print("MODEL EVALUATION") 
print("----------------") 
 
for index, student in students.iterrows(): 
    recommendations = recommend(student["interests"], student["level"], top_n=3) 
    recommended_course_names = recommendations["course_name"].tolist() 
    course_ids = [] 
    for name in recommended_course_names: 
        course_id = courses[courses["course_name"] == name]["course_id"].iloc[0] 
        course_ids.append(course_id) 
    target_course = student["target_course"] 
    if target_course in course_ids: 
        hits += 1 
 
print("Total students:", total_students) 
print("Successful recommendations:", hits) 
 
recall_at_3 = hits / total_students 
precision_at_3 = hits / (total_students * 3) 
 
if (precision_at_3 + recall_at_3) > 0: 
    f1_at_3 = 2 * (precision_at_3 * recall_at_3) / (precision_at_3 + recall_at_3) 
else: 
    f1_at_3 = 0.0 
 
print("\nRESULTS") 
print("-------") 
print("Precision@3:", round(precision_at_3, 3)) 
print("Recall@3:", round(recall_at_3, 3)) 
print("F1@3:", round(f1_at_3, 3)) 
