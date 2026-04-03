import shutil
import os
import subprocess

# 1. Copy template
base_tmpl = 'Problem_statement/problem_statement_template.html'
p1 = 'website/taqbit_problem_1.html'
p2 = 'website/taqbit_problem_2.html'
p3 = 'website/taqbit_problem_3.html'

shutil.copy(base_tmpl, p1)
shutil.copy(base_tmpl, p2)
shutil.copy(base_tmpl, p3)

# 2. Run update_taqbit.py which cleans up the templates
subprocess.run(['python3', 'update_taqbit.py'])

# 3. Add specific titles
def replace_in_file(filepath, old, new):
    with open(filepath, 'r') as f:
        content = f.read()
    with open(filepath, 'w') as f:
        f.write(content.replace(old, new))

# Problem 1 specific
replace_in_file(p1, '<span class="fill">[Detailed Title of the Problem Statement]</span>', '<span class="fill">Decoy-state parameter estimation for Twin-Field QKD</span>')
replace_in_file(p1, '<span class="fill">[One-sentence summary of what the students will build/solve]</span>', '<span class="fill">Analyze and implement decoy-state methods for TF-QKD under realistic imperfections and finite-size effects.</span>')

# Problem 2 specific
replace_in_file(p2, '<span class="fill">[Detailed Title of the Problem Statement]</span>', '<span class="fill">Comparative analysis of Twin-Field QKD variants: operational and security subtleties</span>')
replace_in_file(p2, '<span class="fill">[One-sentence summary of what the students will build/solve]</span>', '<span class="fill">Systematically study and explain subtle differences between multiple TF-QKD variants.</span>')

# Problem 3 specific
replace_in_file(p3, '<span class="fill">[Detailed Title of the Problem Statement]</span>', '<span class="fill">AI/ML for adaptive stabilization and anomaly detection in Continuous-Variable QKD</span>')
replace_in_file(p3, '<span class="fill">[One-sentence summary of what the students will build/solve]</span>', '<span class="fill">Develop machine learning models to dynamically stabilize continuous-variable QKD systems.</span>')
replace_in_file(p3, '<p class="fill">[Can machine learning models predict and correct rapid phase drifts in CV-QKD systems while simultaneously detecting anomalous interventions typical of eavesdroppers?]</p>', '<p class="fill">Can machine learning models predict and correct rapid phase drifts in CV-QKD systems?</p>')

# 4. Apply logo corrections
for f in [p1, p2, p3]:
    replace_in_file(f, 'src="../Logo_NQM.png"', 'src="assets/Logo_NQM.png"')
    replace_in_file(f, 'src="../iiti_logo.png"', 'src="assets/iiti_logo.png"')

print("Rebuild done")
