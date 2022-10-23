# Задача:
# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


def find_pi():
    _pi = 0
    _list = [i for i in range(1, 100000) if i % 2]  # 1 0  3 1  5 2  7 3  9 4
    step = 0
    last_pi = 0
    for i in _list:
        last_pi = _pi
        if step % 2 == 0:
            _pi = _pi + (1 / i)
        else:
            _pi = _pi - (1 / i)
        step += 1
        if abs(last_pi * 4 - _pi * 4) < 0.001:
            print(
                f"Шаг итерации, когда заданая точность была равна условию задачи>> {step}"
            )
            break
    return _pi * 4


print(find_pi())
