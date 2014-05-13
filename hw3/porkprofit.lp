\* Pork Profit *\
Maximize
OBJ: 11 Ham_Smoked_OT + 14 Ham_Smoked_RT + 9 PHam_Smoked_OT
 + 13 PHam_Smoked_RT + 7 PORK_Smoked_OT + 12 PORK_Smoked_RT + 4 PORK_fresh
 + 4 Pham_fresh + 8 ham_fresh
Subject To
_C1: Ham_Smoked_OT + Ham_Smoked_RT + ham_fresh <= 480
_C2: PORK_Smoked_OT + PORK_Smoked_RT + PORK_fresh >= 400
_C3: PHam_Smoked_OT + PHam_Smoked_RT + Pham_fresh <= 230
_C4: Ham_Smoked_RT + PHam_Smoked_RT + PORK_Smoked_RT <= 420
_C5: Ham_Smoked_OT + PHam_Smoked_OT + PORK_Smoked_OT <= 250
End
