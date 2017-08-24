#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import Classes

# region Variables

complete_cancer_cell_type = ['acantholytic squamous carcinoma cell line:HCC1806',
                             'acute lymphoblastic leukemia (B-ALL) cell line:BALL-1',
                             'acute lymphoblastic leukemia (B-ALL) cell line:NALM-6',
                             'acute lymphoblastic leukemia (T-ALL) cell line:HPB-ALL',
                             'acute lymphoblastic leukemia (T-ALL) cell line:Jurkat',
                             'acute myeloid leukemia (FAB M0) cell line:Kasumi-3',
                             'acute myeloid leukemia (FAB M0) cell line:KG-1',
                             'acute myeloid leukemia (FAB M1) cell line:HYT-1',
                             'acute myeloid leukemia (FAB M2) cell line:Kasumi-1',
                             'acute myeloid leukemia (FAB M2) cell line:Kasumi-6',
                             'acute myeloid leukemia (FAB M2) cell line:NKM-1',
                             'acute myeloid leukemia (FAB M3) cell line:HL60',
                             'acute myeloid leukemia (FAB M4) cell line:FKH-1',
                             'acute myeloid leukemia (FAB M4) cell line:HNT-34',
                             'acute myeloid leukemia (FAB M4eo) cell line:EoL-1',
                             'acute myeloid leukemia (FAB M4eo) cell line:EoL-3',
                             'acute myeloid leukemia (FAB M5) cell line:NOMO-1',
                             'acute myeloid leukemia (FAB M5) cell line:P31/FUJ',
                             'acute myeloid leukemia (FAB M5) cell line:THP-1 (fresh)',
                             'acute myeloid leukemia (FAB M5) cell line:U-937 DE-4',
                             'acute myeloid leukemia (FAB M6) cell line:EEB',
                             'acute myeloid leukemia (FAB M6) cell line:F-36E',
                             'acute myeloid leukemia (FAB M6) cell line:F-36P',
                             'acute myeloid leukemia (FAB M7) cell line:MKPL-1',
                             'acute myeloid leukemia (FAB M7) cell line:M-MOK', 'adenocarcinoma cell line:IM95m',
                             'adrenal cortex adenocarcinoma cell line:SW-13', 'adult T-cell leukemia cell line:ATN-1',
                             'alveolar cell carcinoma cell line:SW 1573', 'anaplastic carcinoma cell line:8305C',
                             'anaplastic large cell lymphoma cell line:Ki-JK',
                             'anaplastic squamous cell carcinoma cell line:RPMI 2650',
                             'argyrophil small cell carcinoma cell line:TC-YIK', 'astrocytoma cell line:TM-31',
                             'b cell line:RPMI1788', 'B lymphoblastoid cell line: GM12878 ENCODE',
                             'basal cell carcinoma cell line:TE 354.T', 'bile duct carcinoma cell line:HuCCT1',
                             'bile duct carcinoma cell line:TFK-1',
                             'biphenotypic B myelomonocytic leukemia cell line:MV-4-11',
                             'bone marrow stromal cell line:StromaNKtert', 'breast carcinoma cell line:MCF7',
                             'breast carcinoma cell line:MDA-MB-453',
                             'bronchial squamous cell carcinoma cell line:KNS-62',
                             'bronchioalveolar carcinoma cell line:NCI-H358',
                             'bronchioalveolar carcinoma cell line:NCI-H650',
                             'bronchogenic carcinoma cell line:ChaGo-K-1', 'Burkitt lymphoma cell line:DAUDI',
                             'Burkitt lymphoma cell line:RAJI', 'carcinoid cell line:NCI-H1770',
                             'carcinoid cell line:NCI-H727', 'carcinoid cell line:SK-PN-DW',
                             'carcinosarcoma cell line:JHUCS-1', 'cervical cancer cell line:D98-AH2',
                             'cervical cancer cell line:ME-180', 'cholangiocellular carcinoma cell line:HuH-28',
                             'chondrosarcoma cell line:SW 1353', 'choriocarcinoma cell line:BeWo',
                             'choriocarcinoma cell line:SCH', 'choriocarcinoma cell line:T3M-3',
                             'chronic lymphocytic leukemia cell line:SKW-3',
                             'chronic myeloblastic leukemia cell line:KCL-22',
                             'chronic myelogenous leukemia cell line:K562',
                             'chronic myelogenous leukemia cell line:KU812',
                             'chronic myelogenous leukemia cell line:MEG-A2', 'clear cell carcinoma cell line:JHOC-5',
                             'clear cell carcinoma cell line:TEN', 'colon carcinoma cell line:CACO-2',
                             'colon carcinoma cell line:COLO-320', 'cord blood derived cell line:COBL-a untreated',
                             'diffuse large B-cell lymphoma cell line:CTB-1', 'ductal cell carcinoma cell line:KLM-1',
                             'ductal cell carcinoma cell line:MIA Paca2',
                             'embryonic kidney cell line: HEK293/SLAM untreated', 'embryonic pancreas cell line:1B2C6',
                             'embryonic pancreas cell line:1C3D3', 'embryonic pancreas cell line:1C3IKEI',
                             'embryonic pancreas cell line:2C6', 'endometrial carcinoma cell line:OMC-2',
                             'endometrial stromal sarcoma cell line:OMC-9',
                             'endometrioid adenocarcinoma cell line:JHUEM-1', 'epidermoid carcinoma cell line:A431',
                             'epidermoid carcinoma cell line:Ca Ski', 'epithelioid sarcoma cell line:HS-ES-1',
                             'epithelioid sarcoma cell line:HS-ES-2R', 'epitheloid carcinoma cell line: HelaS3 ENCODE',
                             'Ewing sarcoma cell line:Hs 863.T',
                             'extraskeletal myxoid chondrosarcoma cell line:H-EMC-SS', 'fibrosarcoma cell line:HT-1080',
                             'fibrous histiocytoma cell line:GCT TIB-223', 'gall bladder carcinoma cell line:TGBC14TKB',
                             'gall bladder carcinoma cell line:TGBC2TKB', 'gastric adenocarcinoma cell line:MKN1',
                             'gastric adenocarcinoma cell line:MKN45', 'gastric cancer cell line:AZ521',
                             'gastric cancer cell line:GSS', 'gastrointestinal carcinoma cell line:ECC12',
                             'giant cell carcinoma cell line:LU65', 'giant cell carcinoma cell line:Lu99B',
                             'glassy cell carcinoma cell line:HOKUG', 'glioblastoma cell line:A172',
                             'glioblastoma cell line:T98G', 'glioma cell line:GI-1',
                             'granulosa cell tumor cell line:KGN', 'hairy cell leukemia cell line:Mo',
                             'Hep-2 cells mock treated', 'hepatic mesenchymal tumor cell line:LI90',
                             'hepatoblastoma cell line:HuH-6', 'hepatocellular carcinoma cell line: HepG2 ENCODE',
                             'hepatoma cell line:Li-7', 'hereditary spherocytic anemia cell line:WIL2-NS',
                             'Hodgkin lymphoma cell line:HD-Mar2', 'keratoacanthoma cell line:HKA-1',
                             'Krukenberg tumor cell line:HSKTC', 'large cell lung carcinoma cell line:IA-LM',
                             'large cell lung carcinoma cell line:NCI-H460',
                             'large cell non-keratinizing squamous carcinoma cell line:SKG-II-SF',
                             'leiomyoblastoma cell line:G-402', 'leiomyoma cell line:10964C',
                             'leiomyoma cell line:15242A', 'leiomyoma cell line:15425', 'leiomyosarcoma cell line:Hs 5',
                             'lens epithelial cell line:SRA', 'leukemia, chronic megakaryoblastic cell line:MEG-01',
                             'liposarcoma cell line:KMLS-1', 'liposarcoma cell line:SW 872',
                             'lung adenocarcinoma cell line:A549', 'lung adenocarcinoma cell line:PC-14',
                             'lung adenocarcinoma, papillary cell line:NCI-H441', 'lymphangiectasia cell line:DS-1',
                             'lymphoma, malignant, hairy B-cell cell line:MLMA',
                             'malignant trichilemmal cyst cell line:DJM-1', 'maxillary sinus tumor cell line:HSQ-89',
                             'medulloblastoma cell line:D283 Med', 'medulloblastoma cell line:ONS-76',
                             'melanoma cell line:COLO 679', 'melanoma cell line:G-361', 'meningioma cell line:HKBMM',
                             'merkel cell carcinoma cell line:MKL-1', 'merkel cell carcinoma cell line:MS-1',
                             'mesenchymal stem cell line:Hu5/E18', 'mesodermal tumor cell line:HIRS-BM',
                             'mesothelioma cell line:ACC-MESO-1', 'mesothelioma cell line:ACC-MESO-4',
                             'mesothelioma cell line:Mero-14', 'mesothelioma cell line:Mero-25',
                             'mesothelioma cell line:Mero-41', 'mesothelioma cell line:Mero-48a',
                             'mesothelioma cell line:Mero-82', 'mesothelioma cell line:Mero-83',
                             'mesothelioma cell line:Mero-84', 'mesothelioma cell line:Mero-95',
                             'mesothelioma cell line:NCI-H2052', 'mesothelioma cell line:NCI-H226',
                             'mesothelioma cell line:NCI-H2452', 'mesothelioma cell line:NCI-H28',
                             'mesothelioma cell line:No36', 'mesothelioma cell line:ONE58',
                             'mixed mullerian tumor cell line:HTMMT', 'mucinous adenocarcinoma cell line:JHOM-1',
                             'mucinous cystadenocarcinoma cell line:MCAS', 'myelodysplastic syndrome cell line:SKM-1',
                             'myeloma cell line:PCM6', 'myxofibrosarcoma cell line:MFH-ino',
                             'myxofibrosarcoma cell line:NMFH-1', 'neuroblastoma cell line:CHP-134',
                             'neuroblastoma cell line:NB-1', 'neuroblastoma cell line:NBsusSR',
                             'neuroblastoma cell line:NH-12', 'neuroectodermal tumor cell line:FU-RPNT-1',
                             'neuroectodermal tumor cell line:FU-RPNT-2', 'neuroectodermal tumor cell line:TASK1',
                             'neuroepithelioma cell line:SK-N-MC', 'neurofibroma cell line:Hs 53.T',
                             'NK T cell leukemia cell line:KHYG-1',
                             'non T non B acute lymphoblastic leukemia cell line:P30/OHK',
                             'non-small cell lung cancer cell line:NCI-H1385',
                             'normal embryonic palatal mesenchymal cell line:HEPM',
                             'normal intestinal epithelial cell line:FHs 74 Int',
                             'oral squamous cell carcinoma cell line:Ca9-22',
                             'oral squamous cell carcinoma cell line:HO-1-u-1',
                             'oral squamous cell carcinoma cell line:HSC-3',
                             'oral squamous cell carcinoma cell line:SAS', 'osteoclastoma cell line:Hs 706.T',
                             'osteosarcoma cell line:143B/TK', 'osteosarcoma cell line:HS-Os-1',
                             'pagetoid sarcoma cell line:Hs 925', 'pancreatic carcinoma cell line:NOR-P1',
                             'papillary adenocarcinoma cell line:8505C',
                             'papillotubular adenocarcinoma cell line:TGBC18TKB',
                             'peripheral neuroectodermal tumor cell line:KU-SN',
                             'pharyngeal carcinoma cell line:Detroit 562', 'plasma cell leukemia cell line:ARH-77',
                             'pleomorphic hepatocellular carcinoma cell line:SNU-387',
                             'prostate cancer cell line:DU145', 'prostate cancer cell line:PC-3',
                             'rectal cancer cell line:TT1TKB', 'renal cell carcinoma cell line:OS-RC-2',
                             'renal cell carcinoma cell line:TUHR10TKB', 'retinoblastoma cell line:Y79',
                             'rhabdomyosarcoma cell line:KYM-1', 'rhabdomyosarcoma cell line:RMS-YM',
                             'sacrococcigeal teratoma cell line:HTST', 'schwannoma cell line:HS-PSS',
                             'serous adenocarcinoma cell line:JHOS-2', 'serous adenocarcinoma cell line:SK-OV-3-R',
                             'serous cystadenocarcinoma cell line:HTOA', 'signet ring carcinoma cell line:Kato III',
                             'signet ring carcinoma cell line:NUGC-4', 'small cell cervical cancer cell line:HCSC-1',
                             'small cell gastrointestinal carcinoma cell line:ECC10',
                             'small cell lung carcinoma cell line:DMS 144', 'small cell lung carcinoma cell line:LK-2',
                             'small cell lung carcinoma cell line:NCI-H82', 'small cell lung carcinoma cell line:WA-hT',
                             'small-cell gastrointestinal carcinoma cell line:ECC4', 'somatostatinoma cell line:QGP-1',
                             'spindle cell sarcoma cell line:Hs 132.T',
                             'splenic lymphoma with villous lymphocytes cell line:SLVL',
                             'squamous cell carcinoma cell line:EC-GI-10', 'squamous cell carcinoma cell line:JHUS-nk1',
                             'squamous cell carcinoma cell line:T3M-5', 'squamous cell lung carcinoma cell line:EBC-1',
                             'squamous cell lung carcinoma cell line:LC-1F',
                             'squamous cell lung carcinoma cell line:RERF-LC-AI', 'synovial sarcoma cell line:HS-SY-II',
                             'T cell lymphoma cell line:HuT 102 TIB-162', 'teratocarcinoma cell line:NCC-IT-A3',
                             'teratocarcinoma cell line:NCR-G1', 'teratocarcinoma cell line:PA-1',
                             'testicular germ cell embryonal carcinoma cell line:ITO-II',
                             'testicular germ cell embryonal carcinoma cell line:NEC14',
                             'testicular germ cell embryonal carcinoma cell line:NEC15',
                             'testicular germ cell embryonal carcinoma cell line:NEC8',
                             'thymic carcinoma cell line:Ty-82', 'thyroid carcinoma cell line:KHM-5M',
                             'thyroid carcinoma cell line:TCO-1', 'transitional cell carcinoma cell line:Hs 769',
                             'transitional-cell carcinoma cell line:5637',
                             'transitional-cell carcinoma cell line:JMSU1', 'tridermal teratoma cell line:HGRT',
                             'tubular adenocarcinoma cell line:SUIT-2', 'Wilms tumor cell line:G-401',
                             'Wilms tumor cell line:HFWT', 'xeroderma pigentosum b cell line:XPL 17']
