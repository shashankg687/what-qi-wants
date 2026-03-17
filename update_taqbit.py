import re
import os

files = [
    'taqbit_problem_1.html',
    'taqbit_problem_2.html',
    'taqbit_problem_3.html',
    'problem_statement_template.html'
]

for filename in files:
    filepath = os.path.join('/Users/quantsha/Downloads/what_QI_want/website', filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Logo
    logo_pattern = re.compile(r'<div class="cover__company-logo">\s*Company(?:<br>\s*|\s*)Logo\s*</div>')
    content = logo_pattern.sub('<img src="TQL logo.jpeg" alt="Taqbit Labs Logo" class="cover__company-logo" style="background: none; padding: 0; border-radius: 0; object-fit: contain;">', content)

    # 2. Page 2 removal 
    page2_pattern = re.compile(r'<!-- ═══════════════════════════════════════════════\s*PAGE 2: INSTRUCTIONS FOR SPEAKERS\s*═══════════════════════════════════════════════ -->.*?<!-- ═══════════════════════════════════════════════', re.DOTALL)
    content = page2_pattern.sub(r'<!-- ═══════════════════════════════════════════════', content)

    # 3. Company Overview - only for the taqbit files
    if 'taqbit' in filename:
        overview_pattern = re.compile(r'<p>Provide a brief overview of your company, its mission, and its work in the quantum technology space.\s*</p>\s*<div class="fill-block fill-block--large">.*?</div>', re.DOTALL)
        new_overview = '''<div class="fill-block fill-block--large">
                    <strong>Taqbit Labs</strong> is building quantum-secure communication systems, post-quantum cryptography, and real-time quantum key distribution (QKD) solutions that ensure digital trust in an uncertain future. Our technologies enable unhackable encryption, true randomness generation, and a secure quantum backbone for government, finance, and critical infrastructure, proudly developed and manufactured in India.
                </div>'''
        content = overview_pattern.sub(new_overview, content)

        hq_pattern = re.compile(r'<div class="card__desc"><span class="fill">Tokyo, Japan</span></div>')
        content = hq_pattern.sub('<div class="card__desc"><span class="fill">India</span></div>', content)
        
        focus_pattern = re.compile(r'<div class="card__desc"><span class="fill">Quantum Key Distribution / Security</span></div>')
        content = focus_pattern.sub('<div class="card__desc"><span class="fill">Cybersecurity, QKD, QRNG, PQC</span></div>', content)

    # 4. Remove place-holder Impact Statement
    impact_pattern = re.compile(r'<div class="highlight-box">\s*<p><strong>Impact Statement:</strong>\s*<span class="fill">\[Describe in 1–2 sentences the real-world[^\]]+\]</span></p>\s*</div>\s*<div class="divider"></div>', re.DOTALL)
    content = impact_pattern.sub('', content)

    # 5. Remove place-holder Prerequisites
    prereq_pattern = re.compile(r'<div class="section-label"><span class="section-label__icon">🔗</span> Prerequisites</div>\s*<p[^>]*>.*?</p>\s*<div class="fill-block">\s*\[List recommended prerequisites.*?\]\s*</div>', re.DOTALL)
    content = prereq_pattern.sub('', content)

    # 6. Remove place-holder timeline details (only keeping start date if we don't have others)
    timeline_pattern = re.compile(r'<div class="card">\s*<span class="card__icon">⏰</span>\s*<div class="card__title">Submission Deadline</div>\s*<div class="card__desc"><span class="fill">\[Suggested: July 2026\]</span></div>\s*</div>\s*<div class="card">\s*<span class="card__icon">🏆</span>\s*<div class="card__title">Evaluation Period</div>\s*<div class="card__desc"><span class="fill">\[e.g., July – Aug 2026\]</span></div>\s*</div>\s*<div class="card">\s*<span class="card__icon">🎓</span>\s*<div class="card__title">PPO Decisions</div>\s*<div class="card__desc"><span class="fill">\[Expected date for PPO offers\]</span></div>\s*</div>', re.DOTALL)
    content = timeline_pattern.sub('', content)

    # 7. Remove Evaluation Criteria row 5
    crit5_pattern = re.compile(r'<tr>\s*<td><span class="fill">\[Criterion 5\]</span></td>\s*<td><span class="fill">\[e.g., Presentation & report quality\]</span></td>\s*<td><span class="fill">\[%\]</span></td>\s*</tr>', re.DOTALL)
    content = crit5_pattern.sub('', content)

    # 8. Remove Resources and Contact box
    resources_pattern = re.compile(r'<div class="section-label"><span class="section-label__icon">📚</span> Resources & References</div>\s*<p[^>]*>.*?</p>(?:\s*<div class="resource-item">.*?</div>){4}\s*<div class="divider"></div>\s*<div class="highlight-box">\s*<p><strong>Contact for Queries:</strong>.*?</div>', re.DOTALL)
    content = resources_pattern.sub('', content)
    
    # Also remove "Provide a clear and detailed description of the challenge..." instructions
    inst_desc_pattern = re.compile(r'<p>Provide a clear and detailed description of the challenge.*?</p>')
    content = inst_desc_pattern.sub('', content)
    
    # 9. Clean up page numbers slightly if they look like "08 / 08" maybe just remove the "/ 08" since we deleted a page.
    page_total_pattern = re.compile(r'<span class="page-footer__page">0(\d) / 08</span>')
    content = page_total_pattern.sub(r'<span class="page-footer__page">0\1</span>', content)

    with open(filepath, 'w') as f:
        f.write(content)

print("Update complete.")
