p = 'index.html'
s = open(p, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    assert old in s, 'NO ENCONTRADO: ' + old[:80]
    s = s.replace(old, new, n)

rep("viernes 6 de noviembre de 2026 en Daule.", "sábado 7 de noviembre de 2026 en Daule.")
rep("Viernes 6 de noviembre de 2026 · Daule", "Sábado 7 de noviembre de 2026 · Daule") if "Viernes 6 de noviembre de 2026 · Daule" in s else None
rep("Daniela cumple 15 años. Te invitamos a celebrar el viernes 6 de noviembre de 2026 en Daule.", "Daniela cumple 15 años. Te invitamos a celebrar el sábado 7 de noviembre de 2026 en Daule.") if "Te invitamos a celebrar el viernes 6" in s else None
s = s.replace("Sábado 7", "Sábado 7")
s = s.replace("viernes 6 de noviembre", "sábado 7 de noviembre")
s = s.replace("Viernes 6 de noviembre", "Sábado 7 de noviembre")
s = s.replace("6 · NOVIEMBRE · 2026", "7 · NOVIEMBRE · 2026")
s = s.replace("2026-11-06T16:00:00-05:00", "2026-11-07T16:00:00-05:00")
s = s.replace("// viernes 6 de noviembre de 2026", "// sábado 7 de noviembre de 2026")
s = s.replace("¡Te espero el 6 de noviembre!", "¡Te espero el 7 de noviembre!")
s = s.replace("los espero el seis", "los espero el siete")
open(p, 'w', encoding='utf-8').write(s)
import re
print([m for m in re.findall(r'.{30}(?:viernes|Viernes|6 de nov|6 · |06).{30}', s)][:10])
