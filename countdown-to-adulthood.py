def diff(day_1, day_2):
  # 月数の差を求める
  if day_1.day >= day_2.day:
    return (day_1.year - day_2.year) * 12 + (day_1.month - day_2.month)
  else:
    return (day_1.year - day_2.year) * 12 + (day_1.month - day_2.month) - 1



# 標準入力
str = input('\n生年月日を8桁で入力してください (例:2005年1月23日の場合「20050123」と入力)\n→')
# 20050123

# 全角→半角の正規化処理
import unicodedata
normalize = unicodedata.normalize("NFKC", str)    # ２００５０１２３ >> 20050123


try:
  # 生年月日
  from datetime import datetime, date, timedelta
  birthday = datetime.strptime(normalize, '%Y%m%d') # 20050123 >> 2005-01-23 00:00:00

  # 誕生年 (1/1-3/31の場合便宜上前年生まれとして計算)
  # 生年月日から3か月の日付を求め、年のみ取り出す
  from dateutil.relativedelta import relativedelta
  b_fiscalyear = int(datetime.strftime(birthday - relativedelta(months=3), '%Y'))
  # 2005-01-23 >> 2004

  # 今日の日付
  import datetime
  today = datetime.datetime.now()
  today = today.replace(hour=0, minute=0, second=0, microsecond=0)

  # ～2002/3/31生まれの場合20歳で成人
  if b_fiscalyear <= 2001:
    adult = birthday + relativedelta(years=20)
  # 2004/4/1～生まれの場合18歳で成人
  elif b_fiscalyear >= 2004:
    adult = birthday + relativedelta(years=18)
  # 2002/4/1～2004/3/31生まれの場合2022/4/1をもって成人したとして計算
  else:
    adult = datetime.datetime(2022, 4, 1, 0, 0, 0)

  # 1行改行する
  print()

  # 月の差を求める
  from datetime import datetime, timedelta
  if today > adult:
    buf_diff = divmod(diff(today, adult), 12)
    d_diff = today - adult
    
    if buf_diff[0] == 0:
      if buf_diff[1] > 0:
        buf_msg = f"{buf_diff[1]}か月"
      else:
        buf_msg = f"{d_diff.days}日"
    else:
      buf_msg = f"{buf_diff[0]}年{buf_diff[1]}か月"
    
    print(f"成人してから{buf_msg}経過しました")
  elif today < adult:
    buf_diff = divmod(diff(adult, today), 12)
    d_diff = adult - today
    
    if buf_diff[0] == 0:
      if buf_diff[1] > 0:
        buf_msg = f"{buf_diff[1]}か月"
      else:
        buf_msg = f"{d_diff.days}日"
    else:
      buf_msg = f"{buf_diff[0]}年{buf_diff[1]}か月"
    
    print(f"成人するまであと{buf_msg}です")
  else:
    print("成人おめでとう!")


except:
  print('\n入力された値が正しくありません\n')