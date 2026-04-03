from generate_speaker_posters import speakers
import os

OUTPUT_FILE = "linkedin_speaker_posts.md"

def generate_linkedin_post(speaker):
    name = speaker['name']
    org = speaker['org']
    company_desc = speaker['company_desc']
    
    post = f"""
---
### 🌟 Speaker Announcement: {name} from {org}! 🌟

We are thrilled to welcome **{name}** to the upcoming **"What Quantum Industry Wants"** event this World Quantum Day (April 14, 2026)! 🚀

🏢 **About {org}:**
{company_desc}

Don't miss the opportunity to hear directly from quantum industry leaders and learn what they are looking for in terms of skills, partnerships, and research! 

📅 **When:** April 14, 2026 | 09:00 AM – 6:00 PM IST
📍 **Where:** Google Meet
🔗 **Register Now:** [Add Registration Link Here]

Join us as we bridge the gap between quantum research and practical industry applications. See you there! ⚡

#QuantumComputing #QuantumIndustry #WorldQuantumDay #QuantumTechnology #QuantumWorkforce
---
"""
    return post

def main():
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# LinkedIn Speaker Announcement Posts\n\n")
        f.write("*Below are draft LinkedIn posts for each confirmed speaker to promote the event.*\n\n")
        
        for speaker in speakers:
            f.write(generate_linkedin_post(speaker))
            f.write("\n")
            
    print(f"✅ Generated {len(speakers)} LinkedIn posts in {OUTPUT_FILE}")

if __name__ == '__main__':
    main()
