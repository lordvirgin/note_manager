username = input("Введите имя пользователя: ")
content = input("Введите содержание заметки: ")
status = input("Введите статус: ")
date_created = input("Дата создания: ")
issue_date = input("Дата изменения: ")
title1 = input("Напишите заголовок: " )
title2 = input("Напишите заголовок:" )

note = [
username,
content,
status,
date_created,
issue_date,
[title1,
title2]
]
print("Имя пользователя: ",note[0])
print("Описание заметки: ",note[1])
print("Статус заметки: ",note[2])
print("Дата создания: ",note[3])
print("Дата истечения: ",note[4])
print("Заголовки: ",note[5])
