import re
import os

files = {
    'website/taqbit_problem_1.html': {
        'title': 'Decoy-state parameter estimation for Twin-Field QKD',
        'subtitle': 'Analyze and implement decoy-state methods for TF-QKD under realistic imperfections and finite-size effects.',
        'level': 'Intermediate',
        'motivation': 'Twin-Field QKD breaks the fundamental rate-distance limit, creating a secure quantum backbone. However, practical implementation demands rigorous parameter estimation. This project bridges the gap between theoretical limits and realistic operational constraints.',
        'prob_statement': 'Twin-Field QKD is promising for long-distance secure key distribution. A critical security task is estimating parameters like the single-photon yield and error rate from experimental counts using decoy states.<br><br><strong>Objective:</strong> Students will simulate decoy-state methods under finite-block-size assumptions and realistic imperfections (e.g., intensity fluctuations) to calculate secure key rates.<br><br><strong>Scope & Context:</strong> You must consider finite-size bounds like Hoeffding or Chernoff bounds applied to the parameter estimation process. The simulation should yield a clear analysis of how key rates are impacted by these imperfections.',
        'c1_title': 'Finite-size Effects Simulation',
        'c1_desc': 'Accurately modeling the impact of finite block sizes on key rate using rigorous statistical bounds.',
        'c2_title': 'Realistic Imperfections',
        'c2_desc': 'Incorporating practical non-idealities such as intensity fluctuations in the laser sources and detector inefficiencies.',
        'c3_title': 'Key Rate Optimization',
        'c3_desc': 'Optimizing decoy state probabilities and intensities to maximize the secure key rate.',
        'tech': '• Python programming (NumPy/SciPy) or MATLAB/Mathematica<br>• Monte-Carlo simulation techniques<br>• Statistical bounding (Chernoff/Hoeffding)',
        'constraints': '• Simulations must complete within a reasonable timeframe on a standard laptop<br>• The model must accommodate finite-size data blocks and realistic deviations',
        'acceptance': '• Functional simulation code estimating single-photon yields<br>• Comprehensive sensitivity analysis plots<br>• A clear, well-documented technical report',
        'del_src': 'GitHub repository with well-documented simulation code.',
        'del_rep': '3–5 page PDF report covering methodology, results, and sensitivity analysis.',
        'del_demo': '10-minute recorded walkthrough of the code and findings.',
        'del_add': 'Jupyter notebooks demonstrating the key rate calculation continuously.',
        'e1_crit': 'Simulation Accuracy', 'e1_desc': 'Correct application of finite-size bounds', 'e1_wt': '40%',
        'e2_crit': 'Code Quality', 'e2_desc': 'Readability, modularity, and commenting', 'e2_wt': '20%',
        'e3_crit': 'Analysis Depth', 'e3_desc': 'Comprehensive evaluation of sensitivity to imperfections', 'e3_wt': '25%',
        'e4_crit': 'Documentation', 'e4_desc': 'Clarity of the technical report and presentation', 'e4_wt': '15%'
    },
    'website/taqbit_problem_2.html': {
        'title': 'Comparative analysis of Twin-Field QKD variants',
        'subtitle': 'Systematically study and explain subtle differences between multiple TF-QKD variants targeting experimental feasibility and security assumptions.',
        'level': 'Advanced',
        'motivation': 'Various TF-QKD protocols (e.g., sending-or-not-sending, no-phase-post-selection) exist with subtle differences in security proofs and experimental overhead. A unified comparative analysis is critically needed for industry adoption to select the optimal variant for a given network topology.',
        'prob_statement': 'Conduct a comprehensive review and comparative modeling of at least three prominent TF-QKD variants.<br><br><strong>Objective:</strong> Compare their asymptotic and finite-size key rates under a unified framework, identifying trade-offs between experimental complexity and performance.<br><br><strong>Scope:</strong> Simulate the different protocols assuming identical channel models to isolate the protocol-specific advantages.',
        'c1_title': 'Protocol Standardization',
        'c1_desc': 'Mapping different security assumptions to a unified mathematical framework.',
        'c2_title': 'Simulation Fairness',
        'c2_desc': 'Ensuring the comparative simulations use consistent noise and loss models.',
        'c3_title': 'Experimental Appraisal',
        'c3_desc': 'Evaluating the relative difficulty of physical implementation for each variant.',
        'tech': '• Python programming<br>• Qiskit (optional for modeling)<br>• LaTeX for report generation',
        'constraints': '• Focus exclusively on Prepare-and-Measure TF-QKD variants<br>• Must provide comparable metrics',
        'acceptance': '• A robust unified model<br>• Clear comparative plots (rate vs distance) for all variants',
        'del_src': 'GitHub repo with plotting and modeling scripts.',
        'del_rep': '10-15 page detailed comparative review in IEEE format.',
        'del_demo': 'Live presentation slide deck (PDF/PPT).',
        'del_add': 'Detailed parameter spreadsheets used for generating plots.',
        'e1_crit': 'Methodology Framework', 'e1_desc': 'Robustness of the unified mathematical comparison', 'e1_wt': '35%',
        'e2_crit': 'Simulation Rigor', 'e2_desc': 'Accuracy of comparative rate calculations', 'e2_wt': '35%',
        'e3_crit': 'Practical Insights', 'e3_desc': 'Value of the experimental feasibility appraisal', 'e3_wt': '20%',
        'e4_crit': 'Presentation', 'e4_desc': 'Clarity of the final report and diagrams', 'e4_wt': '10%'
    },
    'website/taqbit_problem_3.html': {
        'title': 'AI/ML for stabilization and anomaly detection in CV-QKD',
        'subtitle': 'Develop machine learning models to dynamically stabilize continuous-variable QKD systems.',
        'level': 'Advanced',
        'motivation': 'Continuous-Variable QKD relies on precise phase and polarization stabilization. Real-world deployments face dynamic environmental noise. AI/ML offers a powerful tool to adaptively correct drifts autonomously, reducing downtime and improving key rates.',
        'prob_statement': 'Design an ML-based control system for CV-QKD.<br><br><strong>Objective:</strong> Create a model that predicts and corrects phase drifts faster and more accurately than standard PID controllers, while simultaneously flagging anomalous patterns that could indicate eavesdropping.<br><br><strong>Scope:</strong> Use provided or simulated noisy datasets of CV-QKD quadratures.',
        'c1_title': 'Dataset Generation',
        'c1_desc': 'Simulating realistic environmental noise alongside eavesdropping attacks on CV-QKD signals.',
        'c2_title': 'Real-time Prediction',
        'c2_desc': 'Designing ML models lightweight enough for real-time phase correction.',
        'c3_title': 'Anomaly Classification',
        'c3_desc': 'Distinguishing between natural environmental drift and deliberate eavesdropping.',
        'tech': '• Python programming<br>• TensorFlow, PyTorch, or Scikit-learn<br>• Signal processing fundamentals',
        'constraints': '• Inference time must be under 1ms per block to simulate real-time correction<br>• Models must not overfit to the simulated dataset',
        'acceptance': '• ML model outperforms a baseline PID controller in stability<br>• Model accurately flags >95% of simulated anomalies',
        'del_src': 'GitHub repo containing training and inference scripts.',
        'del_rep': '5-page report detailing model architecture, dataset, and training process.',
        'del_demo': 'Video demonstrating the model reacting to simulated phase drift vs PID.',
        'del_add': 'The generated synthetic dataset used for training and testing.',
        'e1_crit': 'ML Performance', 'e1_desc': 'Improvement over baseline PID tracking and stability', 'e1_wt': '40%',
        'e2_crit': 'Anomaly Detection', 'e2_desc': 'F1 score of the eavesdropping classification model', 'e2_wt': '30%',
        'e3_crit': 'Efficiency', 'e3_desc': 'Inference speed and computational overhead', 'e3_wt': '15%',
        'e4_crit': 'Code & Reproducibility', 'e4_desc': 'Quality and documentation of the code repository', 'e4_wt': '15%'
    }
}

