# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Hn4wysSGWlRNKpybShXcQiYXziUqnbVk
"""

18

import pandas as pd

#1. DataFrame yaratish

data = { 'Ism': ['Ali', 'Vali', 'Sardor'], 'Yoshi': [25, 30, 221, 'Shahar': ['Toshkent', 'Samarqand', 'Buxoro']

}

df pd.DataFrame(data)

#2. Ma'lumotlarni ko'rish

print(df)

I

#3. Filtrlash

young_people df [df['Yoshi'] < 30] print("30 yoshdan kichiklar:\n", young_people)

#4. O'zgartirish df['Yoshi'] += 1 # Har bir shaxsning yoshini 1 ga oshirish print("Yangilangan DataFrame:\n", df)

5. CSV formatda saqlash df.to_csv('data.csv', index=False)

Ism Yoshi

Ali

25

Toshkent

Vali

30

Samarqand

22

Shahar

Buxoro

30 yoshdan kichiklar:

Ism Yoshi

Shahar

0

1

2 Sardor

Ali

25

Toshkent

2 Sardor

22

0

Buxoro

Yangilangan DataFrame:

Ism Yoshi

Shahar

Ali

26

Toshkent

Vali

31

Samarqand

23

0

1

2 Sardor

Buxoro