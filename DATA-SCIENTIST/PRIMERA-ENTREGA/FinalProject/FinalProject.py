
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from altair.vega import legend
from scipy.ndimage import label

dataFrame = pd.read_csv("DataSet/StudentPerformanceFactors.csv")

dataFrame["Id_student"] = range(1,len(dataFrame) + 1)
print(dataFrame)

studentsTotalWithMaxScore = dataFrame["Exam_Score"].value_counts()
#print(studentsTotalWithMaxScore)

# nullValue = dataFrame["Exam_Scrore"].isnull()

studentsTotal = dataFrame["Exam_Score"].count()
# print(studentsTotal)

minScore = dataFrame["Exam_Score"].min()
# print(minScore)

maxScore = dataFrame["Exam_Score"].max()
# print(maxScore)

studetMaxScores = dataFrame.loc[dataFrame["Exam_Score"] == maxScore]
print("Stu max scores")
print(studetMaxScores)

studentsMinScores = dataFrame.loc[dataFrame["Exam_Score"] == minScore]
print("Stu min scores")
print(studentsMinScores)
#---------------------------------------------------


dataFrame['Range_hours'] = pd.cut(
    dataFrame['Hours_Studied'],
    bins=[0, 5, 9, 13,18,22,26, float('inf')],  # Límites de los rangos
    labels=['1-5 horas', '5-9 horas', '9-13 horas', '13-18 horas' ,'18-22 horas','22-26 horas' , 'Más de 26 horas'],  # Etiquetas
    right=False
)

count_range = dataFrame['Range_hours'].value_counts().sort_index()
count_range.plot(kind='bar', color='skyblue', legend =False)
plt.title('Estudiantes por Rango de horas Estudiadas')
plt.xlabel('Rangos de Horas')
plt.ylabel('Número de Estudiantes')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#----------------------------------------------
dataFrame['Range_scores'] = pd.cut(
    dataFrame["Exam_Score"],
    bins = [0,50, 60, 65, 70, 80, float('inf')],
    labels = ['score 0-50','score 50-60','score 60-65','score 65-70','score 70-80','score mayor a 80'],
    right = False
)

count_scores = dataFrame['Range_scores'].value_counts().sort_index()
count_scores.plot(kind='bar', color='skyblue', legend =False)
plt.title('Estudiantes por rango de scores')
plt.xlabel('Rangos de Scores')
plt.ylabel('Número de Estudiantes')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
#--------------------------------------------------
scores_por_rango = dataFrame.groupby('Range_hours')['Exam_Score'].mean()


scores_por_rango.plot(kind='bar', color='orange', figsize=(10, 6))

plt.title('Promedio de Score por Rango de Horas Estudiadas en una semana')
plt.xlabel('Rango de Horas Estudiadas')
plt.ylabel('Score Promedio')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#-------------------------------------------------

dataFrame['Range_attendance'] = pd.cut(
    dataFrame["Attendance"],
    bins = [0,50, 60, 65, 70, 80, float('inf')],
    labels = ['Attendance 0-50','Attendance 50-60','Attendance 60-65','Attendance 65-70','Attendance 70-80','Attendance mayor a 80'],
    right = False
)
scores_attendance_by = dataFrame.groupby('Range_attendance')['Exam_Score'].mean()
scores_attendance_by.plot(kind='bar', color='green', figsize=(10, 6))
plt.title('Promedio de Score por Rango de asistencias en una semana')
plt.xlabel('Rango de asistencias')
plt.ylabel('Score Promedio')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
#-----------------------------------------------
plt.figure(figsize=(8, 6))
sns.boxplot(x="Distance_from_Home", y="Attendance", data=dataFrame, palette="Set2")

plt.title('Dispersión de Asistencias por Distancia')
plt.xlabel('Distancia')
plt.ylabel('Porcentaje de Asistencias')
plt.ylim(50, 100)
plt.tight_layout()
plt.show()