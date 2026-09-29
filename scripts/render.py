#!/usr/bin/env python3
"""Render the profile's header and stats SVGs.

One palette, one visual system: a terminal session. The design commits to a dark
card, so there is no light variant — the card carries its own background and sits
correctly on either GitHub theme.

Everything is legible with animation stopped. Nothing starts at opacity 0, because
GitHub's image proxy, link thumbnails and reduced-motion readers all paint the SVG
at time zero, and anything invisible then is invisible for good.
"""
import json, os, sys, urllib.request, pathlib

USER = "Vishnu-vashishth"
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"

MONO = "ui-monospace,'SF Mono','JetBrains Mono',Menlo,Consolas,monospace"
BG, BR, GRN, DIM, AMB, DEEP, TXT = (
    "#060A07", "#13301F", "#4ADE80", "#5E9C78", "#FACC15", "#1F7A45", "#CFEBD9")

# service, status, timing — the systems this profile actually describes
LOGS = [("payment.webhook", "settled", "12ms"), ("grpc.checkout", "scope ok", "4ms"),
        ("subscription", "renewed", "31ms"), ("telemetry.flush", "1.2k events", "")]

QUERY = """query($login:String!){user(login:$login){
  contributionsCollection{totalPullRequestReviewContributions
    contributionCalendar{totalContributions}}
  repositories(ownerAffiliations:OWNER,isFork:false){totalCount}
  pullRequests{totalCount}}}"""


def fetch():
    tok = os.environ.get("PROFILE_TOKEN") or os.environ["GITHUB_TOKEN"]
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": USER}}).encode(),
        headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json"},
    )
    u = json.load(urllib.request.urlopen(req))["data"]["user"]
    c = u["contributionsCollection"]
    return [
        (c["contributionCalendar"]["totalContributions"], "contributions", "past year"),
        (u["pullRequests"]["totalCount"],                 "pull requests", "all time"),
        (c["totalPullRequestReviewContributions"],        "code reviews",  "past year"),
        (u["repositories"]["totalCount"],                 "repositories",  "authored"),
    ]


CHROME = f'''<defs><pattern id="sc" width="4" height="4" patternUnits="userSpaceOnUse">
<rect width="4" height="1.1" fill="#0D1F14" opacity=".55"/></pattern></defs>'''


def header():
    rows = (f'<text class="lgt" x="600" y="62" fill="{DEEP}" opacity=".75">~$ tail -f services.log</text>'
            f'<rect class="scan" x="596" y="78" width="364" height="20" rx="4" fill="{GRN}" opacity=".06"/>')
    for i, (svc, st, ms) in enumerate(LOGS):
        y, d = 90 + i * 25, i * 0.42
        rows += (f'<g><text class="ok tick" x="600" y="{y}" style="animation-delay:{d:.2f}s">✓</text>'
                 f'<text class="lgt" x="622" y="{y}">{svc}</text>'
                 f'<text class="ms" x="812" y="{y}">{st}</text>'
                 f'<text class="lgt" x="918" y="{y}" opacity=".7">{ms}</text></g>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="240" viewBox="0 0 1000 240" role="img" aria-label="Vishnu Vashishth — backend engineer, distributed systems">
{CHROME}
<style>
 .nm{{font:700 40px {MONO};fill:{GRN};letter-spacing:-1px}}
 .pr{{font:700 40px {MONO};fill:{DEEP}}}
 .rl{{font:500 12.5px {MONO};fill:{AMB};letter-spacing:2.2px}}
 .sk{{font:400 11.5px {MONO};fill:{DIM};letter-spacing:1.2px}}
 .lgt{{font:400 11px {MONO};fill:{DIM};letter-spacing:.4px}}
 .ok{{font:400 11px {MONO};fill:{GRN}}}
 .ms{{font:400 11px {MONO};fill:{AMB};opacity:.85}}
 .cu{{fill:{GRN};animation:bl 1.05s steps(1) infinite}}
 .tick{{animation:tk 3.4s ease-in-out infinite}}
 .scan{{animation:sn 5.5s ease-in-out infinite}}
 @keyframes bl{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
 @keyframes tk{{0%,100%{{opacity:1}}50%{{opacity:.4}}}}
 @keyframes sn{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(78px)}}}}
 @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style>
<rect width="1000" height="240" rx="14" fill="{BG}"/>
<rect width="1000" height="240" rx="14" fill="url(#sc)"/>
<rect x=".5" y=".5" width="999" height="239" rx="14" fill="none" stroke="{BR}"/>
<text class="pr" x="52" y="102">~$</text>
<text class="nm" x="112" y="102">vishnu-vashishth</text>
<rect class="cu" x="507" y="74" width="15" height="34"/>
<text class="rl" x="52" y="142">BACKEND ENGINEER :: DISTRIBUTED SYSTEMS</text>
<text class="sk" x="52" y="170">payments · microservices · gRPC · AI infrastructure</text>
{rows}</svg>'''


def stats(data):
    cols = ""
    for i, (val, label, sub) in enumerate(data):
        x = 52 + i * 232
        cols += (f'<text class="vl" x="{x}" y="104">{val:,}</text>'
                 f'<text class="lb" x="{x}" y="127">{label.upper()}</text>'
                 f'<text class="sb" x="{x}" y="145">{sub}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="176" viewBox="0 0 1000 176" role="img" aria-label="GitHub activity">
{CHROME}
<style>
 .pr{{font:500 13px {MONO};fill:{DEEP}}}
 .cm{{font:500 13px {MONO};fill:{GRN}}}
 .vl{{font:700 30px {MONO};fill:{AMB}}}
 .lb{{font:500 10.5px {MONO};fill:{TXT};letter-spacing:1.5px;opacity:.75}}
 .sb{{font:400 10.5px {MONO};fill:{DIM};letter-spacing:.5px;opacity:.75}}
</style>
<rect width="1000" height="176" rx="14" fill="{BG}"/>
<rect width="1000" height="176" rx="14" fill="url(#sc)"/>
<rect x=".5" y=".5" width="999" height="175" rx="14" fill="none" stroke="{BR}"/>
<text class="pr" x="52" y="48">~$</text>
<text class="cm" x="80" y="48">gh api graphql --activity</text>
{cols}</svg>'''


if __name__ == "__main__":
    d = fetch()
    if d[0][0] < 100:
        sys.exit(
            f"refusing to write: only {d[0][0]} contributions visible.\n"
            "The token cannot see this account's real activity, so rendering would\n"
            "overwrite correct numbers with near-zero ones. Set PROFILE_TOKEN to a\n"
            "PAT with read:user + repo, or skip the refresh."
        )
    OUT.mkdir(exist_ok=True)
    (OUT / "header.svg").write_text(header())
    (OUT / "stats.svg").write_text(stats(d))
    print("rendered:", ", ".join(sorted(p.name for p in OUT.glob("*.svg"))))
