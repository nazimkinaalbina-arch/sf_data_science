# "Игра угадай число 
# клмпьютер сам загажывает т сам угадывает"
import numpy as np
def random_predict(number: int=1) -> int:
    """_summary_

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        int: _description_
    """
    count = 0
    
    while True:
        count +=1
        predict_number = np.random.randint(1, 101) #предполагаемое число
        if number == predict_number:
            break
    return(count)

def score_game(random_predict) ->int:
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадал число в среднем за: {score}  попыток")
    return(score)
score_game(random_predict)



#print(f"Количество попыток: {random_predict(10)}" )