#!/usr/bin/env python3
import os
import html as html_module

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'poster')
os.makedirs(OUTPUT_DIR, exist_ok=True)

missing_speakers = [
    {
        'name': 'Reena Dayal',
        'designation': 'Founder and CEO',
        'org': 'QETCI',
        'org_short': 'QETCI',
        'photo': 'reena_qetci.jpeg',
        'company_desc': (
            "Building the Indian Quantum Computing Ecosystem. Driving collaborations, investments, "
            "and policies to accelerate quantum research and commercialization globally. QETCI connects "
            "academia, industry startups, and government to build a strong quantum technology pipeline."
        ),
        'bio': (
            "Prominent technology leader, innovation expert, CEO and Partner for Benzaiten Advisors. "
            "Involved in IEEE Quantum Initiative, Government of India's Quantum Task Force, and "
            "Government of Telangana's Quantum Committee. Member of World Economic Forum's Global Futures "
            "Council for Quantum. Formerly founding Director for Microsoft Garage in India. Holds an "
            "Engineering degree from IIT Roorkee and is a Chevening Fellow."
        ),
        'filename': 'poster_reena_qetci.html',
    },
    {
        'name': 'Dr. Kazuya Niizeki',
        'designation': 'CEO & Co-founder',
        'org': 'LQUOM',
        'org_short': 'LQUOM',
        'photo': 'kazuya_lquom.webp',
        'company_desc': (
            "Pioneering the Quantum Internet. Developing next-generation quantum communication systems, "
            "focusing on long-distance secure quantum repeaters. LQUOM's core technology involves developing "
            "hardware for quantum repeater systems, necessary for sending quantum information securely over "
            "long distances, overcoming limitations of optical fiber losses."
        ),
        'bio': (
            "CEO and founder of LQUOM Inc., a quantum technology startup focused on quantum communication "
            "systems, specifically quantum repeaters for a secure quantum internet. Recognized in Forbes' "
            "2023 30 Under 30 - Asia list. Background from Yokohama National University."
        ),
        'filename': 'poster_kazuya_lquom.html',
    }
]

from generate_16_9_speaker_posters import generate_poster

def main():
    for speaker in missing_speakers:
        poster_html = generate_poster(speaker)
        filepath = os.path.join(OUTPUT_DIR, speaker['filename'])
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(poster_html)
        print(f"✅ Created: {filepath}")

    print(f"🎉 16:9 speaker posters generated for missing speakers!")

if __name__ == '__main__':
    main()
