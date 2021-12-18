from numpy import sign

if __name__ == "__main__":
    x_min = 124
    x_max = 174
    y_min = -123
    y_max = -86

    best_max = 0
    best_y = 0
    best_x = 0
    counter = 0
    for xv0 in range(0, x_max + 1):
        for yv0 in range(y_min, 400):
            xv = xv0
            yv = yv0
            x = 0
            y = 0
            max_reached_y = 0
            for i in range(700):
                if xv == 0 and x < x_min:
                    break
                if x > x_max:
                    break
                if y < y_min:
                    break
                x += xv
                y += yv
                xv -= sign(xv)
                yv -= 1
                max_reached_y = max(max_reached_y, y)
                if x_min <= x <= x_max and y_min <= y <= y_max:
                    counter += 1
                    if max_reached_y > best_max:
                        best_max = max_reached_y
                        best_x = xv0
                        best_y = yv0
                    break
    print(f"Part 1: Best max of {best_max} at ({best_x}, {best_y})")
    print(F"Part 2: {counter}")
