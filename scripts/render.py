#!/usr/bin/env python3
"""Render the profile's header and stats SVGs. One palette, two themes."""
import json, os, sys, urllib.request, pathlib

USER = "Vishnu-vashishth"
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"

THEMES = {
    "dark":  dict(bg="#0B0E14", line="#1C222C", text="#ECEFF4", muted="#7E8794", accent="#E8A33D"),
    "light": dict(bg="#FCFBF9", line="#E7E3DC", text="#14171A", muted="#6A7280", accent="#B8791A"),
}
SERIF = "Georgia,'Times New Roman',serif"
MONO  = "ui-monospace,'SF Mono','JetBrains Mono',Menlo,Consolas,monospace"

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


def header(t):
    # service-topology motif: two tiers behind a gateway, pulsing like traffic
    nodes = [(700,100,1),(778,66,0),(778,134,0),(856,100,1),(934,66,0),(934,134,0)]
    edges = [(0,1),(0,2),(1,3),(2,3),(3,4),(3,5)]
    e = "".join(
        f'<line x1="{nodes[a][0]}" y1="{nodes[a][1]}" x2="{nodes[b][0]}" y2="{nodes[b][1]}"/>'
        for a, b in edges)
    n = "".join(
        f'<circle class="n" style="animation-delay:{i*.45:.2f}s" cx="{x}" cy="{y}" r="4.5"'
        f' fill="{t["accent"] if hub else t["bg"]}"/>'
        for i, (x, y, hub) in enumerate(nodes))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="200" viewBox="0 0 1000 200" role="img" aria-label="Vishnu Vashishth — backend engineer">
<style>
  .nm{{font:400 42px {SERIF};fill:{t["text"]}}}
  .rl{{font:500 13px {MONO};fill:{t["muted"]};letter-spacing:1.7px}}
  .sk{{font:400 12px {MONO};fill:{t["muted"]};letter-spacing:1.1px;opacity:.72}}
  .ed{{stroke:{t["accent"]};stroke-width:1.25;opacity:.26}}
  .n{{stroke:{t["accent"]};stroke-width:1.5;animation:p 3.6s ease-in-out infinite}}
  @keyframes p{{0%,100%{{opacity:.34}}50%{{opacity:1}}}}
</style>
<rect x=".5" y=".5" width="999" height="199" rx="12" fill="{t["bg"]}" stroke="{t["line"]}"/>
<text class="nm" x="48" y="88">Vishnu Vashishth</text>
<rect x="48" y="106" width="56" height="2.5" fill="{t["accent"]}"/>
<text class="rl" x="48" y="137">BACKEND ENGINEER — DISTRIBUTED SYSTEMS</text>
<text class="sk" x="48" y="162">TypeScript · NestJS · MongoDB · gRPC · AWS</text>
<line x1="650" y1="52" x2="650" y2="148" stroke="{t["line"]}"/>
<g class="ed">{e}</g><g>{n}</g>
</svg>'''


def stats(t, data):
    cols = ""
    for i, (val, label, sub) in enumerate(data):
        x = 48 + i * 232
        cols += (
            f'<rect x="{x}" y="38" width="20" height="2" fill="{t["accent"]}" opacity=".9"/>'
            f'<text class="vl" x="{x}" y="76">{val:,}</text>'
            f'<text class="lb" x="{x}" y="99">{label.upper()}</text>'
            f'<text class="sb" x="{x}" y="117">{sub}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="152" viewBox="0 0 1000 152" role="img" aria-label="GitHub activity">
<style>
  .vl{{font:400 34px {SERIF};fill:{t["text"]}}}
  .lb{{font:500 10.5px {MONO};fill:{t["muted"]};letter-spacing:1.5px}}
  .sb{{font:400 10.5px {MONO};fill:{t["muted"]};letter-spacing:.5px;opacity:.6}}
</style>
<rect x=".5" y=".5" width="999" height="151" rx="12" fill="{t["bg"]}" stroke="{t["line"]}"/>
{cols}
</svg>'''


if __name__ == "__main__":
    d = fetch()
    contributions = d[0][0]
    if contributions < 100:
        sys.exit(
            f"refusing to write: only {contributions} contributions visible.\n"
            "The token cannot see this account's real activity, so rendering would\n"
            "overwrite correct numbers with near-zero ones. Set PROFILE_TOKEN to a\n"
            "PAT with read:user + repo, or skip the refresh."
        )
    for name, t in THEMES.items():
        (OUT / f"header-{name}.svg").write_text(header(t))
        (OUT / f"stats-{name}.svg").write_text(stats(t, d))
    print("rendered:", ", ".join(sorted(p.name for p in OUT.glob("*.svg"))))
