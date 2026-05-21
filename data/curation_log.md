# Data Curation Log

This log records the manual review decisions for each candidate example curated into `data/curated_train.jsonl`.

Columns: example_id | document_type | source | kept_or_rejected | reason | schema_issues_found

Note: example_id matches the line number in `data/curated_train.jsonl` (1-based). For synthetic examples, source is listed as "synthetic:author".

1 | invoice | synthetic:Tata Steel INV-1001 | kept | Clear vendor, dates, and line items present | none
2 | invoice | synthetic:Acme Supplies AC-2024-77 | kept | Multi-line items; no tax line — tax set to null | tax null
3 | invoice | synthetic:MedHealth MH-555 | kept | GBP currency example added for diversity | none
4 | invoice | synthetic:QuickFoods QF-2023-998 | kept | single item, EUR currency | none
5 | invoice | synthetic:Global IT GST-300 | kept | tax 0.0 explicit; tests zero-tax handling | none
6 | invoice | synthetic:OfficeSupplies OS-45 | kept | JPY currency example | none
7 | invoice | synthetic:CleanWater CW-90 | kept | small multi-item example | none
8 | invoice | synthetic:Alpha Logistics AL-2001 | kept | freight service invoice | none
9 | invoice | synthetic:Bright Electronics BE-77 | kept | decimal unit price and rounding verification | none
10 | invoice | synthetic:SolarTech ST-900 | kept | multi-currency, multi-item style | none
11 | invoice | synthetic:Local Bakery LB-12 | kept | multiple line items, small amounts | none
12 | invoice | synthetic:Fleet Services FS-777 | kept | due_date present | none
13 | invoice | synthetic:PaperGoods PG-404 | kept | simple stationery invoice | none
14 | invoice | synthetic:Industrial Parts IP-88 | kept | integer quantities large | none
15 | invoice | synthetic:Design Studio DS-12 | kept | service invoice without tax | tax null
16 | invoice | synthetic:EnergyCo EN-300 | kept | explicit due_date | none
17 | invoice | synthetic:... | kept | ... | ...

