#!/usr/bin/env python3
"""
Benchmark Template - Performance verification without test coverage

This script provides benchmarking capabilities to verify optimizations
when test coverage is unavailable. It measures execution time and memory
usage before and after code changes.

Usage:
    python benchmark.py <module_path> <function_name> [args...] [--runs N]

Example:
    python benchmark.py my_module process_data --runs 100
    python benchmark.py utils.py find_duplicates "[1,2,3,4,5]" --runs 50
"""

import argparse
import ast
import gc
import importlib.util
import json
import os
import sys
import time
import tracemalloc
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, median, stdev
from typing import Any, Callable


@dataclass
class BenchmarkResult:
    runs: int
    times: list[float]
    memory_peak: int
    memory_current: int
    
    @property
    def avg_time(self) -> float:
        return mean(self.times)
    
    @property
    def median_time(self) -> float:
        return median(self.times)
    
    @property
    def min_time(self) -> float:
        return min(self.times)
    
    @property
    def max_time(self) -> float:
        return max(self.times)
    
    @property
    def std_dev(self) -> float:
        return stdev(self.times) if len(self.times) > 1 else 0
    
    def to_dict(self) -> dict:
        return {
            "runs": self.runs,
            "avg_time_ms": round(self.avg_time * 1000, 4),
            "median_time_ms": round(self.median_time * 1000, 4),
            "min_time_ms": round(self.min_time * 1000, 4),
            "max_time_ms": round(self.max_time * 1000, 4),
            "std_dev_ms": round(self.std_dev * 1000, 4),
            "memory_peak_kb": round(self.memory_peak / 1024, 2),
            "memory_current_kb": round(self.memory_current / 1024, 2),
        }


def load_module_from_file(filepath: str, module_name: str = "benchmark_module"):
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {filepath}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def parse_arg(arg: str) -> Any:
    if arg.lower() == "true":
        return True
    if arg.lower() == "false":
        return False
    try:
        return ast.literal_eval(arg)
    except (ValueError, SyntaxError):
        return arg


def benchmark_function(
    func: Callable,
    args: tuple,
    kwargs: dict,
    runs: int = 100,
    warmup: int = 5,
    measure_memory: bool = True
) -> BenchmarkResult:
    times = []
    memory_peak = 0
    memory_current = 0
    
    for _ in range(warmup):
        try:
            func(*args, **kwargs)
        except Exception:
            pass
    
    if measure_memory:
        tracemalloc.start()
    
    gc.collect()
    
    for _ in range(runs):
        gc.collect()
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"Error during benchmark: {e}")
            continue
        end = time.perf_counter()
        times.append(end - start)
        
        if measure_memory:
            current, peak = tracemalloc.get_traced_memory()
            memory_peak = max(memory_peak, peak)
    
    if measure_memory:
        memory_current, memory_peak_final = tracemalloc.get_traced_memory()
        memory_peak = max(memory_peak, memory_peak_final)
        tracemalloc.stop()
    
    return BenchmarkResult(
        runs=len(times),
        times=times,
        memory_peak=memory_peak,
        memory_current=memory_current
    )


def compare_results(before: BenchmarkResult, after: BenchmarkResult) -> dict:
    time_improvement = (before.avg_time - after.avg_time) / before.avg_time * 100
    memory_improvement = (before.memory_peak - after.memory_peak) / before.memory_peak * 100 if before.memory_peak > 0 else 0
    
    return {
        "time": {
            "before_ms": round(before.avg_time * 1000, 4),
            "after_ms": round(after.avg_time * 1000, 4),
            "improvement_percent": round(time_improvement, 2),
            "speedup_factor": round(before.avg_time / after.avg_time, 2) if after.avg_time > 0 else float('inf')
        },
        "memory": {
            "before_kb": round(before.memory_peak / 1024, 2),
            "after_kb": round(after.memory_peak / 1024, 2),
            "improvement_percent": round(memory_improvement, 2)
        },
        "verdict": "IMPROVED" if time_improvement > 0 else ("REGRESSED" if time_improvement < 0 else "UNCHANGED")
    }


def generate_test_data(size: int, data_type: str = "int") -> Any:
    import random
    if data_type == "int":
        return [random.randint(0, 10000) for _ in range(size)]
    elif data_type == "str":
        return [f"item_{i}" for i in range(size)]
    elif data_type == "dict":
        return [{"id": i, "value": random.random()} for i in range(size)]
    return list(range(size))


