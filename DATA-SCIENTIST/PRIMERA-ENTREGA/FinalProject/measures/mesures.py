import  pandas as pd


class Mesures:

    def studentsMesures(self):
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


        #students max scores
        studetMaxScores = dataFrame.loc[dataFrame["Exam_Score"] == maxScore]
        print("Stu max scores")
        print(studetMaxScores)

        #students min scores
        studentsMinScores = dataFrame.loc[dataFrame["Exam_Score"] == minScore]
        print("Stu min scores")
        print(studentsMinScores)
#-------------------------------------

def createRangeHours(self):
    dataframe = pd.read_csv("DataSet/StudentPerformanceFactors.csv")
    dataframe['Range_hours'] = pd.cut(
        dataframe['Hours_Studied'],
        bins=[0, 5, 9, 13,18,22,26, float('inf')],  # Límites de los rangos
        labels=['1-5 horas', '5-9 horas', '9-13 horas', '13-18 horas' ,'18-22 horas','22-26 horas' , 'Más de 26 horas'],  # Etiquetas
        right=False  # Incluye el límite inferior en el rango
    )