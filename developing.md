# Проектирование
## Для кого предназначено
Бот предназначен для осуществления оперативного доступа к списку товаров, на которые действует акция в магазинах сети
"Пятерочка" в формате csv, работа с которым в любом редакторе таблиц значительно проще и быстрее взаимодействия
с официальным сайтом. Пользоваться функционалом бота могут как обыватели, желающие получить актуальную информацию
об акциях в любом из магазинов страны (добавленных в базу бота), так и люди, заинтересованные в сборе статистики в сфере супер- и гипермаркетов.

## Функционал
После ввода команды `\start` пользователь получает на выбор список магазинов, имеющихся в базе бота, после нажатия
на которые будет произведен парсинг страницы со всеми акционными товарами в данном магазине, а затем составлен
и отправлен пользователю csv файл. Этот файл содержит информацию о товаре в формате 
`Наименование, Ссылка_на_изображение, Период_акции, Старая_цена, Новая_цена, Процент_скидки`.
