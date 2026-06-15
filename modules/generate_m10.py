import os

problems = [
    { "id": "m10-p1", "title": "Climbing Stairs", "difficulty": "Easy", "leetcode": "https://leetcode.com/problems/climbing-stairs/description/", "statement": "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?" },
    { "id": "m10-p2", "title": "Decode Ways", "difficulty": "Medium", "leetcode": "https://leetcode.com/problems/decode-ways/description/", "statement": "A message containing letters from A-Z can be encoded into numbers using the mapping A -> 1, B -> 2, ..., Z -> 26. Given a string s containing only digits, return the number of ways to decode it." },
    { "id": "m10-p3", "title": "House Robber", "difficulty": "Medium", "leetcode": "https://leetcode.com/problems/house-robber/description/", "statement": "You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police." },
    { "id": "m10-p4", "title": "Partition Equal Subset Sum", "difficulty": "Medium", "leetcode": "https://leetcode.com/problems/partition-equal-subset-sum/description/", "statement": "Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise." },
    { "id": "m10-p5", "title": "Unique Paths", "difficulty": "Medium", "leetcode": "https://leetcode.com/problems/unique-paths/description/", "statement": "There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time. Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner." },
    { "id": "m10-p6", "title": "Minimum Path Sum", "difficulty": "Medium", "leetcode": "https://leetcode.com/problems/minimum-path-sum/description/", "statement": "Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path. Note: You can only move either down or right at any point in time." },
    { "id": "m10-p7", "title": "Longest Increasing Subsequence", "difficulty": "Medium", "leetcode": "https://leetcode.com/problems/longest-increasing-subsequence/description/", "statement": "Given an integer array nums, return the length of the longest strictly increasing subsequence." }
]

template = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - CP-II Lab</title>
  <link rel="stylesheet" href="../css/main.css">
  <link rel="stylesheet" href="../css/components.css">
  <link rel="stylesheet" href="../css/problem.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#x26A1;</text></svg>">
</head>
<body class="bg-dots">
  <nav class="navbar" id="navbar"><div class="navbar__inner"><a href="../index.html" class="navbar__brand"><span class="navbar__brand-icon">&#x26A1;</span><span>CP-II Lab</span></a><div class="navbar__nav"><a href="../modules/module-10-dp.html" class="navbar__link">&#8592; Back to Module 10: DP</a></div><div class="navbar__actions"><button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme"></button></div></div></nav>

  <main class="problem-page">
    <header class="problem-header">
      <div class="breadcrumb"><a href="../index.html">Home</a><span class="breadcrumb__sep">&#8250;</span><a href="../modules/module-10-dp.html">Module 10: DP</a><span class="breadcrumb__sep">&#8250;</span><span class="breadcrumb__current">{title}</span></div>
      <h1 class="problem-header__title">{title}</h1>
      <div class="problem-header__meta">
        <span class="badge badge--{diff_lower}">{difficulty}</span>
        <a href="{leetcode}" target="_blank" class="badge" style="background:var(--bg-secondary);color:var(--text-primary);border:1px solid var(--border-primary);text-decoration:none;">&#128279; LeetCode</a>
      </div>
    </header>

    <!-- 1. Problem Statement -->
    <section class="problem-section">
      <h2 class="problem-section__title"><span class="icon">&#128220;</span> Problem Statement</h2>
      <div style="color:var(--text-secondary);line-height:1.8;"><p>{statement}</p></div>
    </section>

    <!-- 2. Mathematical Foundation -->
    <section class="problem-section">
      <h2 class="problem-section__title"><span class="icon">&#128218;</span> Mathematical Foundation</h2>
      <div class="math-block">
        TBD
      </div>
    </section>

    <!-- 3. Approach Progression -->
    <section class="problem-section">
      <h2 class="problem-section__title"><span class="icon">&#128161;</span> Approach Progression: Brute Force &#8594; Optimal</h2>
      TBD
    </section>

    <!-- 4. Interactive Visualization -->
    <section class="problem-section" id="visualization">
      <h2 class="problem-section__title"><span class="icon">&#10024;</span> Interactive Visualization</h2>
      <div class="visualizer" id="viz">
        TBD
      </div>
    </section>

    <!-- 5. Implementation -->
    <section class="problem-section">
      <h2 class="problem-section__title"><span class="icon">&#128187;</span> Optimal Implementation</h2>
      <div class="code-block"><div class="code-block__header"><div class="code-block__tabs"><button class="code-block__tab active" data-lang="cpp">C++</button><button class="code-block__tab" data-lang="python">Python</button></div><button class="code-block__copy">&#128203; Copy</button></div><div class="code-block__body"><div class="code-block__content active" data-lang="cpp"><pre><code class="language-cpp">TBD</code></pre></div><div class="code-block__content" data-lang="python"><pre><code class="language-python">TBD</code></pre></div></div></div>
    </section>
  </main>

  <footer class="footer" style="margin-top: 4rem; padding: 2rem 0; text-align: center; color: var(--text-tertiary); border-top: 1px solid var(--border-primary);">
    <p>CP-II Lab &copy; 2026. Built for learning.</p>
  </footer>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-cpp.min.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
"""

for p in problems:
    filepath = f"d:/CP_II_Website/problems/{p['id']}.html"
    content = template.format(
        title=p["title"],
        difficulty=p["difficulty"],
        diff_lower=p["difficulty"].lower(),
        leetcode=p["leetcode"],
        statement=p["statement"]
    )
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated {filepath}")