complete_primary_non_include_list = {"Adipocyte - breast": "pre", "Adipocyte - omental": "pre",
                                     "Adipocyte - perirenal": "pre", "Adipocyte - subcutaneous": "pre",
                                     "Endothelial Cells - Vein": "Umbilical",
                                     "Renal Epithelial Cells": "Cortical",
                                     "Skeletal Muscle Cells": ["satellite", "differentiated"]}
complete_primary_exclude_list = ["mesenchymal precursor cell - ovarian", "Osteoblast - differentiated",
                                 "Peripheral Blood Mononuclear Cells", "Whole blood"]
complete_primary_jit_exclude_list = {"CD14+ CD16- Monocytes": ("CD14+ Monocytes", "CD16"),
                                     "CD14+ CD16+ Monocytes": ("CD14+ Monocytes", "CD16"),
                                     "CD14- CD16+ Monocytes": ("CD14+ Monocytes", "CD16"),
                                     "CD4+CD25+CD45RA- memory regulatory T cells": ("CD4+ T Cells", "CD25"),
                                     "CD4+CD25+CD45RA+ naive regulatory T cells": ("CD4+ T Cells", "CD25"),
                                     "CD4+CD25-CD45RA- memory conventional T cells": ("CD4+ T Cells", "CD25"),
                                     "CD4+CD25-CD45RA+ naive conventional T cells": ("CD4+ T Cells", "CD25")}
case_studies = ["small cell lung carcinoma", "testicular germ cell embryonal carcinoma",
                "chronic myelo leukemia", "acute myeloid leukemia (FAB M2)", "teratocarcinoma"]

# endregion Variables

if __name__ == "__main__":
    initialize_promoters = Classes.Promoters("hg19.cage_peak_phase1and2combined_tpm.osc.txt",
                                             "acute myeloid leukemia (FAB M2)",
                                             celltype_exclude=complete_primary_exclude_list,
                                             not_include=complete_primary_non_include_list,
                                             partial_exclude=complete_primary_jit_exclude_list,
                                             sample_types=["primary cells", "cell lines"],
                                             second_parser="primary cells")
    # get files for VEn diagram:
    initialize_promoters.ven_diagrams(50000, 4, threshold=50)

    # test if biologically (statistically) relevant:
    # initialize_promoters.statistics_ven_diagram(5000, 5, 22, threshold=50)
