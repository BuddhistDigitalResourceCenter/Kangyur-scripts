# Kangyur-scripts
Internal scripts to play with Kangyur correspondence tables

Kangyurs:

- `W22084`, `O1GS12980` (D) contains IDs for `D` (~correct) and `Toh`
- `W1PD96682`, `O1PD112371` (CK), idem
- `W4CZ7445`, `O1PD185519` (J), idem
- `W22703`, `O01JW005` (N) contains IDs for `D`, `H` and `N` (~correct)
- `W26071`, `O1PD11016` (H) contains IDs for `D`, `H` (~correct) and `N`
- `W29468`, `O1PD19510` (U) contains IDs for `D`, `H` and `N` (what would be correct? no idea, maybe `N`)
- `W1PD96685`, `O4CZ3720` (C) contains IDs for `N`, stog, `D`, `H`


Example of SPARQL request to produce the csv files:

```
PREFIX bdo: <http://purl.bdrc.io/ontology/core/>
PREFIX bdr: <http://purl.bdrc.io/resource/>
PREFIX adm: <http://purl.bdrc.io/ontology/admin/>

SELECT ?nodeId ?N ?D
WHERE {
  GRAPH bdr:W1PD96685 {
  	?subject adm:workLegacyNode ?nodeId .
  	OPTIONAL { ?subject bdo:workKaTenSiglaD ?D }
  	OPTIONAL { ?subject bdo:workKaTenSiglaH ?N }
  	FILTER ( bound(?N) || bound(?D) )
  }
}
```