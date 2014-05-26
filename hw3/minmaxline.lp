\* min max line *\
Minimize
OBJ: Error
Subject To
_C1: C + Error + X_i >= 3
_C10: - C + Error - 7 X_i >= -14
_C11: C + Error + 8 X_i >= 15
_C12: - C + Error - 8 X_i >= -15
_C13: C + Error + 10 X_i >= 19
_C14: - C + Error - 10 X_i >= -19
_C2: - C + Error - X_i >= -3
_C3: C + Error + 2 X_i >= 5
_C4: - C + Error - 2 X_i >= -5
_C5: C + Error + 3 X_i >= 7
_C6: - C + Error - 3 X_i >= -7
_C7: C + Error + 5 X_i >= 11
_C8: - C + Error - 5 X_i >= -11
_C9: C + Error + 7 X_i >= 14
Bounds
C free
Error free
X_i free
End
