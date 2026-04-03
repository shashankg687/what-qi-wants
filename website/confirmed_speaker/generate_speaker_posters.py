#!/usr/bin/env python3
"""Generate individual speaker poster HTML files for each confirmed speaker."""

import os
import html as html_module

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../speakers')

speakers = [
    {
        'name': 'Dr. Jagrati Dwivedi',
        'designation': 'Scientist / Program Associate',
        'org': 'National Quantum Mission (NQM)',
        'org_short': 'NQM, India',
        'photo': 'jagrati_nqm.jpg',
        'company_desc': (
            "India's National Quantum Mission (NQM) is a ₹6,003 crore government initiative "
            "to position India as a global leader in quantum science and technology. The mission "
            "spans quantum computing, communication, sensing, and materials R&D — driving "
            "cutting-edge research and building a robust quantum ecosystem across the nation."
        ),
        'bio': (
            "Dr. Jagrati Dwivedi is associated with India's National Quantum Mission (NQM), "
            "the ₹6,003 crore government initiative to position India as a global leader in "
            "quantum science and technology. She holds a Ph.D. in Physics with expertise in "
            "materials science, X-ray diffraction, thin film deposition, and magnetic materials. "
            "Her research background spans advanced experimental physics with postdoctoral "
            "experience at DESY, Hamburg. Jagrati brings a unique blend of experimental physics "
            "expertise and policy perspective to India's quantum technology ecosystem."
        ),
        'filename': 'poster_jagrati_nqm.html',
    },
    {
        'name': 'Dr. Victoria Goliber',
        'designation': 'Director of Research Partnerships and Government Programs',
        'org': 'D-Wave Systems',
        'org_short': 'D-Wave',
        'photo': 'victoria_dwave.jpg',
        'company_desc': (
            "D-Wave Systems is the world's pioneering quantum computing company, specializing "
            "in quantum annealing technology. With commercial quantum computers deployed across "
            "industries, D-Wave enables real-world optimization for logistics, materials science, "
            "and machine learning — scaling quantum advantage for enterprise solutions globally."
        ),
        'bio': (
            "Dr. Victoria Goliber leads government grants strategy and research partnerships at "
            "D-Wave Quantum, the world's first commercial supplier of quantum computers. She holds a Ph.D. "
            "in Discrete Mathematics from Arizona State University (U.S. DoD SMART Scholar) and "
            "an M.S. in Computer Science (Machine Learning) from Georgia Tech. Previously a "
            "Senior Mathematician at the U.S. Air Force Research Laboratory, she brings a unique "
            "defense-to-industry perspective. Victoria is passionate about demystifying quantum "
            "computing and building quantum-ready workforce pipelines globally."
        ),
        'filename': 'poster_victoria_dwave.html',
    },
    {
        'name': 'Dr. Randy Kuang',
        'designation': 'Co-founder & Chief Scientist',
        'org': 'Quantropi Inc.',
        'org_short': 'Quantropi',
        'photo': 'randy.jpg',
        'company_desc': (
            "Quantropi is a Canadian quantum-safe cybersecurity company building cryptographic "
            "solutions for the post-quantum era. Its pioneering Quantum Permutation Pad (QPP) "
            "encryption and quantum key exchange protocols protect data against both classical "
            "and quantum attacks — making the internet quantum-safe today."
        ),
        'bio': (
            "Dr. Randy Kuang is the Co-founder and Chief Scientist of Quantropi, building "
            "quantum-safe cryptographic solutions for the post-quantum era. He holds a doctorate "
            "in Quantum Physics, and NASA named his work \"Kuang's semi-classical formalism\" in "
            "2012. A prolific inventor with 30+ U.S. patents spanning WiMAX, optical networks, "
            "and quantum cryptography, he previously served as Senior Network Researcher at "
            "Nortel and CTO at inBay Technologies. Randy's pioneering Quantum Permutation Pad "
            "(QPP) encryption has been demonstrated on IBM quantum systems — he loves turning "
            "deep theory into deployable security."
        ),
        'filename': 'poster_randy_quantropi.html',
    },
    {
        'name': 'Dr. Ritajit Majumdar',
        'designation': 'Research Scientist',
        'org': 'IBM Quantum (IBM India Research Lab)',
        'org_short': 'IBM Quantum',
        'photo': 'ritajit.jpeg',
        'company_desc': (
            "IBM Quantum is at the forefront of building utility-scale quantum computers and "
            "an open quantum ecosystem. Through the IBM Quantum Network and Qiskit framework, "
            "IBM enables researchers and enterprises worldwide to push the boundaries of "
            "quantum error correction, algorithms, and practical quantum advantage."
        ),
        'bio': (
            "Dr. Ritajit Majumdar is a Research Scientist at IBM Quantum, enabling utility-scale "
            "quantum results on IBM devices. He earned his Ph.D. from the Indian Statistical "
            "Institute specializing in quantum error correction, supported by a Fulbright-Nehru "
            "Doctoral Research Fellowship at IBM Watson Research Centre. A gold medalist from "
            "Calcutta University and DST Inspire Fellow, he has published extensively on quantum "
            "error mitigation, NISQ algorithms, and machine learning-based decoding. Ritajit is "
            "a sought-after speaker who enjoys bridging the gap between quantum theory and "
            "practical applications."
        ),
        'filename': 'poster_ritajit_ibm.html',
    },
    {
        'name': 'Dr. Shravani Shahapure',
        'designation': 'Associate Director – Quantum Safe Cybersecurity',
        'org': 'Big4 (Risk Advisory)',
        'org_short': 'Big4',
        'photo': 'shravani_deloitte.jpg',
        'company_desc': (
            "Big4's Quantum Safe practice within Risk Advisory helps enterprises prepare "
            "for the quantum threat to cybersecurity. Through cryptographic agility assessments, "
            "quantum risk frameworks, and post-quantum migration strategies, Big4 leads "
            "the industry in quantum-safe transformation across sectors."
        ),
        'bio': (
            "Dr. Shravani Shahapure is an Associate Director at Big4, leading the Quantum Safe "
            "cybersecurity, Cryptography, and Quantum Computing practice within Risk Advisory. "
            "With 20+ years in cybersecurity, she holds two patents in cryptography and quantum "
            "computing and an M.E. from IIT Bombay. She previously held senior roles at Capgemini, "
            "PwC India, and the Data Security Council of India. Shravani is deeply committed to "
            "helping enterprises navigate the quantum threat landscape and is known for making "
            "complex security concepts accessible."
        ),
        'filename': 'poster_shravani_deloitte.html',
    },
    {
        'name': 'Biman Chattopadhyay',
        'designation': 'Co-founder & CTO',
        'org': 'Quanfluence',
        'org_short': 'Quanfluence',
        'photo': 'biman_quanfluence.png',
        'company_desc': (
            "Quanfluence is a Bengaluru-based quantum computing startup building India's first "
            "general-purpose quantum computer using photonic technology. Their optical Ising "
            "machine processes hundreds of interconnected variables simultaneously for "
            "optimization — backed by $2M in seed funding and growing rapidly."
        ),
        'bio': (
            "Biman Chattopadhyay is the Co-founder and CTO of Quanfluence, a Bengaluru-based "
            "quantum computing startup building India's first general-purpose quantum computer "
            "using photonic technology. He leads the development of their optical Ising machine "
            "that processes hundreds of interconnected variables simultaneously for optimization "
            "problems. Quanfluence recently secured $2M in seed funding, and Biman holds patents "
            "in quantum random number generation. An entrepreneur at heart, he also co-founded "
            "SilabTech and is an active angel investor in deep-tech startups."
        ),
        'filename': 'poster_biman_quanfluence.html',
    },
    {
        'name': 'Dr. Sourav Chatterjee',
        'designation': 'Scientist',
        'org': 'TCS Innovation Labs (TCS Research)',
        'org_short': 'TCS Research',
        'photo': 'sourav_tcs.jpg',
        'company_desc': (
            "TCS Innovation Labs drives cutting-edge quantum research within Tata Consultancy "
            "Services, exploring quantum computing, sensing, and communication for industrial "
            "applications. From photonic Ising machines to quantum metrology for healthcare "
            "and materials — TCS Research bridges quantum theory with enterprise impact."
        ),
        'bio': (
            "Dr. Sourav Chatterjee leads the research efforts in Quantum Optical Technologies at TCS. "
            "Previously, he worked as a Scientist (C) in the Quantum Experiments with Satellite "
            "Technology (QuEST) project between the Raman Research Institute (RRI) and the Indian "
            "Space Research Organization (ISRO). Prior to that he completed his doctoral research "
            "in Physics from the Max Planck Institute for the Science of Light, Erlangen, Germany. "
            "In 2020, as a part of a two-member team from RRI, he won the BRICS Worldskills "
            "competition in Quantum Technology competence organized by the Russian Quantum Centre "
            "in Moscow. Besides, he holds a B.Sc. (Hons.) in Physics from Calcutta University, a "
            "B.Tech. in Computer Science Engineering along with a M.S. by research in Computational "
            "Natural Sciences from IIIT-Hyderabad. He has been extensively involved as an expert "
            "in the National Quantum Mission being run by the DST, Government of India."
        ),
        'filename': 'poster_sourav_tcs.html',
    },
    {
        'name': 'Dr. Nayana Das',
        'designation': 'Research Engineer',
        'org': 'LTI Mindtree',
        'org_short': 'LTI Mindtree',
        'photo': 'nayana_ltimindtree.jpeg',
        'company_desc': (
            "LTI Mindtree's quantum research division advances quantum-safe communication "
            "and post-quantum cryptography for enterprise systems. With a focus on building "
            "secure infrastructure ready for the post-quantum era, they drive innovation "
            "in quantum secure direct communication and information security protocols."
        ),
        'bio': (
            "Dr. Nayana Das is a Research Engineer at LTI Mindtree specializing in quantum "
            "communication and post-quantum cryptography, with 9+ years of experience in "
            "quantum cryptography and information security. She earned her Ph.D. in Computer "
            "Science from the Indian Statistical Institute with a thesis on \"Analysis and Design "
            "of Quantum Secure Communication Systems.\" She holds multiple patents and has "
            "published in prestigious journals on topics including Measurement-Device-Independent "
            "Quantum Secure Direct Communication. Nayana is passionate about building secure "
            "communication infrastructure for the quantum era and mentoring the next generation "
            "of researchers."
        ),
        'filename': 'poster_nayana_ltimindtree.html',
    },
    {
        'name': 'Mr. Animesh Aaryan',
        'designation': 'Founder & CEO',
        'org': 'Taqbit Labs',
        'org_short': 'Taqbit',
        'photo': 'Animesh_taqbit.jpeg',
        'company_desc': (
            "Taqbit Labs specializes in quantum-safe cybersecurity solutions including Quantum "
            "Key Distribution (QKD) and Quantum Random Number Generators (QRNG). They build "
            "production-ready quantum-secure communication systems for defense, telecom, and "
            "enterprise infrastructure — protecting organizations against quantum attacks."
        ),
        'bio': (
            "Mr. Animesh Aaryan stands at the forefront of the quantum technology revolution as "
            "the Chief Executive Officer of TAQBIT LABS, Bengaluru. He is an innovator with close "
            "to a decade of experience in quantum physics, with a strong focus on quantum "
            "cryptography and photonics. TAQBIT Labs is a technology company focused on "
            "commercializing Quantum technologies such as Quantum Communication, Sensing, & "
            "Algorithms, which works very closely with the Ministry of Defence, Government of India. "
            "In recognition of its impact and innovation, TAQBIT Labs was awarded Startup of the Year 2025."
        ),
        'filename': 'poster_animesh_taqbit.html',
    },
    {
        'name': 'Dr. Pranab Dutta',
        'designation': 'CEO & Co-founder',
        'org': 'GDQLabs',
        'org_short': 'GDQLabs',
        'photo': 'pranab gdq.jpeg',
        'company_desc': (
            "GDQLabs is an IISER Pune spin-off specializing in quantum sensing for biological "
            "and medical applications. Their breakthrough MAGSENSE™ quantum magnetic sensor "
            "enables radiation-free cardiac diagnostics in under 5 minutes — alongside India's "
            "first quantum gravimeter, pushing quantum precision into healthcare."
        ),
        'bio': (
            "Dr. Pranab Dutta is the CEO and Co-founder of GDQLabs, specializing in quantum "
            "sensing for biological and medical applications. He holds a Ph.D. in Atomic Physics "
            "with 7+ years of experience in quantum technologies, and co-founded GDQLabs with "
            "fellow PhD physicists from IISER Pune. He led the development of India's first "
            "quantum gravimeter and the MAGSENSE™ quantum magnetic sensor for radiation-free "
            "cardiac diagnostics in under 5 minutes. Pranab is driven by the vision of bringing "
            "quantum precision to healthcare and making advanced diagnostics accessible to everyone."
        ),
        'filename': 'poster_pranab_gdqlabs.html',
    },
    {
        'name': 'Dr. Anjani Priyadarsini',
        'designation': 'Quantum Industry Specialist',
        'org': 'Executive Advisor (Independent)',
        'org_short': 'Executive Advisor',
        'photo': 'anjani_aws.jpeg',
        'company_desc': (
            "As a Quantum Industry Specialist and Executive Advisor, Dr. Priyadarsini works across the "
            "quantum ecosystem to accelerate research, education, and industry adoption. She "
            "advises enterprises on quantum readiness and helps build educational initiatives "
            "to democratize access to quantum technologies globally."
        ),
        'bio': (
            "Dr. Anjani Priyadarsini is a Quantum Industry Specialist and Executive Advisor. "
            "With extensive experience in Quantum Business Development (previously with AWS India), "
            "she is passionate about bridging the gap between quantum research and practical industry applications. She "
            "actively engages with academic institutions, enterprises, and the broader tech "
            "community to accelerate the adoption and understanding of quantum technologies "
            "in India and globally."
        ),
        'filename': 'poster_anjani_aws.html',
    },
    {
        'name': 'Dr. Amit Kumar Chauhan',
        'designation': 'Senior Research Associate',
        'org': 'QNu Labs Pvt. Ltd.',
        'org_short': 'QNu Labs',
        'photo': 'amit_qnulabs.jpg',
        'company_desc': (
            "QNu Labs is India's pioneering quantum cryptography company focused on quantum-safe "
            "security solutions. They develop end-to-end quantum key distribution (QKD) systems "
            "and post-quantum cryptographic solutions — building unconditional data security "
            "infrastructure to protect against emerging quantum threats."
        ),
        'bio': (
            "Dr. Amit Kumar Chauhan is a Senior Research Associate at QNu Labs, India's pioneering "
            "quantum cryptography company focused on quantum-safe security solutions. He holds a "
            "Ph.D. in Cryptography from IIT Ropar and an M.Tech in Computer Science from IIIT "
            "Delhi, with research interests in Post-Quantum Cryptography, Cryptanalysis, and "
            "Quantum Computation. Prior to QNu Labs, he worked as a Research Engineer in the PQC "
            "group at C-DOT (Centre for Development of Telematics), contributing to India's "
            "telecom security infrastructure. Amit is passionate about building cryptographic "
            "defenses that will stand the test of quantum computing and enjoys mentoring young "
            "researchers in the field."
        ),
        'filename': 'poster_amit_qnulabs.html',
    },
]


