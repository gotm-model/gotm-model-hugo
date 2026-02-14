#!/usr/bin/env python3
"""
GOTM Documentation Splitter

Splits GOTM_Complete_Documentation.md into Hugo-compatible pages.

Usage:
    python3 source/split_documentation.py
"""

import re
import os
from pathlib import Path

def extract_section(content, section_num, next_section_num=None):
    """Extract a main section from the documentation."""
    if next_section_num:
        pattern = rf'## {section_num}\. (.*?)\n(.*?)(?=\n## {next_section_num}\.)'
    else:
        pattern = rf'## {section_num}\. (.*?)\n(.*?)(?=\n## Appendix|\Z)'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return None, None


def extract_subsection(content, subsection_num, next_subsection_num=None):
    """Extract a subsection from content."""
    subsection_num = subsection_num.replace('.', r'\.')
    if next_subsection_num:
        next_subsection_num = next_subsection_num.replace('.', r'\.')
        pattern = rf'### {subsection_num} (.*?)\n(.*?)(?=### {next_subsection_num})'
    else:
        pattern = rf'### {subsection_num} (.*?)\n(.*?)$'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return None, None


def create_frontmatter(title, weight, toc=True):
    """Create Hugo frontmatter."""
    return f"""---
title: "{title}"
weight: {weight}
bookToc: {str(toc).lower()}
---

"""


def write_file(output_path, title, weight, content):
    """Write a markdown file with frontmatter."""
    filepath = Path(output_path)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(create_frontmatter(title, weight))
        f.write(f"# {title}\n\n")
        f.write(content)
    
    print(f"✓ Created {output_path}")


def main():
    source_file = 'source/GOTM_Complete_Documentation.md'
    output_dir = 'content'
    
    print(f"Reading {source_file}...")
    
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {source_file} not found!")
        print("Make sure you're running this from the repository root.")
        return 1
    
    print(f"\nSplitting documentation into {output_dir}/...\n")
    
    # Section mappings: (section_number, output_path, title, weight)
    sections = {
        '2': ('docs/theory/governing-equations.md', 'Governing Equations', 10),
        '3': ('docs/theory/air-sea-interaction.md', 'Air-Sea Interaction', 20),
        '4': ('docs/theory/equation-of-state.md', 'Equation of State & TEOS-10', 30),
        '5': ('docs/theory/turbulence-introduction.md', 'Turbulence Introduction', 40),
        '6': ('docs/theory/numerical-methods.md', 'Numerical Methods', 50),
        '9': ('docs/theory/turbulence-models.md', 'Turbulence Models (Detailed)', 60),
        '10': ('docs/getting-started/dependencies.md', 'Dependencies', 20),
        '11': ('docs/user-guide/configuration.md', 'Configuration', 10),
        '12': ('docs/user-guide/input-files.md', 'Input Files', 20),
        '14': ('docs/getting-started/installation.md', 'Installation', 10),
        '16': ('docs/reference/publications.md', 'Publications', 10),
        '7': ('docs/modules/architecture.md', 'Architecture', 10),
    }
    
    # Process main sections
    for section_num, (output_path, title, weight) in sections.items():
        next_section = str(int(section_num) + 1)
        _, section_content = extract_section(content, section_num, next_section)
        
        if section_content:
            write_file(os.path.join(output_dir, output_path), title, weight, section_content)
    
    # Process module subsections (section 8)
    module_subsections = {
        '8.1': ('docs/modules/meanflow.md', 'Meanflow Module', 20),
        '8.2': ('docs/modules/turbulence.md', 'Turbulence Module', 30),
        '8.3': ('docs/modules/airsea.md', 'Air-Sea Module', 40),
        '8.4': ('docs/modules/observations.md', 'Observations Module', 50),
        '8.5': ('docs/modules/output.md', 'Output Module', 60),
    }
    
    _, section_8_content = extract_section(content, '8', '9')
    if section_8_content:
        subsections = list(module_subsections.keys())
        for i, subsection_num in enumerate(subsections):
            output_path, title, weight = module_subsections[subsection_num]
            next_sub = subsections[i + 1] if i + 1 < len(subsections) else None
            
            _, sub_content = extract_subsection(section_8_content, subsection_num, next_sub)
            if sub_content:
                write_file(os.path.join(output_dir, output_path), title, weight, sub_content)
    
    # Process extension subsections (section 13)
    extension_subsections = {
        '13.1': ('docs/modules/fabm.md', 'FABM (Biogeochemistry)', 70),
        '13.2': ('docs/modules/stim.md', 'STIM (Ice Models)', 80),
        '13.3': ('docs/modules/cvmix.md', 'CVMix (Community Mixing)', 90),
    }
    
    _, section_13_content = extract_section(content, '13', '14')
    if section_13_content:
        subsections = list(extension_subsections.keys())
        for i, subsection_num in enumerate(subsections):
            output_path, title, weight = extension_subsections[subsection_num]
            next_sub = subsections[i + 1] if i + 1 < len(subsections) else None
            
            _, sub_content = extract_subsection(section_13_content, subsection_num, next_sub)
            if sub_content:
                write_file(os.path.join(output_dir, output_path), title, weight, sub_content)
    
    print("\n" + "="*60)
    print("DOCUMENTATION SPLIT COMPLETE!")
    print("="*60)
    print(f"\nOutput directory: {output_dir}/")
    print("\nNext steps:")
    print("  1. Review generated files")
    print("  2. Test with: hugo server -D")
    print("  3. Commit and push to deploy")
    
    return 0


if __name__ == '__main__':
    exit(main())

