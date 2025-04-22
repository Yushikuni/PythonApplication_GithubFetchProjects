from pathlib import Path

def uloz_markdown_soubor(obsah, nazev_souboru, cesta="."):
  """
  Uloží zadaný obsah do Markdown souboru.

  Args:
    obsah (str): Řetězec obsahující Markdown text.
    nazev_souboru (str): Název vytvářeného .md souboru (bez cesty).
    cesta (str, optional): Cesta k adresáři, kam se má soubor uložit.
                           Výchozí hodnota je aktuální adresář (".")
  Returns:
    str: Celá cesta k vytvořenému souboru, nebo None při chybě.
  """
  try:
    cilova_cesta = Path(cesta) / nazev_souboru
    cilova_cesta.write_text(obsah, encoding="utf-8")
    print(f"Soubor '{cilova_cesta}' byl úspěšně vytvořen.")
    return str(cilova_cesta)
  except Exception as e:
    print(f"Došlo k chybě při vytváření souboru: {e}")
    return None

# Markdown content
md_content = """
# The Path to AI Mastery – Level-Up Journey

## Doba trvání: 3 měsíce (květen – červenec)
**Cíl:** Vybudovat AI systém(y), které tě katapultují do studia jako CDPR, a přitom si udržíš fun + vnitřní flow.

---

## Měsíc 1: Patrol AI & Senzory – Květinový květen

### Hlavní úkoly (Main Quests)
- [ ] Vytvoř AI patrolovací systém ve stylu Zaklínače 3 (v UE5, C++).
- [ ] Zkombinuj s AI Perception (sight + hearing).
- [ ] Ulož pozice patrol bodů do datové struktury (např. `TArray<FVector>`).
- [ ] Udělej fallback, když hráč NPC vyruší (např. investigace).

### Vedlejší questy (Side Quests)
- [ ] Vydat článek: *„Jak vytvořit realistickou patrol AI v Unreal Engine 5“*
- [ ] Nahrát krátké video patrolování (YouTube, nebo blog embed).
- [ ] GitHub: pushni kód se základní dokumentací.

### Bossfight
- [ ] Hráč se vplíží do zorného pole NPC. Otestuj, že NPC reaguje realisticky a nezasekává se.
- [ ] Podaří se ti zneviditelnit se skrz cover systém nebo úhel zorného pole?

---

## Měsíc 2: Reaktivní AI & Decision Making – Červený červen

### Hlavní úkoly
- [ ] Přidej decision-making na základě událostí (FSM nebo jednoduchý BT).
- [ ] NPC mění stav: klid → podezření → útok → ústup.
- [ ] Vytvoř „StateManager“ v C++ s Enumy.

### Vedlejší questy
- [ ] Článek: *„Decision-Making AI: Jak navrhnout chování, které reaguje na hráče“*
- [ ] Přidej breakpointy a logování, aby šlo sledovat přechody stavů.
- [ ] Refaktoruj patrol AI, aby to byla součást modulu „NPCControllerModule“.

### Bossfight
- [ ] NPC musí *bez chyby* přejít mezi 3 různými stavy podle vstupu od hráče (zvuk, útok, smrt).

---

## Měsíc 3: Dynamická AI & Export světu – Zářivý červenec

### Hlavní úkoly
- [ ] Implementuj dynamické chování – např. útěk, hledání spojenců, volání posil.
- [ ] Přidej jednoduchý stealth systém (např. skrývání v trávě nebo detekce podle hlasitosti).
- [ ] Připrav showcase scénu – jako demo pro portfolio/CDPR.

### Vedlejší questy
- [ ] Článek: *„Stealth & Dynamika: Když AI žije svým vlastním životem“*
- [ ] Nahrát video s komentářem: „Behind the AI: Jak to funguje.“

### Bossfight
- [ ] AI zareaguje přirozeně na stealth útok a pokud přežije, zavolá posily, které znají trasu k hráči.

---

## Bonusy & Achievements
- [ ] **„Scribe“** – vydala jsi 3 blog posty.
- [ ] **„Visionary“** – vytvořila jsi vlastní AI framework.
- [ ] **„Witcher Dev“** – dokončila jsi chování inspirované Zaklínačem.
- [ ] **„Master of Perception“** – používala jsi všechny hlavní sensory v UE5.
"""

# Použití metody
nazev_souboru = "The_Path_to_AI_Mastery.md"
cesta_ulozeni = "C:/Users/Atlan/Downloads"  # Můžeš změnit cestu podle potřeby
vytvoreny_soubor = uloz_markdown_soubor(md_content, nazev_souboru, cesta_ulozeni)

if vytvoreny_soubor:
  print(f"Soubor byl uložen na: {vytvoreny_soubor}")
