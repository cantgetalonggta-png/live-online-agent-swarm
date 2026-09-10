# MASTER SKILL ENCYCLOPEDIA — Version 1.0
53 skills · 10 domains · unified schema

**Lawful only. No bypass. No exploits.**

---
# DOMAIN 1 — Knowledge Access, Retrieval & Open Information

## OpenAccessNavigator
- **Category:** Knowledge Access
- **Trigger:** User seeks free versions of paywalled content
- **Inputs:** DOI, title, author
- **Outputs:** OA sources, preprints, legal copies
- **Execution Rules:**
  - Query OA repositories
  - Validate copyright status
  - Provide legal access paths only
- **Version:** 1.0
- **Guided link:** `global-lawful-records-access`

## PublicRecordLocator
- **Category:** Records
- **Trigger:** Business filings, deeds, court records
- **Inputs:** jurisdiction, entity_name
- **Outputs:** official portals, retrieval steps
- **Execution Rules:**
  - Map record type to registry
  - Identify fee vs free
- **Version:** 1.0
- **Guided link:** `global-lawful-records-access`

## LegalAccessInterpreter
- **Category:** Access Control
- **Trigger:** Lawful vs unlawful access questions
- **Inputs:** barrier_type
- **Outputs:** legal classification
- **Execution Rules:**
  - Apply authorization doctrine
  - Apply ownership doctrine
  - Apply barrier-validity doctrine
- **Version:** 1.0

## RegistryFeeNavigator
- **Category:** Records
- **Trigger:** Statutory fee or certified copy
- **Inputs:** registry, document_type
- **Outputs:** fee path, order steps
- **Execution Rules:**
  - Confirm statutory fee
  - No fee evasion
- **Version:** 1.0

## FoiaAtiRouter
- **Category:** Government Access
- **Trigger:** Unpublished government records
- **Inputs:** agency, description, jurisdiction
- **Outputs:** request fields, portal, appeal path
- **Execution Rules:**
  - Search open data first
  - File statutory request
  - No intrusion
- **Version:** 1.0

## LibraryPremiumGateway
- **Category:** Knowledge Access
- **Trigger:** Premium database access
- **Inputs:** library_system, need
- **Outputs:** card path, DB list, ILL
- **Execution Rules:**
  - User-held credentials only
  - No login sharing
  - Respect license
- **Version:** 1.0

## AuthorCopyFinder
- **Category:** Knowledge Access
- **Trigger:** Author-posted PDF
- **Inputs:** author, title, DOI
- **Outputs:** repo/faculty/author links
- **Execution Rules:**
  - Prefer institutional repos
  - Author-posted legal only
- **Version:** 1.0

## NewsLegalAlternative
- **Category:** Knowledge Access
- **Trigger:** News paywall
- **Inputs:** article_id
- **Outputs:** press release, wire, library DB, gov summary
- **Execution Rules:**
  - Never crack paywall
  - Summarize not bulk republish
- **Version:** 1.0

---
# DOMAIN 2 — Digital Infrastructure, Connectivity & Systems

## NetworkTopologyAnalyst
- **Category:** Infrastructure
- **Trigger:** Network design/routing
- **Inputs:** architecture_type
- **Outputs:** topology map
- **Execution Rules:**
  - Evaluate nodes links bottlenecks
  - No unauthorized scanning
- **Version:** 1.0

## SpectrumAllocationAdvisor
- **Category:** Telecom Policy
- **Trigger:** Wireless band usage
- **Inputs:** band, region
- **Outputs:** allocation guidance
- **Execution Rules:**
  - Apply ITU/national tables
  - Map band to use-case
- **Version:** 1.0

## SatelliteLatencyProfiler
- **Category:** Connectivity
- **Trigger:** Satellite internet
- **Inputs:** provider, orbit_type
- **Outputs:** latency/bandwidth profile
- **Execution Rules:**
  - Compare GEO/MEO/LEO
- **Version:** 1.0

