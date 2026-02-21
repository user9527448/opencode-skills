#!/usr/bin/env python3
"""
Complexity Analyzer - Multi-language code complexity analysis tool

This script provides automated complexity analysis for multiple programming languages.
It can be used to analyze code before and after optimization to measure improvements.

Supported Languages:
- Python, JavaScript, TypeScript, Java, C/C++, Go, PHP, Ruby, Swift, Rust, Kotlin, Scala

Usage:
    python analyze.py <file_or_directory> [--format json|text] [--output file]

Requirements:
    pip install lizard radon escomplex

Example:
    python analyze.py src/utils.py
    python analyze.py ./src --format json --output report.json
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


def run_command(cmd: list[str]) -> tuple[int, str, str]:
    """Run a shell command and return exit code, stdout, stderr."""
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=60
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "Command timed out"
    except FileNotFoundError:
        return -1, "", f"Command not found: {cmd[0]}"


def analyze_with_lizard(filepath: str) -> dict[str, Any]:
    """
    Analyze code complexity using lizard.
    Supports: Python, JS, TS, Java, C/C++, Go, PHP, Ruby, Swift, Rust, etc.
    """
    result = {
        "tool": "lizard",
        "file": filepath,
        "functions": [],
        "summary": {}
    }
    
    code, stdout, stderr = run_command(["lizard", filepath, "--json"])
    
    if code == 0 and stdout:
        try:
            data = json.loads(stdout)
            for item in data:
                fn_info = {
                    "name": item.get("name", "unknown"),
                    "start_line": item.get("start_line", 0),
                    "end_line": item.get("end_line", 0),
                    "cyclomatic_complexity": item.get("cyclomatic_complexity", 0),
                    "token_count": item.get("token_count", 0),
                    "parameter_count": item.get("parameter_count", 0),
                    "length": item.get("length", 0),
                    "nloc": item.get("nloc", 0),  # Non-comment lines of code
                }
                result["functions"].append(fn_info)
            
            # Calculate summary
            if result["functions"]:
                total_cc = sum(f["cyclomatic_complexity"] for f in result["functions"])
                result["summary"] = {
                    "total_functions": len(result["functions"]),
                    "total_cyclomatic_complexity": total_cc,
                    "average_cc": round(total_cc / len(result["functions"]), 2),
                    "max_cc": max(f["cyclomatic_complexity"] for f in result["functions"]),
                    "total_nloc": sum(f["nloc"] for f in result["functions"]),
                }
        except json.JSONDecodeError:
            result["error"] = "Failed to parse lizard output"
    else:
        result["error"] = stderr or "lizard command failed"
    
    return result


def analyze_python_radon(filepath: str) -> dict[str, Any]:
    """Analyze Python code using radon (more detailed Python analysis)."""
    result = {
        "tool": "radon",
        "file": filepath,
        "cyclomatic_complexity": [],
        "maintainability_index": None,
        "raw_metrics": None
    }
    
    # Cyclomatic Complexity
    code, stdout, stderr = run_command(["radon", "cc", filepath, "-j"])
    if code == 0 and stdout:
        try:
            result["cyclomatic_complexity"] = json.loads(stdout)
        except json.JSONDecodeError:
            pass
    
    # Maintainability Index
    code, stdout, stderr = run_command(["radon", "mi", filepath, "-j"])
    if code == 0 and stdout:
        try:
            mi_data = json.loads(stdout)
            if filepath in mi_data:
                result["maintainability_index"] = mi_data[filepath]
        except json.JSONDecodeError:
            pass
    
    # Raw metrics
    code, stdout, stderr = run_command(["radon", "raw", filepath, "-j"])
    if code == 0 and stdout:
        try:
            raw_data = json.loads(stdout)
            if filepath in raw_data:
                result["raw_metrics"] = raw_data[filepath]
        except json.JSONDecodeError:
            pass
    
    return result


def analyze_javascript_escomplex(filepath: str) -> dict[str, Any]:
    """Analyze JavaScript/TypeScript using escomplex."""
    result = {
        "tool": "escomplex",
        "file": filepath,
        "metrics": None
    }
    
    # Check if escomplex is available
    code, stdout, stderr = run_command(["npx", "escomplex", filepath, "--format", "json"])
    if code == 0 and stdout:
        try:
            result["metrics"] = json.loads(stdout)
        except json.JSONDecodeError:
            result["error"] = "Failed to parse escomplex output"
    else:
        result["error"] = stderr or "escomplex not available"
    
    return result


def get_file_extension(filepath: str) -> str:
    """Get file extension in lowercase."""
    return Path(filepath).suffix.lower()


def detect_language(filepath: str) -> str:
    """Detect programming language from file extension."""
    ext_map = {
        ".py": "python",
        ".js": "javascript",
        ".mjs": "javascript",
        ".cjs": "javascript",
        ".ts": "typescript",
        ".tsx": "typescript",
        ".jsx": "javascript",
        ".java": "java",
        ".c": "c",
        ".cpp": "cpp",
        ".cc": "cpp",
        ".cxx": "cpp",
        ".h": "c",
        ".hpp": "cpp",
        ".go": "go",
        ".php": "php",
        ".rb": "ruby",
        ".swift": "swift",
        ".rs": "rust",
        ".kt": "kotlin",
        ".scala": "scala",
        ".cs": "csharp",
    }
    ext = get_file_extension(filepath)
    return ext_map.get(ext, "unknown")


def analyze_file(filepath: str) -> dict[str, Any]:
    """Analyze a single file and return comprehensive complexity metrics."""
    if not os.path.exists(filepath):
        return {"error": f"File not found: {filepath}"}
    
    language = detect_language(filepath)
    result = {
        "file": filepath,
        "language": language,
        "analyses": []
    }
    
    # Always try lizard (multi-language)
    lizard_result = analyze_with_lizard(filepath)
    if "error" not in lizard_result:
        result["analyses"].append(lizard_result)
    
    # Language-specific analysis
    if language == "python":
        radon_result = analyze_python_radon(filepath)
        if radon_result.get("cyclomatic_complexity") or radon_result.get("maintainability_index"):
            result["analyses"].append(radon_result)
    
    elif language in ("javascript", "typescript"):
        escomplex_result = analyze_javascript_escomplex(filepath)
        if "metrics" in escomplex_result and escomplex_result["metrics"]:
            result["analyses"].append(escomplex_result)
    
    return result


def analyze_directory(dirpath: str) -> dict[str, Any]:
    """Analyze all code files in a directory."""
    if not os.path.isdir(dirpath):
        return {"error": f"Directory not found: {dirpath}"}
    
    result = {
        "directory": dirpath,
        "files": [],
        "summary": {
            "total_files": 0,
            "total_functions": 0,
            "total_cc": 0,
            "by_language": {}
        }
    }
    
    # Common code file extensions
    code_extensions = {
        ".py", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx",
        ".java", ".c", ".cpp", ".cc", ".cxx", ".h", ".hpp",
        ".go", ".php", ".rb", ".swift", ".rs", ".kt", ".scala", ".cs"
    }
    
    for root, _, files in os.walk(dirpath):
        # Skip common non-source directories
        if any(skip in root for skip in ["node_modules", ".git", "__pycache__", "venv", "build", "dist"]):
            continue
        
        for file in files:
            ext = Path(file).suffix.lower()
            if ext in code_extensions:
                filepath = os.path.join(root, file)
                file_result = analyze_file(filepath)
                result["files"].append(file_result)
                
                # Update summary
                result["summary"]["total_files"] += 1
                lang = file_result.get("language", "unknown")
                result["summary"]["by_language"][lang] = result["summary"]["by_language"].get(lang, 0) + 1
                
                for analysis in file_result.get("analyses", []):
                    if "summary" in analysis:
                        result["summary"]["total_functions"] += analysis["summary"].get("total_functions", 0)
                        result["summary"]["total_cc"] += analysis["summary"].get("total_cyclomatic_complexity", 0)
    
    return result


def format_text_output(data: dict[str, Any]) -> str:
    """Format analysis results as human-readable text."""
    lines = []
    
    if "files" in data:
        # Directory analysis
        lines.append("=" * 60)
        lines.append(f"DIRECTORY ANALYSIS: {data['directory']}")
        lines.append("=" * 60)
        
        for file_result in data["files"]:
            lines.append("")
            lines.extend(format_file_text(file_result))
        
        lines.append("")
        lines.append("=" * 60)
        lines.append("SUMMARY")
        lines.append("=" * 60)
        summary = data["summary"]
        lines.append(f"Total Files: {summary['total_files']}")
        lines.append(f"Total Functions: {summary['total_functions']}")
        lines.append(f"Total Cyclomatic Complexity: {summary['total_cc']}")
        lines.append(f"By Language: {summary['by_language']}")
    else:
        # Single file analysis
        lines.extend(format_file_text(data))
    
    return "\n".join(lines)


def format_file_text(file_result: dict[str, Any]) -> list[str]:
    """Format a single file's analysis as text."""
    lines = []
    lines.append("-" * 60)
    lines.append(f"FILE: {file_result['file']}")
    lines.append(f"LANGUAGE: {file_result['language']}")
    lines.append("-" * 60)
    
    for analysis in file_result.get("analyses", []):
        tool = analysis.get("tool", "unknown")
        
        if tool == "lizard" and "summary" in analysis:
            summary = analysis["summary"]
            lines.append(f"\n[Lizard Analysis]")
            lines.append(f"  Functions: {summary['total_functions']}")
            lines.append(f"  Avg CC: {summary['average_cc']}")
            lines.append(f"  Max CC: {summary['max_cc']}")
            lines.append(f"  Non-comment LOC: {summary['total_nloc']}")
            
            lines.append(f"\n  Top Complex Functions:")
            sorted_fns = sorted(analysis["functions"], key=lambda x: x["cyclomatic_complexity"], reverse=True)
            for fn in sorted_fns[:5]:  # Top 5
                lines.append(f"    - {fn['name']}() [Line {fn['start_line']}] CC={fn['cyclomatic_complexity']}")
        
        elif tool == "radon":
            lines.append(f"\n[Radon Analysis]")
            if analysis.get("maintainability_index"):
                mi = analysis["maintainability_index"]
                lines.append(f"  Maintainability Index: {mi}")
            if analysis.get("raw_metrics"):
                raw = analysis["raw_metrics"]
                lines.append(f"  LOC: {raw.get('loc', 'N/A')}")
                lines.append(f"  LLOC: {raw.get('lloc', 'N/A')}")
                lines.append(f"  SLOC: {raw.get('sloc', 'N/A')}")
    
    return lines


