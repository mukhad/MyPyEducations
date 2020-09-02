import os
import time

# Небольшая программа для переименования фоток по дате их создания.
# Нужна была, чтобы улучшить просмотр фотографий, которые были сняты на разные телефоны и фотоаппараты в разное время.
# В результате в начало имени файла добавляется строка содержащая дату создания файла в формате "р_год_месяц_день_час_минута___"

photodirname = "psort"

print("renaming photo in ", photodirname)

print(os.listdir(photodirname))

for file in os.listdir(photodirname):
    fn = os.path.join(photodirname, file)
    t = os.path.getmtime(fn)
    s1 = photodirname + "\p_" + time.strftime("%Y_%m_%d_%H_%M", time.localtime(t)) + "___" + file
    try:
        os.rename(fn, s1)
    except OSError:
        print("file rename error")
    else:
        print(fn, "\t", s1)