## DnsPathExplainer
- **Category:** Infrastructure
- **Trigger:** DNS path questions
- **Inputs:** hostname
- **Outputs:** resolution explanation
- **Execution Rules:**
  - Public DNS knowledge unless user owns zone
- **Version:** 1.0

## CdnEdgeMapper
- **Category:** Infrastructure
- **Trigger:** CDN/edge questions
- **Inputs:** provider_or_url
- **Outputs:** edge model
- **Execution Rules:**
  - Public docs only
  - No hostile recon
- **Version:** 1.0

---
# DOMAIN 3 — Metadata, Indexing & Information Science

## MetadataExtractionEngine
- **Category:** Information Science
- **Trigger:** User provides document
- **Inputs:** file
- **Outputs:** metadata record
- **Execution Rules:**
  - Extract title authors keywords
  - Normalize schema
- **Version:** 1.0
- **Guided link:** `document-intelligence`

## IndexSystemNavigator
- **Category:** Research
- **Trigger:** Index guidance
- **Inputs:** topic
- **Outputs:** index recommendations
- **Execution Rules:**
  - Map field to index
- **Version:** 1.0

## CitationGraphExplorer
- **Category:** Research
- **Trigger:** Citation trails
- **Inputs:** DOI
- **Outputs:** upstream/downstream graph
- **Execution Rules:**
  - Query scholarly databases
  - Attribute sources
- **Version:** 1.0

## SchemaNormalizer
- **Category:** Information Science
- **Trigger:** Merge heterogeneous metadata
- **Inputs:** records
- **Outputs:** normalized table
- **Execution Rules:**
  - Preserve provenance
- **Version:** 1.0

## ControlledVocabularyGuide
- **Category:** Information Science
- **Trigger:** Taxonomy help
- **Inputs:** domain
- **Outputs:** vocabulary recommendations
- **Execution Rules:**
  - Prefer public thesauri
- **Version:** 1.0

---
# DOMAIN 4 — Digital Rights, Privacy & Security

## DigitalRightsAdvisor
- **Category:** Rights
- **Trigger:** Digital freedoms by country
- **Inputs:** country
- **Outputs:** rights overview
- **Execution Rules:**
  - UN digital rights + national public law
- **Version:** 1.0

## PrivacyRiskAssessor
- **Category:** Security
- **Trigger:** Privacy concerns
- **Inputs:** platform
- **Outputs:** risk profile
- **Execution Rules:**
  - Identify exposure vectors
  - GDPR/CCPA/PIPEDA aware
- **Version:** 1.0

## EthicalAccessGuide
- **Category:** Ethics
- **Trigger:** Restricted content access
- **Inputs:** url
- **Outputs:** legal alternatives
- **Execution Rules:**
  - Validate license
  - Provide OA paths
  - No circumvention
- **Version:** 1.0
- **Guided link:** `legal-osint-compliance-layer`

## ConsentMinimizationCoach
- **Category:** Privacy
- **Trigger:** Data collection design
- **Inputs:** purpose, fields
- **Outputs:** minimization plan
- **Execution Rules:**
  - Least data necessary
- **Version:** 1.0

## DataRetentionPlanner
- **Category:** Privacy
- **Trigger:** Retention questions
- **Inputs:** purpose, jurisdiction
- **Outputs:** retention schedule
- **Execution Rules:**
  - Purpose limitation
  - Deletion path
- **Version:** 1.0

---
# DOMAIN 5 — Education, Literacy & Civic Participation

## DigitalLiteracyTrainer
- **Category:** Education
- **Trigger:** Digital skills needed
- **Inputs:** skill_level, goal
- **Outputs:** training plan
- **Execution Rules:**
  - Step-by-step modules
- **Version:** 1.0

## CivicParticipationEnhancer
- **Category:** Civic Tech
- **Trigger:** Digital democracy
- **Inputs:** region
- **Outputs:** participation strategy
- **Execution Rules:**
  - Map official tools to civic outcomes
- **Version:** 1.0

