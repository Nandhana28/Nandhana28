#!/usr/bin/env python3
import requests
import json
from datetime import datetime, timedelta
import os

class CosmicAnalyzer:
    def __init__(self, username):
        self.username = username
        self.github_data = {}
        
    def fetch_github_universe(self):
        """Fetch comprehensive GitHub data"""
        endpoints = {
            'user': f'https://api.github.com/users/{self.username}',
            'repos': f'https://api.github.com/users/{self.username}/repos?sort=updated&per_page=20',
            'events': f'https://api.github.com/users/{self.username}/events?per_page=100'
        }
        
        for key, url in endpoints.items():
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    self.github_data[key] = response.json()
            except Exception as e:
                print(f"Error fetching {key}: {e}")
    
    def generate_code_weather(self):
        """Generate creative code weather report"""
        events = self.github_data.get('events', [])
        recent_activity = []
        
        for event in events:
            try:
                event_date = datetime.strptime(event['created_at'][:10], '%Y-%m-%d').date()
                if event_date >= (datetime.now() - timedelta(days=7)).date():
                    recent_activity.append(event)
            except:
                continue
        
        activity_level = len(recent_activity)
        
        if activity_level > 20:
            return " **Code Hurricane** - Extreme innovation detected!"
        elif activity_level > 10:
            return " **Development Storm** - High velocity coding"
        elif activity_level > 5:
            return " **Clear Skies** - Steady progress"
        else:
            return " **Quiet Night** - Planning phase"
    
    def calculate_growth_trajectory(self):
        """Calculate and project growth metrics"""
        repos = self.github_data.get('repos', [])
        total_stars = sum(repo.get('stargazers_count', 0) for repo in repos)
        total_forks = sum(repo.get('forks_count', 0) for repo in repos)
        
        # Simple growth projection
        growth_factor = (total_stars * 0.3 + total_forks * 0.2 + len(repos) * 0.5)
        
        if growth_factor > 50:
            return " **Hypergrowth Trajectory** - Exponential innovation"
        elif growth_factor > 25:
            return " **Accelerated Growth** - Strong momentum"
        else:
            return " **Steady Growth** - Building foundation"
    
    def update_readme_sections(self):
        """Update dynamic sections in README"""
        try:
            with open('README.md', 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Update code weather
            weather = self.generate_code_weather()
            content = self.update_section(content, 'CODE_WEATHER_START', 'CODE_WEATHER_END', weather)
            
            # Update growth projection
            growth = self.calculate_growth_trajectory()
            content = self.update_section(content, 'GROWTH_PROJECTION_START', 'GROWTH_PROJECTION_END', growth)
            
            with open('README.md', 'w', encoding='utf-8') as file:
                file.write(content)
                
            print(" Successfully updated README sections")
        except Exception as e:
            print(f" Error updating README: {e}")
    
    def update_section(self, content, start_marker, end_marker, new_content):
        """Helper to update specific sections"""
        start = content.find(start_marker) + len(start_marker)
        end = content.find(end_marker)
        
        if start > len(start_marker) and end != -1:
            return content[:start] + f"\n{new_content}\n" + content[end:]
        return content

if __name__ == "__main__":
    print(" Starting Cosmic Analyzer...")
    analyzer = CosmicAnalyzer("Nandhana28")
    analyzer.fetch_github_universe()
    analyzer.update_readme_sections()
    print("🎉 Cosmic analysis complete!")
