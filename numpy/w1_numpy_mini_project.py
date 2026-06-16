import numpy as np
np.random.seed(42)


# ================================
# AI Agent Performance Analyzer
# ================================

# 5 AI agents tested over 30 days
# Each agent handles random requests (50-200)
# Each request has success rate (0 to 1)
# Response time follows normal distribution

# ================================
# STEP 1 — Generate Data
# ================================

agents = 5
days = 30

# requests per agent per day
requests = np.random.randint(50, 200, (agents, days))

# success rate per agent per day
success = np.random.rand(agents, days)

# response time — mean 200ms std 40ms
response_time = 200 + 40 * np.random.randn(agents, days)
response_time = np.clip(response_time, 50, 500)

print("Data Generated Successfully")
print("Requests shape :", requests.shape)
print("Success shape  :", success.shape)
print("Response shape :", response_time.shape)
print("-" * 50)

# ================================
# STEP 2 — Basic Analysis
# ================================

# Total requests per agent
total_requests = requests.sum(axis=1)
print("Total requests per agent:", total_requests)

# Average success rate per agent
avg_success = success.mean(axis=1)
print("Avg success per agent   :", avg_success)

# Average response time per agent
avg_response = response_time.mean(axis=1)
print("Avg response per agent  :", avg_response)
print("-" * 50)

# ================================
# STEP 3 — Boolean Masking
# ================================

# Days where success rate was below 0.5 (bad days)
bad_days = np.where(success < 0.5)
print("Total bad days across all agents:", len(bad_days[0]))

# Agents with average success above 0.7
good_agents = np.where(avg_success > 0.7)[0] + 1
print("Good agents (above 0.7) :", good_agents)

# Response times above 350ms (slow)
slow_responses = (response_time > 350).sum()
print("Total slow responses    :", slow_responses)
print("-" * 50)

# ================================
# STEP 4 — Aggregations
# ================================

# Best agent overall
best_agent = np.argmax(avg_success) + 1
print("Best agent              :", best_agent)

# Worst agent overall
worst_agent = np.argmin(avg_success) + 1
print("Worst agent             :", worst_agent)

# Most active agent
most_active = np.argmax(total_requests) + 1
print("Most active agent       :", most_active)

# Best day across all agents
daily_success = success.mean(axis=0)
best_day = np.argmax(daily_success) + 1
print("Best day                :", best_day)

# Worst day
worst_day = np.argmin(daily_success) + 1
print("Worst day               :", worst_day)
print("-" * 50)

# ================================
# STEP 5 — Broadcasting
# ================================

# Normalize success rates between 0 and 1
min_success = success.min(axis=1).reshape(agents, 1)
max_success = success.max(axis=1).reshape(agents, 1)
normalized = (success - min_success) / (max_success - min_success)
print("Normalized success (first agent):", normalized[0][:5])

# Mean centering response times
mean_response = response_time.mean(axis=1).reshape(agents, 1)
centered = response_time - mean_response
print("Centered response (first agent) :", centered[0][:5])
print("-" * 50)

# ================================
# STEP 6 — Percentile Analysis
# ================================

# 90th percentile response time per agent
p90_response = np.percentile(response_time, 90, axis=1)
print("P90 response per agent  :", p90_response)

# Agents above 90th percentile response (slowest)
slow_agents = np.where(avg_response > np.percentile(avg_response, 75))[0] + 1
print("Slowest agents          :", slow_agents)
print("-" * 50)

# ================================
# STEP 7 — Final Report
# ================================

print("=" * 50)
print("       FINAL PERFORMANCE REPORT")
print("=" * 50)

for i in range(agents):
    print(f"Agent {i+1}:")
    print(f"  Total Requests : {total_requests[i]}")
    print(f"  Avg Success    : {avg_success[i]:.2f}")
    print(f"  Avg Response   : {avg_response[i]:.2f}ms")
    print(f"  P90 Response   : {p90_response[i]:.2f}ms")
    print("-" * 30)

print(f"\nBest Agent    : Agent {best_agent}")
print(f"Worst Agent   : Agent {worst_agent}")
print(f"Most Active   : Agent {most_active}")
print(f"Best Day      : Day {best_day}")
print(f"Worst Day     : Day {worst_day}")
print("=" * 50)