#!/usr/bin/env python3
"""
Generate a vCard (.vcf) file with hundreds of fake contacts for iOS Simulator demo.
Includes names, phone numbers, emails, and base64-encoded profile pictures.
"""

import random
import base64
from pathlib import Path
from typing import List, Tuple
import urllib.request
import io

# Diverse first names (various cultures/backgrounds)
FIRST_NAMES = [
    # American/European
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
    "William", "Barbara", "David", "Elizabeth", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Christopher", "Karen", "Charles", "Lisa", "Daniel", "Nancy",
    "Matthew", "Betty", "Anthony", "Margaret", "Mark", "Sandra", "Donald", "Ashley",
    "Steven", "Kimberly", "Andrew", "Emily", "Paul", "Donna", "Joshua", "Michelle",
    # Asian
    "Wei", "Yuki", "Min-jun", "Sakura", "Raj", "Priya", "Chen", "Mei", "Haruto", "Aiko",
    "Arjun", "Ananya", "Ji-hoon", "So-yeon", "Kenji", "Hana", "Ravi", "Divya",
    # Hispanic/Latino
    "Carlos", "Maria", "Jose", "Sofia", "Miguel", "Isabella", "Diego", "Valentina",
    "Luis", "Camila", "Juan", "Lucia", "Pedro", "Martina", "Francisco", "Elena",
    # Middle Eastern
    "Mohammed", "Fatima", "Ali", "Aisha", "Omar", "Layla", "Hassan", "Noor",
    "Ahmed", "Mariam", "Khalid", "Zainab", "Ibrahim", "Yasmin",
    # African
    "Kwame", "Amara", "Chidi", "Zuri", "Kofi", "Nia", "Jabari", "Imani",
    # Modern/Trendy
    "Jayden", "Harper", "Aiden", "Ava", "Mason", "Olivia", "Logan", "Emma",
    "Ethan", "Sophia", "Noah", "Mia", "Liam", "Charlotte", "Lucas", "Amelia",
]

LAST_NAMES = [
    # Common surnames from various cultures
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Thompson", "White",
    "Wang", "Li", "Zhang", "Liu", "Chen", "Yang", "Huang", "Zhao", "Wu", "Zhou",
    "Kumar", "Singh", "Patel", "Shah", "Gupta", "Reddy", "Sharma", "Khan",
    "Kim", "Park", "Choi", "Jung", "Kang", "Tanaka", "Suzuki", "Takahashi", "Watanabe",
    "Mohammed", "Ahmed", "Hassan", "Ali", "Ibrahim", "Omar", "Abdullah",
    "Silva", "Santos", "Oliveira", "Souza", "Pereira", "Costa", "Rodrigues",
    "Okonkwo", "Adeyemi", "Mensah", "Diallo", "Traore", "Mwangi",
]

COMPANIES = [
    "Acme Corp", "TechStart", "Global Inc", "Innovation Labs", "DataSys",
    "CloudTech", "NextGen Solutions", "Digital Dynamics", "SmartWorks",
    "FutureVision", "Quantum LLC", "Apex Industries", "Stellar Systems",
    "Vertex Group", "Horizon Enterprises", "Phoenix Technologies",
]

AREA_CODES = [
    "212", "415", "310", "312", "617", "713", "214", "202", "646",
    "702", "404", "305", "206", "303", "408", "512", "858", "720",
]

def generate_contact_photo_base64(initials: str, color_hue: int) -> str:
    """
    Generate a simple SVG profile picture with initials, convert to PNG-like base64.
    For simulator demo purposes, we'll use UIImage-compatible data.
    """
    # Generate a simple color based on hue (0-360)
    r = int(127 + 127 * ((color_hue % 360) / 360))
    g = int(127 + 127 * ((color_hue + 120) % 360 / 360))
    b = int(127 + 127 * ((color_hue + 240) % 360 / 360))

    # Create a minimal SVG (iOS Contacts can handle this)
    svg = f'''<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="rgb({r},{g},{b})"/>
  <text x="100" y="120" font-size="80" text-anchor="middle" fill="white" font-family="Arial">{initials}</text>
</svg>'''

    return base64.b64encode(svg.encode()).decode()

