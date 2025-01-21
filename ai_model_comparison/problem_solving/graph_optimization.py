"""
Exercise: Network Resource Optimization Problem

Problem Statement:
You are tasked with designing a system to optimize resource allocation in a distributed network.
The network is represented as a weighted directed graph where:
- Nodes represent computing resources
- Edges represent communication channels
- Weights represent various metrics (latency, bandwidth, cost)

Requirements:
1. Design an algorithm that:
   - Finds the optimal path for resource allocation
   - Minimizes overall system latency
   - Maximizes resource utilization
   - Stays within budget constraints
   - Handles dynamic network changes

2. Constraints:
   - Maximum budget: B units
   - Minimum reliability requirement: R%
   - Maximum latency threshold: L milliseconds
   - Resource capacity limits
   - Real-time adaptation requirements

3. The solution should:
   - Handle network failures gracefully
   - Scale efficiently with network size
   - Support dynamic resource addition/removal
   - Provide alternative solutions when optimal is not possible

4. Expected Analysis:
   - Time complexity analysis
   - Space complexity analysis
   - Scalability considerations
   - Trade-off discussions

Compare how each AI model:
- Approaches problem decomposition
- Considers different algorithms and their trade-offs
- Handles constraint satisfaction
- Explains their reasoning process
- Addresses edge cases and failure scenarios
- Provides optimization strategies
""" 