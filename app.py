import pandas as pd
import numpy as np
import datetime

#Lütfen 2 Tarih Aralığını yyyy-aa-gg formatında giriniz.
#Tarih aralığı min = '2021-01-01'
#Tarih aralığı max = '2021-06-30' girilebilir
startDate = np.datetime64('2021-04-28')
stopDate = np.datetime64('2021-05-28')

#excell readfile
data = pd.read_excel("data.xlsx")
dataDate = np.array(data['Date'])
dataValue = np.array(data['Value'])
greatestValueDates  = []
smallestValueDates  = [] 

#başlangıç ve bitiş tarihlerinin indexini bulma
def searcIndex(startDate,stopDate):
    startIndex = int(np.where(dataDate == startDate)[0])
    stopIndex = int(np.where(dataDate == stopDate)[0])
    return startIndex,stopIndex

#indexlere göre minimum ve maksimum değerleri bulma. Minimum ve maximum değerlerin indexlerini bulma.
def searchValue(startIndex,endIndex):
    print()
    greatestValue = dataValue[startIndex:endIndex].max()
    smallestValue = dataValue[startIndex:endIndex].min()
    greatestValueIndex = np.where(dataValue[startIndex:endIndex] == greatestValue)[0] + startIndex + 1
    smallestValueIndex = np.where(dataValue[startIndex:endIndex] == smallestValue)[0] + startIndex + 1
    return greatestValue,smallestValue,greatestValueIndex,smallestValueIndex
    
#en büyük ve en küçük değerlerin indexine göre tarihi bulma
def searchDate(greatestValueIndex,smallestValueIndex):
    for index in greatestValueIndex:
        index -= 1
        greatestValueDates.append(dataDate[int(index)]) 
    for index in smallestValueIndex:
        index -= 1
        smallestValueDates.append(dataDate[int(index)])


#run
startIndex,endIndex = searcIndex(startDate,stopDate)
greatestValue,smallestValue,greatestValueIndex,smallestValueIndex = searchValue(startIndex,endIndex)
searchDate(greatestValueIndex,smallestValueIndex)

 

#print
print('Toplam  "',endIndex-startIndex+1,'"  Adet Sayı Vardır')
print('\n----------------------------------------------------------------------------\n')
print('İki Tarih Arasındaki En Büyük sayı : ',greatestValue,'\nIndex Bilgisi-leri : ',greatestValueIndex,'\nTam Tarih-ler : ',greatestValueDates, '\nGün-ler Sırayla :',pd.to_datetime(greatestValueDates).day)
print('\n----------------------------------------------------------------------------\n')
print('İki Tarih Arasındaki En Küçük sayı : ',smallestValue,'\nIndex Bilgisi-leri : ',smallestValueIndex,'\nTam Tarih-ler : ',smallestValueDates, '\nGün-ler Sırayla :',pd.to_datetime(smallestValueDates).day)
print('\n----------------------------------------------------------------------------')
