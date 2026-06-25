import os
import re

BASE_DIR = r"C:\Users\ishan\Documents\Projects\Awesome-RLHF"
os.makedirs(os.path.join(BASE_DIR, 'assets'), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, 'pages'), exist_ok=True)

svg_banner = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8A2BE2;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#FF1493;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad)" />
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-size="48" font-weight="bold" fill="#ffffff">Awesome RLHF</text>
  <text x="50%" y="75%" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-size="24" fill="#f0f0f0">Reinforcement Learning from Human Feedback</text>
</svg>'''

with open(os.path.join(BASE_DIR, 'assets/banner.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_banner)

pages_data = {
    "The Actor-Critic Foundation (PPO Era, ~2019–2022)": ("actor-critic-foundation.md", "## Actor-Critic Pipeline\n\n```mermaid\ngraph TD;\n    SFT[Supervised Fine-Tuning] --> RM[Reward Model Training]\n    RM --> PPO[PPO Optimization]\n```"),
    "The Non-RL Direct Preference Shift (DPO Era, ~2023–2024)": ("dpo-era.md", "## DPO Pipeline\n\n```mermaid\ngraph TD;\n    Pref[Preference Data] --> Loss[Cross-Entropy Loss]\n    Loss --> Opt[Implicit Reward Engine]\n```"),
    "The Scaled Inference-Time & AI-Feedback Era (~2024–Present)": ("rlaif-era.md", "## RLAIF Pipeline\n\n```mermaid\ngraph TD;\n    Model[AI Model] --> Gen[Generate Responses]\n    Gen --> Eval[AI Verifier/Compiler]\n    Eval --> Score[Feedback Scores]\n    Score --> Train[Iterative Self-Correction]\n```"),
    "Pairwise Comparisons (Bradley-Terry Model)": ("pairwise-comparisons.md", "## Bradley-Terry Model\n\n```mermaid\ngraph LR;\n    Prompt --> A[Response A]\n    Prompt --> B[Response B]\n    A --> Eval[Evaluator]\n    B --> Eval\n    Eval --> Choice[Chosen vs Rejected]\n```"),
    "Listwise / K-Pair Rankings": ("listwise-rankings.md", "## Listwise Ranking\n\n```mermaid\ngraph LR;\n    Prompt --> Gen[Generate K Responses]\n    Gen --> Rank[Rank 1 to K]\n    Rank --> Loss[Ranking Loss Optimization]\n```"),
    "Binary Binary Utility Mapping (KTO Type)": ("binary-utility-mapping.md", "## KTO Process\n\n```mermaid\ngraph LR;\n    Input --> Output\n    Output --> Feedback[Good/Bad Signal]\n    Feedback --> Update[Utility Update]\n```"),
    "PPO (Proximal Policy Optimization)": ("ppo.md", "## PPO Algorithm\n\n```mermaid\ngraph TD;\n    Policy --> Action\n    Action --> Reward[Reward Model Score]\n    Reward --> KL[KL Penalty vs Ref Model]\n    KL --> Update[Policy Update]\n```"),
    "DPO (Direct Preference Optimization)": ("dpo.md", "## DPO Algorithm\n\n```mermaid\ngraph LR;\n    Data[Chosen/Rejected Pair] --> Ratio[Log-likelihood Ratio]\n    Ratio --> Loss[Implicit Reward Minimization]\n```"),
    "IPO (Identity Preference Optimization)": ("ipo.md", "## IPO Regularization\n\n```mermaid\ngraph LR;\n    DPO[DPO Base] --> Reg[RMS Regularizer]\n    Reg --> Out[Maintains Output Diversity]\n```"),
    "ORPO (Odds Ratio Preference Optimization)": ("orpo.md", "## ORPO Framework\n\n```mermaid\ngraph TD;\n    SFT[SFT Loss] --> Blend[Blended Monolithic Loss]\n    OddsRatio[Odds Ratio Penalty] --> Blend\n```"),
    "Frontier Safety Guardrail Hardening": ("frontier-safety.md", "## Safety Hardening\n\n```mermaid\ngraph TD;\n    RedTeam[Toxic Prompts] --> Eval[Safety Evaluator]\n    Eval --> Refusal[Prefer Safe Refusals]\n```"),
    "Conversational Persona Formatting": ("conversational-persona.md", "## Persona Formatting\n\n```mermaid\ngraph TD;\n    Raw[Raw Output] --> Pref[Markdown & Tone Preferences]\n    Pref --> Tune[Enterprise Assistant Persona]\n```"),
    "Mathematical & Software Logic Verification": ("math-software-logic.md", "## PRM Logic Verification\n\n```mermaid\ngraph TD;\n    Step1 --> Step2\n    Step2 --> PRM[Process-Supervised Reward]\n    PRM --> Check[Check Syntax/Logic]\n```")
}

for title, (filename, content) in pages_data.items():
    full_content = f"# {title}\\n\\nDetailed information and breakdown of {title}.\\n\\n{content}\\n\\n[Back to README](../README.md)"
    with open(os.path.join(BASE_DIR, 'pages', filename), 'w', encoding='utf-8') as f:
        f.write(full_content)

readme_path = os.path.join(BASE_DIR, 'README.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    readme_text = f.read()

# Emojis and Banners
if "Awesome RLHF Banner" not in readme_text:
    readme_text = readme_text.replace("# Awesome-RLHF", "# Awesome-RLHF \U0001F680 \U0001F9E0\n\n![Awesome RLHF Banner](assets/banner.svg)\n\n<a href=\"https://github.com/ishandutta2007/Awesome-Awesome-Awesome\"><img src=\"https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github\" alt=\"Awesome\"/></a><a href=\"https://discord.gg/jc4xtF58Ve\"><img src=\"https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white\" alt=\"Discord\" /></a><a href=\"https://github.com/ishandutta2007\"><img alt=\"GitHub followers\" src=\"https://img.shields.io/github/followers/ishandutta2007?label=Follow\" /></a>\n")

# Replace Links in tables
for title, (filename, _) in pages_data.items():
    readme_text = readme_text.replace(f"**{title}**", f"**[{title}](pages/{filename})**")

# Replace awesome link
readme_text = readme_text.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")

# Fix starplot
readme_text = readme_text.replace("chartrepos", "chart?repos")

# Add Star History
star_history = """
## \u2B50 Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-RLHF&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-RLHF&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-RLHF&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-RLHF&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
if "Star History" not in readme_text:
    readme_text += star_history

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme_text)
