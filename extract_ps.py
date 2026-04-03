import re
import glob

files = [
    'dwave_problem.html',
    'ltimindtree_problem.html',
    'taqbit_problem_1.html',
    'taqbit_problem_2.html',
    'taqbit_problem_3.html'
]

for f in files:
    with open(f, 'r') as file:
        content = file.read()
        title_match = re.search(r'<h1 class="cover__title"[^>]*>(.*?)</h1>', content, re.DOTALL)
        title = title_match.group(1).strip() if title_match else "No Title"
        title = re.sub(r'<[^>]+>', '', title)
        
        subtitle_match = re.search(r'<p class="cover__subtitle"[^>]*>(.*?)</p>', content, re.DOTALL)
        subtitle = subtitle_match.group(1).strip() if subtitle_match else "No Subtitle"
        subtitle = re.sub(r'<[^>]+>', '', subtitle)
        
        blocks = re.findall(r'<div class="fill-block[^>]*>(.*?)</div>', content, re.DOTALL)
        blocks = [re.sub(r'<br\s*/?>', '\n', b) for b in blocks]
        blocks = [re.sub(r'<[^>]+>', '', b).strip() for b in blocks]
        
        print(f"=== {f} ===")
        print("TITLE:", title)
        print("SUBTITLE:", subtitle)
        if len(blocks) > 2:
            print("PROBLEM STATEMENT:\n", blocks[2])

