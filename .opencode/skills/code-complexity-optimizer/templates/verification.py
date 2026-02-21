"""
Verification Template - Quick correctness check for optimizations

Usage:
    from templates.verification import verify_optimization, quick_test_cases
    
    # Define your functions
    def original_func(data):
        # Original implementation
        ...
    
    def optimized_func(data):
        # Optimized implementation
        ...
    
    # Verify they produce same results
    verify_optimization(original_func, optimized_func, quick_test_cases())
"""

import time
from typing import Any, Callable, List, Optional, Tuple


def quick_test_cases() -> List[Tuple]:
    """Generate common test cases for verification."""
    return [
        # Edge cases
        ([],),
        ([], 0),
        ([1],),
        ([1], 1),
        ([1, 2],),
        ([1, 2], 3),
        
        # Typical cases
        ([1, 2, 3, 4, 5],),
        ([1, 2, 3, 4, 5], 6),
        (list(range(100)),),
        (list(range(100)), 50),
        
        # Negative/special values
        ([-1, -2, -3],),
        ([0, 0, 0],),
        ([1, -1, 1, -1],),
        
        # Duplicates
        ([1, 1, 1, 1],),
        ([1, 2, 2, 3],),
    ]


def verify_optimization(
    original: Callable,
    optimized: Callable,
    test_cases: List[Tuple],
    verbose: bool = True
) -> bool:
    """
    Compare outputs of original and optimized functions.
    
    Args:
        original: Original function
        optimized: Optimized function
        test_cases: List of argument tuples to test
        verbose: Print detailed results
    
    Returns:
        True if all outputs match, False otherwise
    """
    all_passed = True
    
    for i, args in enumerate(test_cases):
        try:
            original_result = original(*args)
            optimized_result = optimized(*args)
            
            if original_result != optimized_result:
                all_passed = False
                if verbose:
                    print(f"❌ Case {i+1}: MISMATCH")
                    print(f"   Args: {args}")
                    print(f"   Original: {original_result}")
                    print(f"   Optimized: {optimized_result}")
            else:
                if verbose:
                    print(f"✓ Case {i+1}: PASSED (args={args})")
                    
        except Exception as e:
            all_passed = False
            if verbose:
                print(f"❌ Case {i+1}: ERROR - {e}")
                print(f"   Args: {args}")
    
    if verbose:
        print(f"\n{'='*50}")
        if all_passed:
            print(f"✅ All {len(test_cases)} cases passed!")
        else:
            print(f"⚠️ Some cases failed - optimization may be incorrect")
    
    return all_passed


def benchmark_comparison(
    original: Callable,
    optimized: Callable,
    args: Tuple,
    runs: int = 1000
) -> dict:
    """
    Compare execution time of original vs optimized function.
    
    Args:
        original: Original function
        optimized: Optimized function
        args: Arguments to pass to both functions
        runs: Number of benchmark runs
    
    Returns:
        Dictionary with timing results
    """
    # Warmup
    for _ in range(10):
        original(*args)
        optimized(*args)
    
    # Benchmark original
    start = time.perf_counter()
    for _ in range(runs):
        original(*args)
    original_time = time.perf_counter() - start
    
    # Benchmark optimized
    start = time.perf_counter()
    for _ in range(runs):
        optimized(*args)
    optimized_time = time.perf_counter() - start
    
    speedup = original_time / optimized_time if optimized_time > 0 else float('inf')
    
    return {
        "original_time_ms": round(original_time * 1000 / runs, 4),
        "optimized_time_ms": round(optimized_time * 1000 / runs, 4),
        "speedup": round(speedup, 2),
        "improvement_percent": round((1 - optimized_time / original_time) * 100, 2)
    }


def full_verification(
    original: Callable,
    optimized: Callable,
    test_cases: List[Tuple],
    benchmark_args: Optional[Tuple] = None,
    benchmark_runs: int = 1000
) -> dict:
    """
    Full verification: correctness + performance.
    
    Args:
        original: Original function
        optimized: Optimized function
        test_cases: List of argument tuples for correctness testing
        benchmark_args: Arguments for performance benchmarking
        benchmark_runs: Number of benchmark runs
    
    Returns:
        Dictionary with full verification results
    """
    print("="*50)
    print("OPTIMIZATION VERIFICATION REPORT")
    print("="*50)
    
    # Correctness check
    print("\n📋 CORRECTNESS CHECK")
    print("-"*50)
    correctness = verify_optimization(original, optimized, test_cases)
    
    # Performance check
    if benchmark_args:
        print("\n⚡ PERFORMANCE CHECK")
        print("-"*50)
        perf = benchmark_comparison(original, optimized, benchmark_args, benchmark_runs)
        print(f"Original: {perf['original_time_ms']} ms/call")
        print(f"Optimized: {perf['optimized_time_ms']} ms/call")
        print(f"Speedup: {perf['speedup']}x")
        print(f"Improvement: {perf['improvement_percent']}%")
    else:
        perf = None
    
    # Summary
    print("\n📊 SUMMARY")
    print("-"*50)
    print(f"Correctness: {'✅ PASSED' if correctness else '❌ FAILED'}")
    if perf:
        print(f"Performance: {perf['speedup']}x faster")
    
    return {
        "correctness_passed": correctness,
        "performance": perf
    }


if __name__ == "__main__":
    # Example usage
    def original_find_max(arr):
        max_val = arr[0]
        for val in arr:
            if val > max_val:
                max_val = val
        return max_val
    
    def optimized_find_max(arr):
        return max(arr)  # Built-in is often faster
    
    test_cases = [
        ([1, 2, 3],),
        ([3, 2, 1],),
        ([-1, -2, -3],),
        ([5],),
        (list(range(1000)),),
    ]
    
    full_verification(
        original_find_max,
        optimized_find_max,
        test_cases,
        benchmark_args=(list(range(10000)),),
        benchmark_runs=10000
    )
