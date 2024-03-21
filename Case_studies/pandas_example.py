
import seaborn as sns
#Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.

df = sns.load_dataset("titanic")
print(df.head())

#Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.

print(df.sex.value_counts())
# Toplam yolcu sayısı
print(df.shape[0])

#Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.

print(df.nunique())

#Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.

print(df.pclass.unique().shape[0])

#Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.

print(df[['pclass', 'parch']].nunique())

#Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.



print(df.embarked.dtype)
df.embarked = df.embarked.astype('category')
print(df.embarked.dtype)

#Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.

print(df.query("embarked == 'C'"))

#Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.

print(df.query("embarked != 'S'"))

#Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

print(df.query("age < 30 and sex == 'female'"))

#Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz

print(df.query("fare > 500 or age > 70"))

#Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.

print('Question 11')
print(df.isnull().sum())

#Görev 12: who değişkenini dataframe’den çıkarınız.

print('Question 12')
# who değişkenini dataframe'den silme
df = df.drop('who', axis=1)

print('who' in df.columns)

#Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.

print('Question 13')
# deck değişkeninin en çok tekrar eden değerini (mode) bulma.
deck_mode = df.deck.mode()[0]

# deck değişkenindeki boş değerleri mode ile değiştirme.
df.deck.fillna(deck_mode, inplace=True)

# Check etme .
print(df.deck.isnull().sum())

#Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.

print('Question 14')
# age değişkeninin medyanını bulur.
age_median = df.age.median()

# age değişkenindeki boş değerleri medyan ile doldurur.
df.age.fillna(age_median, inplace=True)

# age değişkeninde boş değer olup olmadığını kontrol eder.
print(df.age.isnull().sum())

#Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.

print('Question 15')

print(df.pivot_table(values='survived', index='sex', columns='pclass', aggfunc=['sum', 'count', 'mean']))

#Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)

print('Question 16')


df['age_flag'] = df.age.apply(lambda age: 1 if age < 30 else 0)

# age_flag değişkeninin ilk 5 satırını gösterme
print(df.age_flag.head())


#Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.

print('Question 17')
tips = sns.load_dataset("tips")

print(tips.head())

#Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

print('Question 18')


print(tips.pivot_table(values='total_bill', index='time', aggfunc=['sum', 'min', 'max', 'mean']))

#Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz

print('Question 19')
print(tips.pivot_table(values='total_bill', index='day', columns='time', aggfunc=['sum', 'min', 'max', 'mean']))

#Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.

print('Question 20')

# Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerini day'e göre özetleme
df_lunch_female = tips.loc[(tips['time'] == 'Lunch') & (tips['sex'] == 'Female')]
df_lunch_female_summary = df_lunch_female.pivot_table(values=['total_bill', 'tip'], index='day', aggfunc=['sum', 'min', 'max', 'mean'])


print(df_lunch_female_summary)


#Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)

print('Görev 21')

average_of_filtered_orders = tips.loc[(tips['size'] < 3) & (tips['total_bill'] > 10), 'total_bill'].mean()
print("Görev 21 Ortalama:", average_of_filtered_orders)

#Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.


print('Görev 22')

# Her bir müşterinin ödediği totalbill ve tip in toplamını veren yeni bir değişken oluşturma

tips['total_bill_tip_sum'] = tips['total_bill'] + tips['tip']

#Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.



print('Görev 23')

sorted_df = tips.sort_values(by='total_bill_tip_sum', ascending=False).head(30)
print("Görev 23 İlk 30 Kişi:")
print(sorted_df)