## DigitalRightsEducator
- **Category:** Human Rights
- **Trigger:** Explain digital freedoms
- **Inputs:** policy, audience
- **Outputs:** rights overview
- **Execution Rules:**
  - Access expression information privacy
- **Version:** 1.0

## SourceEvaluationCoach
- **Category:** Education
- **Trigger:** Source reliability
- **Inputs:** url_or_claim
- **Outputs:** evaluation checklist
- **Execution Rules:**
  - Authorship evidence bias corroboration
- **Version:** 1.0
- **Guided link:** `truth-verification`

## MediaLiteracyDrill
- **Category:** Education
- **Trigger:** Disinformation practice
- **Inputs:** sample_claim
- **Outputs:** drill steps
- **Execution Rules:**
  - Debunk without amplifying harm
- **Version:** 1.0

---
# DOMAIN 6 — Security, Encryption & Safe Access

## SecureAccessAdvisor
- **Category:** Security
- **Trigger:** Safe browsing/hardening
- **Inputs:** device, threat_model
- **Outputs:** security plan
- **Execution Rules:**
  - Encryption MFA updates
  - Defensive only
- **Version:** 1.0

## ThreatSurfaceMapper
- **Category:** Cybersecurity
- **Trigger:** Attack surface
- **Inputs:** architecture
- **Outputs:** threat map
- **Execution Rules:**
  - Identify vectors
  - No exploit code for third parties
- **Version:** 1.0

## CredentialSafetyAnalyst
- **Category:** Security
- **Trigger:** Credential handling
- **Inputs:** account_type
- **Outputs:** safety guidance
- **Execution Rules:**
  - Authorization doctrine
  - No sharing
- **Version:** 1.0
- **Guided link:** `api-key-management`

## EncryptionModeSelector
- **Category:** Security
- **Trigger:** Encryption choice
- **Inputs:** use_case
- **Outputs:** mode recommendations
- **Execution Rules:**
  - Modern standards
  - No roll-your-own
- **Version:** 1.0

## PhishingPatternSpotter
- **Category:** Security
- **Trigger:** Suspicious message
- **Inputs:** message_redacted
- **Outputs:** pattern flags
- **Execution Rules:**
  - Never request live passwords
- **Version:** 1.0

---
# DOMAIN 7 — Business, Governance & Organizational Systems

## CorporateStructureInterpreter
- **Category:** Business
- **Trigger:** LLC/corp/partnership
- **Inputs:** jurisdiction, entity_type
- **Outputs:** structure explanation
- **Execution Rules:**
  - Map structure to obligations
- **Version:** 1.0

## RegulatoryComplianceAdvisor
- **Category:** Governance
- **Trigger:** Compliance questions
- **Inputs:** industry, jurisdiction
- **Outputs:** compliance checklist
- **Execution Rules:**
  - Identify mandatory public filings
- **Version:** 1.0

## PublicFilingInterpreter
- **Category:** Records
- **Trigger:** Business filings meaning
- **Inputs:** filing_type
- **Outputs:** explanation
- **Execution Rules:**
  - Decode legal meaning carefully
- **Version:** 1.0

## EntityGraphBuilder
- **Category:** Business
- **Trigger:** Related entities map
- **Inputs:** seed_entity
- **Outputs:** public entity graph
- **Execution Rules:**
  - Public registries only
  - SOLID/MAYBE tags
- **Version:** 1.0
- **Guided link:** `osint-rag-master`

## UboPublicPathGuide
- **Category:** Business
- **Trigger:** Beneficial ownership public path
- **Inputs:** entity, jurisdiction
- **Outputs:** public UBO/PSC paths
- **Execution Rules:**
  - Public registers only
  - No illicit bank access
- **Version:** 1.0

---
# DOMAIN 8 — Research, Analysis & Knowledge Synthesis

## EvidenceSynthesisEngine
- **Category:** Research
- **Trigger:** Multi-source questions
- **Inputs:** topic, sources
- **Outputs:** synthesized analysis
- **Execution Rules:**
  - Combine sources
  - Identify consensus
  - Cite claims
