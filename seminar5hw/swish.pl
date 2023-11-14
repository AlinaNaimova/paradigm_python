% Определение предиката для вычисления суммы элементов списка
sum_list([], 0). % Базовый случай: сумма пустого списка равна 0
sum_list([Head|Tail], Sum) :-
    sum_list(Tail, TailSum), % Рекурсивно вычисляем сумму оставшейся части списка
    Sum is Head + TailSum. % Сумма списка равна сумме головы и суммы оставшейся части списка