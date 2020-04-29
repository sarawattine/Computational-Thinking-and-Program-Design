# 1. 建立變數,輸入資料並儲存
minutes_convert = 133 #電影魔球時間長度(分鐘)
# 2. 方法(一)
## 變數轉換為小時數
hours_進位 = minutes_convert/60 #數學運算除以60
hours_部分 = int(hours_進位) #將浮點數結果轉換為整數
minutes_進位 = hours_進位 - hours_部分#浮點數減整數取得小數
minutes_部分 = round(minutes_進位*60) #小數乘60得分鐘數,但要四捨五入才行

# 2. 方法(二)
minutes_部分 = minutes_convert//60 #商數運算取得小時數
minutes_部分 = minutes_convert%60 #餘數運算取得分鐘數
print("Hours")
print(hours_部分)
print("Minutes")
print(minutes_部分)

print(minutes_to_convert)

