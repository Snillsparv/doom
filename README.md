# Hur kan AI döda alla? – argumentbank för en videoserie

Researchunderlag för en pedagogisk videoserie i tre delar som svarar på frågan
"HUR skulle AI kunna döda alla människor?":

1. **Hur AI fungerar** – varför "bara nästa ord" ändå kan bli riktig intelligens, vad AI kan idag och vart det pekar.
2. **Varför skulle AI vilja det?** – hur mål "växer fram" i träning, belöningshackning, instrumentell konvergens, och vad labben redan sett.
3. **Hur skulle det gå till?** – konkreta, plausibla vägar, och varför "dra ur sladden" inte räcker.

Plus tvärgående sektioner: skeptikerns starkaste invändningar (med ärliga svar), de bästa befintliga förklararna att låna från, svensk kontext och ordlista, samt metod.

## Sidan

`index.html` är en fristående sida (all data inbakad). Öppna den direkt i en webbläsare, eller aktivera GitHub Pages för repot.
Där kan du bläddra mellan delar och frågor, se alla svar sorterade efter bedömd effektivitet, och fälla ut varje svar för manusförslag, fördelar, nackdelar, förbehåll, förklarare och källor.

## Struktur

| Mapp/fil | Innehåll |
|---|---|
| `index.html` | Den byggda sidan (genereras – redigera inte för hand) |
| `template.html` | Sidans mall: design, navigering, rendering |
| `data/*.json` | Sidans data på svenska: `del1.json`, `del2.json`, `del3.json`, `skeptiker.json`, `forklarare.json`, `svenskt.json`, `metod.json` |
| `build.py` | Bakar in `data/*.json` i `template.html` → `index.html` |
| `research/` | Hela researchmaterialet på engelska (elva filer, rev 2 med researcharnas svar till rödlaget) |
| `research/debate/` | Rödlagens tre granskningar |
| `research/00_*.md` | Briefingar som styrde agenterna (uppdrag, schema, syntesregler) |

## Bygga om

```
python3 build.py
```

Redigera JSON-filerna i `data/` (schemat finns i `research/00_SCHEMA.md`) och kör byggskriptet. Svaren sorteras automatiskt efter `score`.

## Metod i korthet

Elva researchagenter arbetade parallellt med varsitt område. Tre rödlagsagenter angrep resultaten och verifierade de mest bärande påståendena mot primärkällor. Researcharna svarade punkt för punkt (medge/försvara) och rättade sina filer. Domaragenter per del vägde ihop allt enligt en rubrik grundad i forskning om riskkommunikation och skrev den svenska datan. Se sidans metodsektion för detaljer och kända begränsningar.

Allt är daterat till 15 september 2026. Kontrollera siffror och citat mot källorna innan inspelning.