def format_result_table(result: BenchmarkResult, title: str = "Benchmark Results") -> str:
    lines = [
        f"\n{'='*50}",
        f"{title:^50}",
        f"{'='*50}",
        f"Runs:              {result.runs}",
        f"Average Time:      {result.avg_time*1000:.4f} ms",
        f"Median Time:       {result.median_time*1000:.4f} ms",
        f"Min Time:          {result.min_time*1000:.4f} ms",
        f"Max Time:          {result.max_time*1000:.4f} ms",
        f"Std Deviation:     {result.std_dev*1000:.4f} ms",
        f"Peak Memory:       {result.memory_peak/1024:.2f} KB",
        f"{'='*50}",
    ]
    return "\n".join(lines)


def format_comparison_table(comparison: dict) -> str:
    lines = [
        f"\n{'='*50}",
        f"{'COMPARISON RESULTS':^50}",
        f"{'='*50}",
        "",
        "TIME:",
        f"  Before:     {comparison['time']['before_ms']:.4f} ms",
        f"  After:      {comparison['time']['after_ms']:.4f} ms",
        f"  Change:     {comparison['time']['improvement_percent']:+.2f}%",
        f"  Speedup:    {comparison['time']['speedup_factor']:.2f}x",
        "",
        "MEMORY:",
        f"  Before:     {comparison['memory']['before_kb']:.2f} KB",
        f"  After:      {comparison['memory']['after_kb']:.2f} KB",
        f"  Change:     {comparison['memory']['improvement_percent']:+.2f}%",
        "",
        f"VERDICT: {comparison['verdict']}",
        f"{'='*50}",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Benchmark Python functions to verify optimizations"
    )
    parser.add_argument("file", help="Python file or module path")
    parser.add_argument("function", help="Function name to benchmark")
    parser.add_argument("args", nargs="*", help="Function arguments (as Python literals)")
    parser.add_argument("--runs", "-n", type=int, default=100, help="Number of benchmark runs")
    parser.add_argument("--warmup", "-w", type=int, default=5, help="Warmup runs")
    parser.add_argument("--compare", "-c", help="Compare with another file (after optimization)")
    parser.add_argument("--generate-data", "-g", type=int, help="Generate test data of given size")
    parser.add_argument("--data-type", choices=["int", "str", "dict"], default="int", help="Type of generated data")
    parser.add_argument("--output", "-o", help="Output file for results (JSON)")
    parser.add_argument("--no-memory", action="store_true", help="Skip memory measurement")
    
    args = parser.parse_args()
    
    parsed_args = [parse_arg(a) for a in args.args]
    
    if args.generate_data:
        test_data = generate_test_data(args.generate_data, args.data_type)
        parsed_args = [test_data]
        print(f"Generated test data: {len(test_data)} items of type '{args.data_type}'")
    
    module = load_module_from_file(args.file)
    func = getattr(module, args.function)
    
    print(f"\nBenchmarking: {args.function}()")
    print(f"File: {args.file}")
    print(f"Arguments: {parsed_args}")
    print(f"Runs: {args.runs} (warmup: {args.warmup})")
    
    result = benchmark_function(
        func,
        tuple(parsed_args),
        {},
        runs=args.runs,
        warmup=args.warmup,
        measure_memory=not args.no_memory
    )
    
    print(format_result_table(result))
    
    output_data = {
        "function": args.function,
        "file": args.file,
        "arguments": str(parsed_args),
        "runs": args.runs,
        "result": result.to_dict()
    }
    
    if args.compare:
        compare_module = load_module_from_file(args.compare, "compare_module")
        compare_func = getattr(compare_module, args.function)
        
        compare_result = benchmark_function(
            compare_func,
            tuple(parsed_args),
            {},
            runs=args.runs,
            warmup=args.warmup,
            measure_memory=not args.no_memory
        )
        
        print(format_result_table(compare_result, "After Optimization"))
        
        comparison = compare_results(result, compare_result)
        print(format_comparison_table(comparison))
        
        output_data["comparison"] = {
            "before_file": args.file,
            "after_file": args.compare,
            "before_result": result.to_dict(),
            "after_result": compare_result.to_dict(),
            "analysis": comparison
        }
    
    if args.output:
        with open(args.output, "w") as f:
            json.dump(output_data, f, indent=2)
        print(f"\nResults saved to: {args.output}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