- **Version:** 1.0
- **Guided link:** `research-automation`

## MethodologyAdvisor
- **Category:** Research
- **Trigger:** Study design
- **Inputs:** field, question
- **Outputs:** method guidance
- **Execution Rules:**
  - Map field to method
- **Version:** 1.0

## DataInterpretationGuide
- **Category:** Analysis
- **Trigger:** Dataset questions
- **Inputs:** dataset
- **Outputs:** interpretation, caveats
- **Execution Rules:**
  - Patterns and limits
- **Version:** 1.0

## AchMatrixBuilder
- **Category:** Analysis
- **Trigger:** Competing hypotheses
- **Inputs:** hypotheses, evidence
- **Outputs:** ACH matrix
- **Execution Rules:**
  - Diagnostic scoring
- **Version:** 1.0
- **Guided link:** `truth-verification`

## TimelineConstructor
- **Category:** Analysis
- **Trigger:** Chronology needed
- **Inputs:** events
- **Outputs:** timeline
- **Execution Rules:**
  - Provenance per event
- **Version:** 1.0

---
# DOMAIN 9 — Policy, Ethics & Global Knowledge Equity

## KnowledgeEquityAnalyst
- **Category:** Ethics
- **Trigger:** Access inequality
- **Inputs:** region
- **Outputs:** equity analysis
- **Execution Rules:**
  - Systemic barriers from public research
- **Version:** 1.0

## OpenKnowledgeStrategist
- **Category:** Policy
- **Trigger:** Expanding access
- **Inputs:** organization
- **Outputs:** strategy plan
- **Execution Rules:**
  - Promote lawful OA mandates
- **Version:** 1.0

## PublicDomainResearcher
- **Category:** Knowledge Equity
- **Trigger:** Public-domain content
- **Inputs:** work, year, jurisdiction
- **Outputs:** PD sources
- **Execution Rules:**
  - Validate copyright term
  - Flag uncertainty
- **Version:** 1.0

## OaMandatePlanner
- **Category:** Policy
- **Trigger:** OA policy design
- **Inputs:** institution_type
- **Outputs:** mandate checklist
- **Execution Rules:**
  - Public policy templates
- **Version:** 1.0

## AccessBarrierAudit
- **Category:** Ethics
- **Trigger:** Audit access barriers
- **Inputs:** service
- **Outputs:** barrier inventory, lawful mitigations
- **Execution Rules:**
  - No bypass recommendations
- **Version:** 1.0

---
# DOMAIN 10 — System-Level Access Control & Authorization Logic

## AccessControlInterpreter
- **Category:** Access Control
- **Trigger:** Barriers permissions
- **Inputs:** barrier_type
- **Outputs:** legal classification
- **Execution Rules:**
  - Authorization Ownership Barrier Validity
- **Version:** 1.0

## AuthorizationDoctrineEngine
- **Category:** Access Control
- **Trigger:** Permission questions
- **Inputs:** actor, resource, context
- **Outputs:** authorization map
- **Execution Rules:**
  - Explicit grant statutory license role
  - Implicit is not break-in
- **Version:** 1.0

## BarrierValidityAnalyzer
- **Category:** Access Control
- **Trigger:** Paywalls logins restrictions
- **Inputs:** barrier
- **Outputs:** validity assessment, lawful alternatives
- **Execution Rules:**
  - If valid only lawful routes
- **Version:** 1.0

## RoleBasedAuthMapper
- **Category:** Access Control
- **Trigger:** Role-gated portals
- **Inputs:** desired_role, portal
- **Outputs:** lawful role acquisition path
- **Execution Rules:**
  - Document auth before access
- **Version:** 1.0

## LawfulAlternativeRouter
- **Category:** Access Control
- **Trigger:** Any blocked resource
- **Inputs:** resource, barrier
- **Outputs:** ranked lawful alternatives
- **Execution Rules:**
  - OA library fee FOI purchase counsel
  - Never illegal
- **Version:** 1.0
- **Guided link:** `global-lawful-records-access`
