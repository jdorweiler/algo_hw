\* min max line *\
Minimize
OBJ: W
Subject To
_C1: - C + Error + X_i = 3
_C10: - C + Error + 5 X_i = 11
_C11: Error - 5 X_i - 11 Y_i >= 0
_C12: Error - 5 X_i + 11 Y_i >= 0
_C13: - C + Error + 7 X_i = 14
_C14: Error - 7 X_i - 14 Y_i >= 0
_C15: Error - 7 X_i + 14 Y_i >= 0
_C16: - C + Error + 8 X_i = 15
_C17: Error - 8 X_i - 15 Y_i >= 0
_C18: Error - 8 X_i + 15 Y_i >= 0
_C19: - C + Error + 10 X_i = 19
_C2: Error - X_i - 3 Y_i >= 0
_C20: Error - 10 X_i - 19 Y_i >= 0
_C21: Error - 10 X_i + 19 Y_i >= 0
_C22: - Error + W >= 0
_C3: Error - X_i + 3 Y_i >= 0
_C4: - C + Error + 2 X_i = 5
_C5: Error - 2 X_i - 5 Y_i >= 0
_C6: Error - 2 X_i + 5 Y_i >= 0
_C7: - C + Error + 3 X_i = 7
_C8: Error - 3 X_i - 7 Y_i >= 0
_C9: Error - 3 X_i + 7 Y_i >= 0
Bounds
C free
Error free
W free
X_i free
Y_i free
End
