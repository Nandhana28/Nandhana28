#!/usr/bin/env python3
import requests
import random

class ConstellationMapper:
    def __init__(self, username):
        self.username = username
    
    def map_project_constellation(self):
        """Create a creative project visualization"""
        url = f"https://api.github.com/users/{self.username}/repos?sort=updated&per_page=8"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                repos = response.json()
                
                constellation = "###  Project Constellation\\n\\n"
                
                # Creative descriptions based on repo data
                descriptions = [
                    "**{name}** - *Orbiting at {stars} stars* - {desc}",
                    " **{name}** - *Celestial body with {forks} forks* - {desc}",
                    " **{name}** - *Gravitational pull: {watchers} observers* - {desc}",
                    " **{name}** - *Luminous innovation* - {desc}"
                ]
                
                for repo in repos[:4]:  # Top 4 projects
                    desc_template = random.choice(descriptions)
                    repo_desc = desc_template.format(
                        name=repo['name'],
                        stars=repo.get('stargazers_count', 0),
                        forks=repo.get('forks_count', 0),
                        watchers=repo.get('watchers_count', 0),
                        desc=repo.get('description', 'Exploring new frontiers') or 'Exploring new frontiers'
                    )
                    constellation += f"{repo_desc}\\n\\n"
                
                return constellation
        except Exception as e:
            print(f"Error mapping constellation: {e}")
        
        return "###  Project Constellation\\n\\n*Charting new project galaxies...*"
    
    def update_constellation_section(self):
        """Update the constellation section in README"""
        try:
            constellation = self.map_project_constellation()
            
            with open('README.md', 'r', encoding='utf-8') as file:
                content = file.read()
            
            start_marker = '<!-- PROJECT_CONSTELLATION_START -->'
            end_marker = '<!-- PROJECT_CONSTELLATION_END -->'
            
            start = content.find(start_marker) + len(start_marker)
            end = content.find(end_marker)
            
            if start > len(start_marker) and end != -1:
                updated_content = content[:start] + f"\n{constellation}\n" + content[end:]
                
                with open('README.md', 'w', encoding='utf-8') as file:
                    file.write(updated_content)
                    
            print(" Constellation mapped successfully")
        except Exception as e:
            print(f" Error updating constellation: {e}")

if __name__ == "__main__":
    print(" Mapping project constellation...")
    mapper = ConstellationMapper("Nandhana28")
    mapper.update_constellation_section()
    print(" Constellation mapping complete!")
