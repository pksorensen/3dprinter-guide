"""Builds site/index.html from source/template.html + source/data.json."""
import json, pathlib
root = pathlib.Path(__file__).parent
t = (root / 'source/template.html').read_text()
d = json.loads((root / 'source/data.json').read_text())
body = t.replace('/*DATA*/null', json.dumps(d, ensure_ascii=False).replace('</', '<\\/'))
title_end = body.index('</title>') + len('</title>')
title, rest = body[:title_end], body[title_end:]
URL = 'https://3dprinter.arvo.works/'
DESC = 'Uafhængig købsguide til 21 aktuelle 3D-printere: svar på fem spørgsmål, sammenlign side om side, og se kilden bag hvert tal. Tjekket 3. oktober 2026.'
head = f'''<!doctype html>
<html lang="da">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
{title}
<meta name="description" content="{DESC}">
<link rel="canonical" href="{URL}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:locale" content="da_DK">
<meta property="og:url" content="{URL}">
<meta property="og:title" content="Hvilken 3D-printer skal jeg købe?">
<meta property="og:description" content="{DESC}">
<meta property="og:image" content="{URL}og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="author" content="Poul Kjeldager Sørensen">
<style>html{{color-scheme:light;padding:env(safe-area-inset-top,0) 0 env(safe-area-inset-bottom,0)}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
'''
out = head + rest.replace('<div class="wrap">', '</head>\n<body>\n<div class="wrap">', 1) + '\n</body>\n</html>\n'
(root / 'site/index.html').write_text(out)
print('wrote', len(out), 'bytes')
