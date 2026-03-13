
import math

def euclidean_distance(coords1, coords2):
    return math.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(coords1, coords2)))

# Selected Coordinates
# Russian (Voronez - Central/South Russia, close to Ukraine)
ru_voronez = [0.13089650,0.12160975,0.07353850,0.06088550,0.03608375,0.02252050,0.00969400,0.01171100,-0.00245425,-0.02400975,0.00081175,-0.00790525,0.01728200,0.02435900,-0.01364025,-0.00371250,0.00123850,0.00110850,0.00282850,0.00343925,-0.00237075,-0.00321475,0.00237250,-0.00503050,-0.00197575]

# Ukrainian (Sumy - East Ukraine, close to Russia)
ua_sumy = [0.13009980,0.12277760,0.06746680,0.05933510,0.03914580,0.02359420,0.00900080,0.01253030,-0.00040900,-0.02139450,-0.00298810,-0.00929170,0.01465800,0.02638230,-0.01211990,-0.00476010,-0.00265980,0.00011390,0.00330570,-0.00178830,-0.00444220,-0.00592290,0.00568170,-0.00736220,-0.00038320]

dist = euclidean_distance(ru_voronez, ua_sumy)
print(f"Distance between Russian (Voronez) and Ukrainian (Sumy): {dist:.4f}")
print("Note: G25 distances < 0.02 are usually considered very close, often indistinguishable without fine-scale analysis.")
