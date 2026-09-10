#!/usr/bin/env python3
"""Hint lawful portals by category + country (offline lookup). Not a scraper."""
import sys

HINTS = {
    ("business", "us"): "SEC EDGAR + state SOS + OpenCorporates",
    ("business", "uk"): "Companies House",
    ("business", "au"): "ASIC",
    ("business", "in"): "MCA",
    ("business", "sg"): "ACRA",
    ("property", "us"): "County recorder/assessor; NYC=ACRIS",
    ("property", "uk"): "HM Land Registry",
    ("property", "nz"): "LINZ",
    ("court", "us"): "CourtListener then PACER; state portals",
    ("court", "uk"): "HMCTS",
    ("academic", "global"): "Unpaywall + arXiv + PMC + CORE",
    ("government", "us"): "FOIA.gov + Data.gov",
    ("government", "uk"): "data.gov.uk",
    ("government", "eu"): "data.europa.eu",
}

def main():
    if len(sys.argv) < 3:
        print("Usage: lookup_portal_hint.py <category> <country_code>")
        print("Categories: business property court academic government news")
        print("Examples: lookup_portal_hint.py business us")
        sys.exit(1)
    cat, country = sys.argv[1].lower(), sys.argv[2].lower()
    key = (cat, country)
    print(HINTS.get(key) or HINTS.get((cat, "global")) or "See references/country-portals.md")

if __name__ == "__main__":
    main()