def generate_contacts(count: int = 500) -> List[Tuple[str, str, str, str, str, str]]:
    """Generate list of fake contacts with realistic data."""
    contacts = []
    used_names = set()

    for i in range(count):
        # Generate unique name
        while True:
            first = random.choice(FIRST_NAMES)
            last = random.choice(LAST_NAMES)
            full_name = f"{first} {last}"
            if full_name not in used_names:
                used_names.add(full_name)
                break

        # Generate phone number
        area_code = random.choice(AREA_CODES)
        phone = f"+1 ({area_code}) {random.randint(200,999)}-{random.randint(1000,9999)}"

        # Generate email (mix of providers)
        email_providers = ["gmail.com", "yahoo.com", "outlook.com", "icloud.com", "proton.me"]
        email_first = first.lower()
        email_last = last.lower()
        email_formats = [
            f"{email_first}.{email_last}",
            f"{email_first}{email_last}",
            f"{email_first[0]}{email_last}",
            f"{email_first}_{email_last}",
            f"{email_first}{random.randint(1,99)}",
        ]
        email = f"{random.choice(email_formats)}@{random.choice(email_providers)}"

        # Generate company (50% chance)
        company = random.choice(COMPANIES) if random.random() < 0.5 else ""

        # Generate photo (initials-based)
        initials = f"{first[0]}{last[0]}"
        color_hue = (i * 37) % 360  # Spread colors across spectrum
        photo_base64 = generate_contact_photo_base64(initials, color_hue)

        contacts.append((full_name, phone, email, company, photo_base64, initials))

    return contacts

def create_vcard_file(contacts: List[Tuple[str, str, str, str, str, str]], output_path: str):
    """Create a vCard (.vcf) file with all contacts."""
    with open(output_path, 'w', encoding='utf-8') as f:
        for full_name, phone, email, company, photo_base64, initials in contacts:
            # vCard 3.0 format (iOS compatible)
            f.write("BEGIN:VCARD\n")
            f.write("VERSION:3.0\n")
            f.write(f"FN:{full_name}\n")

            # Split name into first/last
            name_parts = full_name.split(" ", 1)
            if len(name_parts) == 2:
                f.write(f"N:{name_parts[1]};{name_parts[0]};;;\n")
            else:
                f.write(f"N:{full_name};;;;\n")

            # Phone
            f.write(f"TEL;TYPE=CELL:{phone}\n")

            # Email
            f.write(f"EMAIL;TYPE=INTERNET:{email}\n")

            # Company
            if company:
                f.write(f"ORG:{company}\n")

            # Photo (base64-encoded SVG)
            # Note: Using PHOTO;ENCODING=b;TYPE=SVG for compatibility
            # iOS will render these as simple colored circles with initials
            f.write(f"PHOTO;ENCODING=b;TYPE=SVG:{photo_base64}\n")

            f.write("END:VCARD\n")

    print(f"✅ Generated {len(contacts)} contacts in {output_path}")

def main():
    # Generate different contact counts
    configs = [
        (100, "demo-contacts-100.vcf", "Quick demo (100 contacts)"),
        (500, "demo-contacts-500.vcf", "Standard demo (500 contacts)"),
        (1000, "demo-contacts-1000.vcf", "Large demo (1,000 contacts)"),
        (2000, "demo-contacts-2000.vcf", "Extreme demo (2,000 contacts)"),
    ]

    print("🎬 Generating Demo Contacts for iOS Simulator\n")
    print("=" * 60)

    for count, filename, description in configs:
        print(f"\n📦 {description}")
        contacts = generate_contacts(count)
        create_vcard_file(contacts, filename)

    print("\n" + "=" * 60)
    print("\n✅ All contact files generated!")
    print("\n📱 How to import into iOS Simulator:")
    print("   1. Drag the .vcf file onto the simulator")
    print("   2. Tap the file notification")
    print("   3. Choose 'Add All X Contacts'")
    print("   4. Wait for import to complete")
    print("   5. Open Stale Contacts Cleaner")
    print("   6. Record your demo with Camtasia!")
    print("\n🎥 YouTube Upload:")
    print("   - Title: 'Stale Contacts Cleaner - Clean 1,000 Contacts in 10 Minutes'")
    print("   - Description: Include security angle (phishing risk)")
    print("   - Tags: iOS, productivity, security, contacts, privacy")
    print("   - Add to: https://go.fabswill.com")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
