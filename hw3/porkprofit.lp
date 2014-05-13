\* Pork Profit *\
Maximize
OBJ: 11 Ham_Smoked_OT + 14 Ham_Smoked_RT + 7 PORK_Smoked_OT
 + 12 PORK_Smoked_RT + 4 PORK_fresh + 9 P_Ham_Smoked_OT + 13 P_Ham_Smoked_RT
 + 4 P_ham_fresh + 8 ham_fresh
Subject To
_C1: Ham_Smoked_OT + Ham_Smoked_RT + ham_fresh <= 480
_C2: PORK_Smoked_OT + PORK_Smoked_RT + PORK_fresh >= 400
_C3: P_Ham_Smoked_OT + P_Ham_Smoked_RT + P_ham_fresh <= 230
_C4: Ham_Smoked_RT + PORK_Smoked_RT + P_Ham_Smoked_RT <= 420
_C5: Ham_Smoked_OT + PORK_Smoked_OT + P_Ham_Smoked_OT <= 250
Bounds
5 <= Ham_Smoked_RT
End
