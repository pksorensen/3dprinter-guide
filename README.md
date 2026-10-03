# Hvilken 3D-printer?

Uafhængig købsguide til 21 aktuelle 3D-printere — live på <https://3dprinter.arvo.works>.

Hvert tal har en kilde og et verifikationsmærke (bekræftet / rettet / ikke verificeret).
Data er indsamlet og krydstjekket 3. oktober 2026.

- `source/template.html` — siden, med `/*DATA*/null` som pladsholder
- `source/data.json` — printere, typiske købere, ordliste, advarsler
- `build.py` — bygger `site/index.html` (kør efter enhver ændring i `source/`)
- `source/og/` — delebilledet; `PW=<sti til playwright-core> node source/og/render.cjs`
- `Dockerfile` — nginx; deployes via Coolify bag doorman på arvo-boksen

Push deployer ikke af sig selv — udløs en deployment i Coolify.