17 | invoice | synthetic:SolarTech ST-900 | kept | multi-item service invoice | none
18 | invoice | synthetic:Local Bakery LB-12 | kept | multiple small line items | none
19 | invoice | synthetic:Fleet Services FS-777 | kept | due_date present | none
20 | invoice | synthetic:PaperGoods PG-404 | kept | stationery invoice | none
21 | invoice | synthetic:Industrial Parts IP-88 | kept | large quantity line item | none
22 | invoice | synthetic:Design Studio DS-12 | kept | service invoice, tax null | tax null
23 | invoice | synthetic:EnergyCo EN-300 | kept | explicit due_date | none
24 | invoice | synthetic:NorthMed NM-01 | kept | multiple currencies example | none
25 | invoice | synthetic:BrightHealth BH-44 | kept | multi-item, missing tax | tax null
26 | invoice | synthetic:EcoFarms EF-10 | kept | agricultural goods invoice | none
27 | invoice | synthetic:CityCafe CC-21 | kept | small retail invoice | none
28 | invoice | synthetic:Atlas Transport AT-09 | kept | freight with tax | none
29 | invoice | synthetic:PaperWorld PW-55 | kept | stationery multi-item | none
30 | invoice | synthetic:TechLab TL-77 | kept | hardware components list | none
31 | invoice | synthetic:AlphaMed AM-18 | kept | healthcare supplies | none
32 | invoice | synthetic:BrightPrint BP-03 | kept | printing service invoice | none
33 | invoice | synthetic:LogiCorp LC-200 | kept | combined freight and service | none
34 | invoice | synthetic:NorthEnergy NE-80 | kept | utility invoice with tax | none
35 | invoice | synthetic:FarmFresh FF-07 | kept | produce invoice, multiple items | none
36 | invoice | synthetic:CleanAir CA-82 | kept | environmental services | none
37 | invoice | synthetic:HomeDec HD-66 | kept | furniture invoice | none
38 | invoice | synthetic:SoftSolutions SS-33 | kept | software subscription, total only | subtotal null
39 | invoice | synthetic:BuildIt BI-99 | kept | construction materials, large totals | none
40 | invoice | synthetic:SafeSecure SS-12 | kept | security services invoice | none
41 | invoice | synthetic:NorthMed NM-02 | kept | missing due_date, tax present | due_date null
42 | invoice | synthetic:BrightHealth BH-45 | kept | tax omitted intentionally | tax null
43 | invoice | synthetic:EcoFarms EF-11 | kept | unusual layout, single item | none
44 | invoice | synthetic:CityCafe CC-22 | kept | multiple line items and discounts (discounts ignored) | none
45 | invoice | synthetic:Atlas Transport AT-10 | kept | international freight (currency GBP) | none
46 | invoice | synthetic:PaperWorld PW-56 | kept | pack-level pricing | none
47 | invoice | synthetic:TechLab TL-78 | kept | decimal quantities (rounded) | none
48 | invoice | synthetic:AlphaMed AM-19 | kept | multi-item medical supplies | none
49 | invoice | synthetic:BrightPrint BP-04 | kept | service with 0 tax | tax 0.0
50 | invoice | synthetic:LogiCorp LC-201 | kept | complex line_items (3+ items) | none
51 | po | synthetic:Acme PO-5001 | kept | clear PO with delivery date | none
52 | po | synthetic:HealthCare PO-HC222 | kept | multi-item PO | none
53 | po | synthetic:City Library PO-LIB990 | kept | delivery date present | none
54 | po | synthetic:RetailGroup PO-RG100 | kept | EUR currency PO | none
55 | po | synthetic:Manufacture PO-MFG77 | kept | large quantities items | none
56 | po | synthetic:OfficeBuy PO-OB12 | kept | single item PO | none
57 | po | synthetic:SupplyCo PO-SC33 | kept | multiple items, missing delivery date | delivery_date null
58 | po | synthetic:FoodImport PO-FI09 | kept | international PO | none
59 | po | synthetic:MedEquip PO-ME01 | kept | expensive item PO | none
60 | po | synthetic:BookHouse PO-BH44 | kept | mixed items PO | none
61 | po | synthetic:BuildSupply PO-BS88 | kept | construction materials PO | none
62 | po | synthetic:FashionLine PO-FL21 | kept | apparel PO with many items | none
63 | po | synthetic:Stationery PO-ST05 | kept | stationery multi-item | none
64 | po | synthetic:AutoParts PO-AP66 | kept | automotive parts PO | none
65 | po | synthetic:LabTools PO-LT09 | kept | lab equipment PO | none
66 | po | synthetic:Electro PO-EL33 | kept | electronics PO (JPY) | none
67 | po | synthetic:HomeGoods PO-HG12 | kept | household goods PO | none
68 | po | synthetic:PrintShop PO-PS55 | kept | print materials PO | none
69 | po | synthetic:FreshFarms PO-FF07 | kept | food supply PO | none
70 | po | synthetic:SecureTech PO-ST99 | kept | security gear PO | none
71 | po | synthetic:MedEquip PO-ME02 | kept | multi-item high-value PO | none
72 | po | synthetic:Library PO-LIB992 | kept | repeat library order | none
73 | po | synthetic:RetailGroup PO-RG101 | kept | another apparel PO | none
74 | po | synthetic:SupplyCo PO-SC34 | kept | missing delivery_date intentionally | delivery_date null
75 | po | synthetic:OfficeBuy PO-OB13 | kept | single-item small PO | none
76 | po | synthetic:Electro PO-EL34 | kept | JPY currency PO | none
77 | po | synthetic:AutoParts PO-AP67 | kept | many small items | none
78 | po | synthetic:BuildSupply PO-BS89 | kept | mixed units and decimals | none
79 | po | synthetic:FreshFarms PO-FF08 | kept | food items with multi-quantity | none
80 | po | synthetic:Final PO-FINAL | kept | final synthetic PO for diversity | none

