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

## Package publisher keys

This table concerns material the Foundation publishes in this repository. A company may publish its own
standalone materials and packages elsewhere without being registered here. It creates and protects its
own private signing key, then distributes only its package, public key, public metadata and fingerprint;
recipients can add that public key in Academy's *Trusted publishers* settings.

The Foundation may separately decide to include a confirmed partner **public** key in a future Academy
release so it is trusted by default. This is a deliberate app-distribution decision, not a transfer of the
private key and not a statement that every package or certificate from the publisher is
Foundation-approved. The complete process is in
[Academy's signing-key guide](https://github.com/SemiTecFoundation/semitec-academy/blob/main/docs/KEYS.md#optional-foundation-default-trust-for-a-partner).

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