def generate_poster(speaker):
    """Generate an individual speaker poster HTML."""
    name = html_module.escape(speaker['name'])
    designation = html_module.escape(speaker['designation'])
    org = html_module.escape(speaker['org'])
    org_short = html_module.escape(speaker['org_short'])
    photo = speaker['photo']
    company_desc = html_module.escape(speaker['company_desc'])
    bio = html_module.escape(speaker['bio'])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} | What Quantum Industry Wants?</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

        :root {{
            --black: #000000;
            --card-bg: #0a0a0a;
            --card-border: rgba(255,255,255,0.08);
            --lime: #BFF549;
            --lime-dim: rgba(191,245,73,0.15);
            --white: #ffffff;
            --gray: #9ca3af;
            --gray-dim: #6b7280;
        }}

        body {{
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            background: var(--black);
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
            padding: 0;
            color: var(--white);
        }}

        .poster {{
            width: 1080px;
            min-height: 1080px;
            background: var(--black);
            position: relative;
            overflow: hidden;
        }}

        .poster::before {{
            content: '';
            position: absolute;
            top: 10%;
            left: 50%;
            transform: translateX(-50%);
            width: 800px;
            height: 800px;
            background: radial-gradient(circle, rgba(191,245,73,0.04) 0%, transparent 70%);
            z-index: 0;
            pointer-events: none;
        }}

        .content {{
            position: relative;
            z-index: 1;
            width: 100%;
            display: flex;
            flex-direction: column;
            padding: 40px 60px 50px;
        }}

        /* ─── Header ─── */
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }}

        .logo-left {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .logo-left img {{
            width: 56px;
            height: 56px;
            object-fit: contain;
        }}

        .logo-left .org-name {{
            color: var(--gray);
            font-weight: 700;
            font-size: 9px;
            line-height: 1.4;
            text-transform: uppercase;
            letter-spacing: 2px;
        }}

        .logo-right img {{
            width: 60px;
            height: 60px;
            object-fit: contain;
        }}

        /* ─── Event Tag ─── */
        .event-tag {{
            text-align: center;
            margin-bottom: 20px;
        }}

        .event-tag .badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(191,245,73,0.08);
            border: 1px solid rgba(191,245,73,0.2);
            border-radius: 100px;
            padding: 6px 18px;
            font-size: 11px;
            font-weight: 600;
            color: var(--lime);
            letter-spacing: 0.5px;
        }}

        .event-title {{
            text-align: center;
            font-size: 28px;
            font-weight: 900;
            letter-spacing: -0.5px;
            background: linear-gradient(180deg, #ffffff 30%, #6b7280 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 24px;
        }}

        .divider {{
            width: 120px;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--lime), transparent);
            margin: 0 auto 32px;
            opacity: 0.5;
        }}

        /* ─── Company Section ─── */
        .company-section {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 20px;
            padding: 32px 36px;
            margin-bottom: 24px;
            position: relative;
            overflow: hidden;
        }}

        .company-section::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, transparent, var(--lime), transparent);
            opacity: 0.4;
        }}

        .company-question {{
            font-size: 13px;
            font-weight: 800;
            color: var(--lime);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 6px;
            line-height: 1.4;
        }}

        .company-highlight {{
            display: block;
            font-size: 32px;
            font-weight: 900;
            letter-spacing: 3px;
        }}

        .company-desc {{
            font-size: 15px;
            font-weight: 500;
            color: var(--gray);
            line-height: 1.7;
            margin-top: 12px;
        }}

        /* ─── Speaker Section ─── */
        .speaker-section {{
            display: flex;
            gap: 32px;
            align-items: flex-start;
            background: var(--card-bg);
            border: 1px solid rgba(191,245,73,0.15);
            border-radius: 20px;
            padding: 32px 36px;
            margin-bottom: 24px;
            position: relative;
            overflow: hidden;
        }}

        .speaker-section::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, transparent, var(--lime), transparent);
            opacity: 0.3;
        }}

        .photo-col {{
            flex-shrink: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 12px;
        }}

        .avatar {{
            width: 160px;
            height: 160px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid rgba(191,245,73,0.3);
            box-shadow: 0 0 40px rgba(191,245,73,0.08);
        }}

        .speaker-name {{
            font-size: 22px;
            font-weight: 900;
            color: var(--white);
            text-align: center;
        }}

        .speaker-title {{
            font-size: 13px;
            font-weight: 600;
            color: var(--gray);
            text-align: center;
            margin-top: 2px;
        }}

        .speaker-org {{
            font-size: 12px;
            font-weight: 700;
            color: var(--lime);
            text-align: center;
            margin-top: 4px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .bio-col {{
            flex: 1;
        }}

        .bio-label {{
            font-size: 10px;
            font-weight: 800;
            color: var(--lime);
            text-transform: uppercase;
            letter-spacing: 3px;
            margin-bottom: 10px;
        }}

        .bio-text {{
            font-size: 14px;
            font-weight: 500;
            color: var(--gray);
            line-height: 1.75;
        }}

        /* ─── Bottom Bar ─── */
        .bottom-bar {{
            display: flex;
            justify-content: center;
            gap: 14px;
        }}

        .bottom-card {{
            display: flex;
            align-items: center;
            gap: 10px;
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 12px 18px;
        }}

        .bottom-icon {{
            width: 32px;
            height: 32px;
            background: rgba(191,245,73,0.08);
            border: 1px solid rgba(191,245,73,0.15);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            flex-shrink: 0;
        }}

        .bottom-label {{
            font-size: 9px;
            font-weight: 800;
            color: var(--lime);
            text-transform: uppercase;
            letter-spacing: 2px;
        }}

        .bottom-value {{
            font-size: 12px;
            font-weight: 600;
            color: var(--white);
        }}

        /* ─── Host Section ─── */
        .host-section {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            padding: 14px 0 4px;
        }}

        .host-avatar {{
            width: 36px;
            height: 36px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid rgba(191,245,73,0.25);
        }}

        .host-info {{
            font-size: 11px;
            color: var(--gray);
            line-height: 1.4;
        }}

        .host-info .host-label {{
            font-size: 9px;
            font-weight: 800;
            color: var(--lime);
            text-transform: uppercase;
            letter-spacing: 2px;
        }}

        .host-info .host-name {{
            font-weight: 700;
            color: var(--white);
        }}

        .contact {{
            text-align: center;
            padding: 8px 0 0;
            font-size: 12px;
            color: var(--gray-dim);
        }}

        .contact a {{
            color: var(--white);
            text-decoration: none;
            font-weight: 600;
        }}

        .contact .mail-icon {{
            color: var(--lime);
        }}

        @media print {{
            body {{ background: #000; padding: 0; }}
        }}
    </style>
</head>
<body>

<div class="poster">
    <div class="content">

        <!-- Header -->
        <div class="header">
            <div class="logo-left">
                <img src="../assets/Logo_NQM.png" alt="NQM">
                <img src="../assets/qmd_logo.png" alt="QMD" style="height:56px;width:auto;">
                <span class="org-name">National<br>Quantum<br>Mission</span>
            </div>
            <div class="logo-right">
                <img src="../assets/iiti_logo.png" alt="IIT Indore">
            </div>
        </div>

        <!-- Event Tag -->
        <div class="event-tag">
            <div class="badge">⚡ World Quantum Day · 14 April 2026</div>
        </div>
        <div class="event-title">What Quantum Industry Wants?</div>
        <div class="divider"></div>

        <!-- Company Section -->
        <div class="company-section">
            <div class="company-question">What <span class="company-highlight">{org_short}</span> Wants?</div>
            <div class="company-desc">{company_desc}</div>
        </div>

        <!-- Speaker Section -->
        <div class="speaker-section">
            <div class="photo-col">
                <img class="avatar" src="../assets/photos/{photo}" alt="{name}">
                <div class="speaker-name">{name}</div>
                <div class="speaker-title">{designation}</div>
                <div class="speaker-org">{org}</div>
            </div>
            <div class="bio-col">
                <div class="bio-label">Speaker Bio</div>
                <div class="bio-text">{bio}</div>
            </div>
        </div>

        <!-- Bottom Bar -->
        <div class="bottom-bar">
            <div class="bottom-card">
                <div class="bottom-icon">📅</div>
                <div>
                    <div class="bottom-label">Date</div>
                    <div class="bottom-value">14 April 2026</div>
                </div>
            </div>
            <div class="bottom-card">
                <div class="bottom-icon">🕐</div>
                <div>
                    <div class="bottom-label">Time</div>
                    <div class="bottom-value">09:00 – 18:00 IST</div>
                </div>
            </div>
            <div class="bottom-card">
                <div class="bottom-icon">📍</div>
                <div>
                    <div class="bottom-label">Venue</div>
                    <div class="bottom-value">Google Meet</div>
                </div>
            </div>
        </div>

        <div class="host-section">
            <img class="host-avatar" src="../assets/photos/sha_pic_linkedin.png" alt="Dr. Shashank Gupta">
            <div class="host-info">
                <div class="host-label">Host</div>
                <span class="host-name">Dr. Shashank Gupta</span> · Asst. Prof., IIT Indore
            </div>
        </div>

        <div class="contact">
            <span class="mail-icon">✉</span> Contact: <a href="mailto:shashankg@iiti.ac.in">shashankg@iiti.ac.in</a>
        </div>

    </div>
</div>

</body>
</html>'''


def main():
    for speaker in speakers:
        poster_html = generate_poster(speaker)
        filepath = os.path.join(OUTPUT_DIR, speaker['filename'])
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(poster_html)
        print(f"✅ Created: {speaker['filename']}")

    print(f"\n🎉 All {len(speakers)} speaker posters generated!")


if __name__ == '__main__':
    main()
