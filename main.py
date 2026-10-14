from teglalap import Teglalap

try:
    t1 = Teglalap(8,5)
    t2 = Teglalap(3,10)
    t3 = Teglalap(7,7)

    print (f"T1 ({t1.a_oldal}, {t1.b_oldal}) kerülete: {t1.kerulet()}, területe :{t1.terulet()}")
    print (f"T2 ({t2.a_oldal}, {t2.b_oldal}) kerülete: {t2.kerulet()}")
    print (f"T3 ({t3.a_oldal}, {t3.b_oldal}) területe: {t3.terulet()}")

except ValueError as hiba:
    print("Hiba:", hiba)