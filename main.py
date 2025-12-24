import heapq


def min_cost_cables(cables):
    """
    Для пошуку найдешевшого зʼєднання спочатку можна використовувати жадібний підхід 
    в якому будемо зʼєднувати кабелі від мінімальної довжини до максимальної.
    Це реалізовано за допомогою структури min-heap, де кореневий елемент завжди є мінімальним. 
    Тому, реалізація алгоритму пошуку манімальної вартості 
    буде заключатися в отриманні верхніх вузлів і додаванні їх по черзі одна до одної 
    та поверненні цієї суми назад у купу доти, доки не залишиться один кабель.
    """
    if not cables or len(cables) <= 1:
        return 0
    
    heap = cables.copy()

    # Створюємо структуру min-heap
    heapq.heapify(heap)
    
    total_cost = 0
    
    while len(heap) > 1:
        # Беремо два найкоротші кабелі
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        
        # Рахуємо вартість з'єднання
        cost = first + second
        total_cost += cost
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(heap, cost)
    
    return total_cost


if __name__ == "__main__":
    cables = [5,1,2,1]
    result = min_cost_cables(cables)
    print(f"Кабелі: {cables}")
    print(f"Мінімальні витрати: {result}")

