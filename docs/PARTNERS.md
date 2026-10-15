# Partners and contributors

Material in this repository is either made by the Foundation, made **with a company**, or contributed by
the **community** (students, individual researchers). Anything that is not Foundation-made names its
origin in the material's `meta.json`, and the key it uses is registered here.

No partners registered yet — the table below is the shape to fill in.

## Companies

| Key | Company | Materials | Permission | Licence | Credit shown as |
|---|---|---|---|---|---|
| `example-semiconductor` | Example Semiconductor Ltd | *(topic / material paths)* | e-mail / agreement, date | `CC-BY-4.0` | "Made with Example Semiconductor" |

A `meta.json` referring to a key that is not in this table is an error — `tools/inventory.py` reports it.

### What we need before publishing partner material

1. **Written permission** to publish, from someone who can give it — an e-mail is enough, kept with the
   agreement, not in this repository.
2. **The licence** the material is published under, and whether the company's name and logo may be used.
3. **How they want to be credited** — the exact wording and, if there is one, a logo (SVG, on a
   transparent background).
4. **Review**: the material has to pass the same checks as ours (`validate.py`, `check_lab.py`,
   `stlp check`) before it is signed into a package.

## Community contributions

| Key | Contributor | Role | Materials | Licence |
|---|---|---|---|---|
| | | student / researcher / lecturer | | |

Community material is reviewed before it is signed. Until it is, it stays `status: draft` and is packaged
`--unsigned`, which the app installs only with *Developer mode* on — so a draft can be tried without
being published as Foundation-approved.

## Trademarks

Company and product names (boards, tools, devices) belong to their owners and are used for
identification only. Naming a tool in a lab is not an endorsement by that company, and naming a
Foundation material is not an endorsement by us.
