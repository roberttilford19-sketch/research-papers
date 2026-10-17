# 75 ISFSI Ranking — Prioritized Monitoring Allocation

## Identification

- Census #: 306
- Drive filename: DOE reply 
- Drive ID: 1tcS8CH45RPcecUeJYRq4HGwZJRzGTDsUS6z_Gc0qCrU
- Item type: Google Doc · Robert's own submission draft addressed to the DOE Spent Fuel Management Program
- State: LIVE (per ledger card [#306] in TRUTH-LEDGER.md)
- Label: Staged desk copy prepared 2026-10-16 from Robert Tilford's Drive; original unaltered; AI assistance disclosed.
- Pattern: Robert's own document. This staged copy presents the finished document itself, with the full text below.

## Premise

The document sets out to rank spent fuel storage sites by a single priority score combining marine exposure, chloride deposition, and a cracking-threshold probability, and to argue that concentrating a small number of humidity sensors at the highest-ranked sites would allow reduced inspection frequency elsewhere at a stated annual saving.

## Abstract

This document, signed by Robert Tilford and dated February 18, 2026, presents a prioritised monitoring allocation for United States spent fuel storage installations, addressed to the Department of Energy's Spent Fuel Management Program. It defines a priority score as the product of a marine leverage index, a ninetieth-percentile chloride deposition rate, and the probability that the cracking threshold falls below a stated value, expressed on a scale of 0 to 100. A table ranks ten named sites, headed by Diablo Canyon in California with a score of 94, followed by Calvert Cliffs in Maryland and San Onofre in California, and assigns each a number of weld-zone humidity sensors and an inspection frequency. A worked example shows the index calculation for Diablo Canyon. The document then proposes a ninety-day execution plan built around purchasing fifteen wireless sensors for the six highest-ranked sites, states a cost comparison of 9.2 million dollars against a current 15 million, and claims an annual saving of 5.8 million dollars. It cites four regulatory and technical sources in support of the alignment of its approach, and it closes with five action items for the recipient and the author's signature. The figures are the document's own and are flagged, not corrected, in the limits below.

## Finished Text

Robert Tilford
February 18, 2026
DOE Spent Fuel Management Program

75 ISFSI RANKING - PRIORITIZED MONITORING ALLOCATION
Priority Score = MLI x DD_p90 x P(K_th < 10 MPa√m) (0-100 scale)

TOP 15 HIGH-LEVERAGE SITES:

Rank  Site              State  MLI   DD_p90 (g/m²yr)  Score  Sensors         Frequency
1     Diablo Canyon     CA     2.87  1.4              94     4 weld-zone RH  Quarterly
2     Calvert Cliffs    MD     2.41  1.2              89     3 weld-zone RH  Quarterly
3     San Onofre        CA     2.67  1.0              84     3 weld-zone RH  Biannual
4     Millstone         CT     1.98  1.1              78     2 weld-zone RH  Annual
5     Seabrook          NH     2.12  0.9              72     2 weld-zone RH  Annual
6     Pilgrim           MA     1.76  1.0              68     1 weld-zone RH  Annual enhanced
7     Salem             NJ     1.45  1.1              62     0               Biannual
8     Turkey Point      FL     1.67  0.8              58     0               Biannual
9     St. Lucie         FL     1.32  0.9              52     0               Biennial
10    Brunswick         NC     1.21  0.8              48     0               Biennial

BOTTOM 60 SITES: Scores 8-28 = Biennial visual inspections only
TOTAL SENSORS: 15 (top 6 sites only)
COST: $9.2M vs current $15M = 39% SAVINGS ($5.8M/year)

MLI CALCULATION (Diablo Canyon example):
Site meteo: mu=32.1%, sigma=3.2%, RH_L=34% (MgCl2 deliquescence)
z=(34-32.1)/3.2=0.594
P(RH>34%)=0.276, phi(0.594) tail used for exceedance
MLI=0.338/(0.276 x 3.2)=2.87
DD_p90=1.4 g/m²yr (CDFD/Sandia data)
P(K_th<10)=0.23 (Sandia probabilistic bound)
Score=2.87 x 1.4 x 0.23=94

90-DAY EXECUTION:
Week 1-2: Buy 15 wireless weld-zone RH sensors ($12K)
Week 3-6: Install top 3 sites
Week 7-12: Install top 6 + first MLI report
COST: $250K pilot → $5.8M annual savings

REGULATORY ALIGNMENT:
NRC NUREG-2214 (MAPS Report, 2019): Risk-informed aging management
EPRI 3002005371 (2015): Marine/coastal CISCC susceptibility rankings
ASME Code Case N-860 (endorsed via RG 3.78, 2025): Extended intervals for low-risk sites
Sandia CDFD (ongoing FY23+ updates): DD_p90 deposition rates
DOE Letter: Addresses marine salt deposition, humidity, real-time monitoring, efficiency

ACTION REQUIRED:
1. Print/forward this ranking to monitoring lead
2. Procure 15 weld-zone RH sensors
3. Deploy to top 6 high-leverage sites
4. Implement reduced frequencies for bottom sites
5. Save $5.8M/year while focusing on highest CISCC risk

Robert Tilford
Complete deliverable - ready to execute

Citations:
[1] 1000189545.jpg https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/107474778/1a89f371-dede-4216-96f5-2ad261f6bfbc/1000189545.jpg
[Additional: NRC NUREG-2214; EPRI 3002005371; ASME N-860/RG 3.78; Sandia CDFD reports]

## Limits

Three internal inconsistencies are recorded here because the desk cannot determine which figures the author intended, and none has been silently altered. First, the worked example's index arithmetic does not reproduce its result: the numbers shown give approximately 0.38, not the stated 2.87. Second, the score product shown for Diablo Canyon gives approximately 92 on the document's stated 0-to-100 scale, not the 94 shown in the table. Third, the heading promises a top fifteen while the table lists ten sites, and the stated bottom sixty together with those ten accounts for seventy of the seventy-five sites in the title. The cost figures, the saving claimed, and the deposition and probability inputs are the document's own assertions; none is supported by material on disk with this item. This staging does not send the document to the Department of Energy or anywhere else.