for filepath, data in files.items():
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    with open(filepath, 'r') as f:
        content = f.read()

    # Global
    content = content.replace('[Problem Statement Title]', data['title'])
    content = content.replace('[One-line description of the problem]', data['subtitle'])
    content = content.replace('[Company Name]', 'Taqbit Labs')
    content = content.replace('[Company tagline or domain]', 'Quantum-Safe Cybersecurity Solutions')
    content = content.replace('[Level]', data['level'])
    content = content.replace('[e.g., Quantum Computing / Cryptography / Sensing /\n                                Communication]', 'Cybersecurity, QKD, QRNG, PQC')
    content = content.replace('[e.g., Quantum Computing / Cryptography / Sensing / Communication]', 'Cybersecurity, QKD, QRNG, PQC')
    content = content.replace('[City, Country]', 'India')
    content = content.replace('[Year]', '2023')
    content = content.replace('[Company URL]', 'www.taqbit.com')
    
    # Motivation and Problem Statement
    mot_pattern = re.compile(r'\[Describe the motivation behind this problem statement.*?\]', re.DOTALL)
    content = mot_pattern.sub(data['motivation'], content)
    
    prob_pattern = re.compile(r'\[Write a comprehensive problem statement.*?\]', re.DOTALL)
    content = prob_pattern.sub(data['prob_statement'], content)
    
    # Challenges
    content = content.replace('[Challenge 1 Title]', data['c1_title'])
    content = content.replace('[Brief description of this challenge]', data['c1_desc'], 1)
    content = content.replace('[Challenge 2 Title]', data['c2_title'])
    content = content.replace('[Brief description of this challenge]', data['c2_desc'], 1)
    content = content.replace('[Challenge 3 Title]', data['c3_title'])
    content = content.replace('[Brief description of this challenge]', data['c3_desc'], 1)
    # in case any remain
    content = content.replace('[Brief description of this challenge]', '')

    # Requirements
    content = re.sub(r'\[Specify required/recommended:\s*<br>• Programming languages\s*<br>• Frameworks & libraries\s*<br>• Hardware platforms \(if any\)\s*<br>• Cloud services or simulators\]', data['tech'], content)
    content = re.sub(r'\[List technical constraints:\s*<br>• Performance requirements\s*<br>• Memory/resource limits\s*<br>• Compatibility requirements\]', data['constraints'], content)
    content = re.sub(r'\[Define what constitutes a valid solution:\s*<br>• Minimum benchmarks\s*<br>• Required functionality\s*<br>• Quality standards\]', data['acceptance'], content)
    
    # Deliverables
    content = re.sub(r'\[Specify format: GitHub repo, zip file, etc\.\s*Include any naming conventions or structure requirements\.\]', data['del_src'], content)
    content = re.sub(r'\[Specify length \(e.g., 3–5 pages\), format \(PDF\),\s*and what it should cover: approach, methodology, results, analysis\.\]', data['del_rep'], content)
    content = re.sub(r'\[Specify if a video demo, live presentation, or\s*recorded walkthrough is required\. Include duration limits\.\]', data['del_demo'], content)
    content = re.sub(r'\[Any additional submissions: test reports,\s*benchmarks, documentation, datasets, etc\.\]', data['del_add'], content)
    
    # Evaluation Criteria
    content = content.replace('[Criterion 1]', data['e1_crit'])
    content = content.replace('[e.g., Correctness of implementation]', data['e1_desc'])
    content = content.replace('[%]', data['e1_wt'], 1)
    
    content = content.replace('[Criterion 2]', data['e2_crit'])
    content = content.replace('[e.g., Performance & optimization]', data['e2_desc'])
    content = content.replace('[%]', data['e2_wt'], 1)
    
    content = content.replace('[Criterion 3]', data['e3_crit'])
    content = content.replace('[e.g., Innovation & creativity]', data['e3_desc'])
    content = content.replace('[%]', data['e3_wt'], 1)
    
    content = content.replace('[Criterion 4]', data['e4_crit'])
    content = content.replace('[e.g., Clarity of communication]', data['e4_desc'])
    content = content.replace('[%]', data['e4_wt'], 1)

    with open(filepath, 'w') as f:
        f.write(content)

print("Replacement complete.")
