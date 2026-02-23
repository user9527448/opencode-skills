#!/usr/bin/env python3
"""
Code Review Auto-Scan Script

Performs automated code quality and security scans on target files.
Use this as a first-pass before manual review.

Usage:
    python auto-scan.py <directory> [--format=json|markdown]
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any

# Common vulnerability patterns
SECURITY_PATTERNS = [
    (r'execute\s*\(\s*[\'"].*?\+', 'Command injection risk: exec() with string concatenation'),
    (r'eval\s*\(', 'Code injection risk: eval() usage'),
    (r'process\.env\.\w+\s*=\s*[\'"]', 'Potential hardcoded secret'),
    (r'sql\s*=\s*[\'"].*?\%s.*?\+', 'SQL injection risk: string formatting'),
    (r'\.innerHTML\s*=', 'XSS risk: innerHTML assignment'),
    (r'fetch\s*\(.*?\+', 'Potential injection in fetch URL'),
]

# Code quality issues
QUALITY_PATTERNS = [
    (r'console\.log\s*\(', 'Debug statement left in code'),
    (r'TODO|FIXME|HACK', 'TODO/FIXME comment found'),
    (r'catch\s*\(\s*\)\s*\{\s*\}', 'Empty catch block'),
    (r'//.*[Aa]s\s+[Aa]ny', 'Type assertion to any'),
    (r'@ts-ignore|@ts-expect-error', 'TypeScript ignore comment'),
]

# Performance anti-patterns
PERFORMANCE_PATTERNS = [
    (r'for\s*\(.*?await.*?query', 'Potential N+1 query in loop'),
    (r'readFileSync|execSync', 'Synchronous blocking operation'),
    (r'\.toLowerCase\(\)\s*===', 'Case-insensitive compare without locale'),
]

def scan_file(filepath: Path) -> Dict[str, Any]:
    """Scan a single file for issues."""
    issues = []
    
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Skip comments
            if line.strip().startswith('//') or line.strip().startswith('#'):
                continue
                
            # Check security patterns
            for pattern, msg in SECURITY_PATTERNS:
                if re.search(pattern, line):
                    issues.append({
                        'severity': 'critical',
                        'type': 'security',
                        'line': i,
                        'message': msg,
                        'code': line.strip()[:80]
                    })
            
            # Check quality patterns
            for pattern, msg in QUALITY_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    issues.append({
                        'severity': 'medium',
                        'type': 'quality',
                        'line': i,
                        'message': msg,
                        'code': line.strip()[:80]
                    })
            
            # Check performance patterns
            for pattern, msg in PERFORMANCE_PATTERNS:
                if re.search(pattern, line):
                    issues.append({
                        'severity': 'high',
                        'type': 'performance',
                        'line': i,
                        'message': msg,
                        'code': line.strip()[:80]
                    })
    
    except Exception as e:
        issues.append({
            'severity': 'info',
            'type': 'error',
            'line': 0,
            'message': f'Could not read file: {e}',
            'code': ''
        })
    
    return {
        'file': str(filepath),
        'issues': issues,
        'issue_count': len(issues)
    }

def scan_directory(directory: str, extensions: List[str] = None) -> Dict[str, Any]:
    """Scan all files in a directory."""
    if extensions is None:
        extensions = ['.js', '.ts', '.py', '.java', '.go', '.rb', '.php']
    
    results = {
        'total_files': 0,
        'total_issues': 0,
        'by_severity': {'critical': 0, 'high': 0, 'medium': 0, 'info': 0},
        'by_type': {'security': 0, 'quality': 0, 'performance': 0, 'error': 0},
        'files': []
    }
    
    path = Path(directory)
    for filepath in path.rglob('*'):
        if filepath.is_file() and filepath.suffix in extensions:
            # Skip node_modules, .git, etc.
            if any(skip in filepath.parts for skip in ['node_modules', '.git', 'dist', 'build']):
                continue
                
            results['total_files'] += 1
            file_result = scan_file(filepath)
            results['files'].append(file_result)
            results['total_issues'] += file_result['issue_count']
            
            for issue in file_result['issues']:
                results['by_severity'][issue['severity']] += 1
                results['by_type'][issue['type']] += 1
    
    return results

def format_markdown(results: Dict[str, Any]) -> str:
    """Format results as markdown."""
    md = """# Auto-Scan Report

## Summary

| Metric | Count |
|--------|-------|
| Files Scanned | {total_files} |
| Total Issues | {total_issues} |
| 🔴 Critical | {critical} |
| 🟠 High | {high} |
| 🟡 Medium | {medium} |
| 🟢 Info | {info} |

## Issues by Type

| Type | Count |
|------|-------|
| Security | {security} |
| Quality | {quality} |
| Performance | {performance} |

## Detailed Issues

""".format(
        total_files=results['total_files'],
        total_issues=results['total_issues'],
        critical=results['by_severity']['critical'],
        high=results['by_severity']['high'],
        medium=results['by_severity']['medium'],
        info=results['by_severity']['info'],
        security=results['by_type']['security'],
        quality=results['by_type']['quality'],
        performance=results['by_type']['performance']
    )
    
    # Group issues by file
    for file_result in results['files']:
        if file_result['issue_count'] > 0:
            md += f"\n### {file_result['file']}\n"
            for issue in file_result['issues']:
                severity_icon = {
                    'critical': '🔴',
                    'high': '🟠',
                    'medium': '🟡',
                    'info': '🟢'
                }.get(issue['severity'], '')
                md += f"- **{severity_icon} {issue['severity'].upper()}** [{issue['type']}] Line {issue['line']}: {issue['message']}\n"
                if issue['code']:
                    md += f"  ```\n  {issue['code']}\n  ```\n"
    
    return md

def main():
    parser = argparse.ArgumentParser(description='Code Review Auto-Scan Tool')
    parser.add_argument('directory', help='Directory to scan')
    parser.add_argument('--format', choices=['json', 'markdown'], default='markdown',
                        help='Output format')
    args = parser.parse_args()
    
    results = scan_directory(args.directory)
    
    if args.format == 'json':
        print(json.dumps(results, indent=2))
    else:
        print(format_markdown(results))
    
    # Exit with error code if critical issues found
    if results['by_severity']['critical'] > 0:
        exit(1)

if __name__ == '__main__':
    main()
