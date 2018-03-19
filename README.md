# Kangyur-scripts
Internal scripts to play with Kangyur correspondence tables

Kangyurs:

- `W22084`, `O1GS12980` (D) contains IDs for `D` (~correct) and `Toh`
- `W4CZ5369`, `O4CZ5369` (D), idem
- `W30532`, (no outline) (D), idem
- `W1PD96682`, `O1PD112371` (A), no catalogue indication in the outline
- `W4CZ7445`, `O1PD185519` (J), idem
- `W22703`, `O01JW005` (N) contains IDs for `D`, `H` and `N` (~correct)
- `W26071`, `O1PD11016` (H) contains IDs for `D`, `H` (~correct) and `N`
- `W29468`, `O1PD19510` (U) contains IDs for `D`, `H` and `N` (what would be correct? no idea, maybe `N`)
- `W1PD96685`, `O4CZ3720` (C) contains IDs for `N`, `S`, `D`, `H`
- `W22083`, `O01CT0007` (S) contains IDs for `S` (~correct), `D`

Tengyurs:

- `W1GS66030`, `O2DB20796` (C) contains IDs for `Toh`
- `W23703`, `O1GS6011` (D), idem
- `W22704`, `O2DB75712` (N), contains IDs for `D`, `Q` (~correct?) and `G`
- `W1KG13126`, `O1PD181215` (Q), contains IDs for `Q` (~correct?) and `G`
- `W1PD95844`, `O2MS16391` (A), contains IDs for `Toh` (~correct?), `Q` and `G`
- `W23702`, `O00CR0008` (G), `Q` and `G` (~correct?)

Example of SPARQL request to produce the csv files:

```
PREFIX bdo: <http://purl.bdrc.io/ontology/core/>
PREFIX bdr: <http://purl.bdrc.io/resource/>
PREFIX adm: <http://purl.bdrc.io/ontology/admin/>

SELECT ?nodeId ?N ?D
WHERE {
  GRAPH bdr:W1PD96682 {
  	?subject adm:workLegacyNode ?nodeId .
  	OPTIONAL { ?subject bdo:workKaTenSiglaD ?D }
  	OPTIONAL { ?subject bdo:workKaTenSiglaH ?N }
  	FILTER ( bound(?N) || bound(?D) )
  }
}
```