def check_tools() -> dict[str, bool]:
    """Check which analysis tools are available."""
    tools = {
        "lizard": False,
        "radon": False,
        "node/npm": False,
    }
    
    # Check lizard
    code, _, _ = run_command(["lizard", "--version"])
    tools["lizard"] = code == 0
    
    # Check radon
    code, _, _ = run_command(["radon", "--version"])
    tools["radon"] = code == 0
    
    # Check node
    code, _, _ = run_command(["node", "--version"])
    tools["node/npm"] = code == 0
    
    return tools


def main():
    parser = argparse.ArgumentParser(
        description="Multi-language code complexity analyzer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python analyze.py src/utils.py
  python analyze.py ./src --format json --output report.json
  python analyze.py . --check-tools
        """
    )
    parser.add_argument("path", nargs="?", help="File or directory to analyze")
    parser.add_argument("--format", "-f", choices=["json", "text"], default="text", help="Output format")
    parser.add_argument("--output", "-o", help="Output file (default: stdout)")
    parser.add_argument("--check-tools", action="store_true", help="Check which analysis tools are available")
    
    args = parser.parse_args()
    
    if args.check_tools:
        tools = check_tools()
        print("Available Analysis Tools:")
        for tool, available in tools.items():
            status = "✓ Available" if available else "✗ Not installed"
            print(f"  {tool}: {status}")
        
        if not all(tools.values()):
            print("\nTo install missing tools:")
            if not tools["lizard"]:
                print("  pip install lizard")
            if not tools["radon"]:
                print("  pip install radon")
        return 0
    
    if not args.path:
        parser.print_help()
        return 1
    
    path = args.path
    
    if os.path.isfile(path):
        result = analyze_file(path)
    elif os.path.isdir(path):
        result = analyze_directory(path)
    else:
        print(f"Error: Path not found: {path}", file=sys.stderr)
        return 1
    
    # Format output
    if args.format == "json":
        output = json.dumps(result, indent=2)
    else:
        output = format_text_output(result)
    
    # Write output
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Analysis written to: {args.output}")
    else:
        print(output)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
