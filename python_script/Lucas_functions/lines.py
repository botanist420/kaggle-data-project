def slope(x1, y1, x2, y2):
    slope = (y2-y1) / (x2-x1)
    return slope

def intercept(slope, x2, y2):
    intercept = y2 - (slope * x2)
    return intercept


# x1, y1 = 0, 0
# x2, y2 = 3, 4

# print(f"point A: {x1}, {y1}")
# print(f"point B: {x2}, {y2}")

# result = slope(x1, y1, x2, y2)
# print(result)
# print('#'*22)
# print('line function as below:\n')
# print(f'y = {result}x + b')
# print(f'intercept = {y2} - {result} * {x2}')
# print(y2 - result * x2)

# slope_value = slope(x1, y1, x2, y2)
# intercept_value = intercept(slope_value, x2, y2)

# print(f'slope: {slope_value}')
# print(f'intercept: {intercept_value}')


if __name__ == "__main__":
    print('__name__ value:', __name__)
    print('This script is for calculating the slope and intercept')
    