# Job Sequencing with Deadlines - Greedy Method
#
# Time Complexity : O(n^2) - for each job, find a free slot by scanning slots
# Space Complexity: O(n)   - slot array of size n

def job_sequencing(jobs):
    # Sort jobs in descending order of profit (greedy choice)
    jobs.sort(key=lambda x: x[2], reverse=True)

    n = len(jobs)

    # Find the maximum deadline to size the slot array
    max_deadline = max(job[1] for job in jobs)

    # slot[i] = True means time slot i is already taken
    slot = [False] * (max_deadline + 1)

    # Stores the job IDs that are selected
    result = []
    total_profit = 0

    for job in jobs:
        job_id, deadline, profit = job

        # Find a free slot from deadline down to 1
        for t in range(deadline, 0, -1):
            if not slot[t]:
                slot[t] = True
                result.append(job_id)
                total_profit += profit
                break

    return result, total_profit


# ── Driver ────────────────────────────────────────────────
if __name__ == "__main__":
    # Each job: (job_id, deadline, profit)
    jobs = [
        ('J1', 2, 100),
        ('J2', 1, 19),
        ('J3', 2, 27),
        ('J4', 1, 25),
        ('J5', 3, 15),
    ]

    selected_jobs, profit = job_sequencing(jobs)

    print("Selected Jobs :", selected_jobs)
    print("Total Profit  :", profit)
