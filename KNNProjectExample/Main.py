import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
import pickle
import tkinter as tk
pencere=tk.Tk()
pencere.title("Diabet Bakım")
pencere.geometry("500x500")

def butonBas():
    y=np.array([[float(PregnanciesEntry.get()),float(GlucoseEntry.get()),float(BloodPressureEntry.get()),float(SkinThicknessEntry.get()),float(InsulinEntry.get()),float(BMIEntry.get()),float(DiabetesPedigreeFunctionEntry.get()),float(AgeEntry.get())]])
    y = (y - np.min(y))/(np.max(y)-np.min(y))
    mymodel=pickle.load(open("KNNDiabetModel.pickle","rb"))
    z=mymodel.predict(y)
    if(z[0]==1):
        sonuc["text"]="Hasta"
    else:
        sonuc["text"]="Sağlıklı"
    
Pregnancies=tk.Label(text="Pregnancies",font="Arial 12 bold")
Pregnancies.pack()
PregnanciesEntry=tk.Entry(width=30)
PregnanciesEntry.pack()
Glucose=tk.Label(text="Glucose",font="Arial 12 bold")
Glucose.pack()
GlucoseEntry=tk.Entry(width=30)
GlucoseEntry.pack()
BloodPressure=tk.Label(text="BloodPressure",font="Arial 12 bold")
BloodPressure.pack()
BloodPressureEntry=tk.Entry(width=30)
BloodPressureEntry.pack()
SkinThickness=tk.Label(text="SkinThickness",font="Arial 12 bold")
SkinThickness.pack()
SkinThicknessEntry=tk.Entry(width=30)
SkinThicknessEntry.pack()
Insulin=tk.Label(text="Insulin",font="Arial 12 bold")
Insulin.pack()
InsulinEntry=tk.Entry(width=30)
InsulinEntry.pack()
BMI=tk.Label(text="BMI",font="Arial 12 bold")
BMI.pack()
BMIEntry=tk.Entry(width=30)
BMIEntry.pack()
DiabetesPedigreeFunction=tk.Label(text="DiabetesPedigreeFunction",font="Arial 12 bold")
DiabetesPedigreeFunction.pack()
DiabetesPedigreeFunctionEntry=tk.Entry(width=30)
DiabetesPedigreeFunctionEntry.pack()
Age=tk.Label(text="Age",font="Arial 12 bold")
Age.pack()
AgeEntry=tk.Entry(width=30)
AgeEntry.pack()
sonuc=tk.Label(text="SONUC",font="Arial 12 bold")
sonuc.pack()
b1=tk.Button(text="GİRİŞ",bg="black",fg="white",font="Arial 20 bold",command=butonBas)
b1.pack()

pencere.mainloop()

