SQL запросы:

Задание 1
```
SELECT c.login,
       COUNT(o.id) AS orders_in_delivery
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = TRUE
GROUP BY c.login;
```
<img width="581" height="370" alt="Задание 1" src="https://github.com/user-attachments/assets/d7cb6d8d-26cd-4b7c-abad-a6c45185ec0b" />


Задание 2
```
SELECT track AS order_tracker,
       CASE
           WHEN finished = TRUE THEN 2
           WHEN cancelled = TRUE THEN -1
           WHEN "inDelivery" = TRUE THEN 1
           ELSE 0
       END AS status
FROM "Orders";
```
<img width="721" height="496" alt="Задание 2" src="https://github.com/user-attachments/assets/f88f4ab7-b054-4964-b31a-4e121dc5cac8" />

Запуск теста через терминал
<img width="1920" height="1040" alt="Запуск через терминал" src="https://github.com/user-attachments/assets/9c4b5c02-7de6-44a3-8621-92012193cc21" />

Запуск теста через тестранера

<img width="1920" height="1040" alt="Запуск через тестраннер" src="https://github.com/user-attachments/assets/71291135-0ca3-471a-9306-9e77c933e736" />




  
