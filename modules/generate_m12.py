import os

problems = [
    { "id": "m12-p1", "title": "DFS Traversal", "difficulty": "Easy", "leetcode": "https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1", "statement": "Given a connected undirected graph, perform a Depth First Search (DFS) traversal starting from vertex 0." },
    { "id": "m12-p2", "title": "Find if Path Exists in Graph", "difficulty": "Easy", "leetcode": "https://leetcode.com/problems/find-if-path-exists-in-graph/description/", "statement": "There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). Given an array edges, return true if there is a valid path from source to destination, or false otherwise." },
    { "id": "m12-p3", "title": "Keys and Rooms", "difficulty": "Medium", "leetcode": "https://leetcode.com/problems/keys-and-rooms/description/", "statement": "There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. When you visit a room, you may find a set of distinct keys in it that can unlock other rooms." },
    { "id": "m12-p4", "title": "Open the Lock", "difficulty": "Medium", "leetcode": "https://leetcode.com/problems/open-the-lock/description/", "statement": "You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The lock initially starts at '0000'. Given a list of deadends, return the minimum total number of turns required to open the lock, or -1 if it is impossible." },
    { "id": "m12-p5", "title": "Jump Game III", "difficulty": "Medium", "leetcode": "https://leetcode.com/problems/jump-game-iii/description/", "statement": "Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0." },
    { "id": "m12-p6", "title": "Course Schedule", "difficulty": "Medium", "leetcode": "https://leetcode.com/problems/course-schedule/description/", "statement": "There are a total of numCourses courses you have to take. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai. Return true if you can finish all courses. Otherwise, return false." }
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
  <nav class="navbar" id="navbar"><div class="navbar__inner"><a href="../index.html" class="navbar__brand"><span class="navbar__brand-icon">&#x26A1;</span><span>CP-II Lab</span></a><div class="navbar__nav"><a href="../modules/module-12-graphs.html" class="navbar__link">&#8592; Back to Module 12: Graphs</a></div><div class="navbar__actions"><button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme"></button></div></div></nav>

  <main class="problem-page">
    <header class="problem-header">
      <div class="breadcrumb"><a href="../index.html">Home</a><span class="breadcrumb__sep">&#8250;</span><a href="../modules/module-12-graphs.html">Module 12: Graphs</a><span class="breadcrumb__sep">&#8250;</span><span class="breadcrumb__current">{title}</span></div>
      <h1 class="problem-header__title">{title}</h1>
      <div class="problem-header__meta">
        <span class="badge badge--{diff_lower}">{difficulty}</span>
        <a href="{leetcode}" target="_blank" class="badge" style="background:var(--bg-secondary);color:var(--text-primary);border:1px solid var(--border-primary);text-decoration:none;">&#128279; Problem Link</a>
      </div>
    </header>

    <!-- 1. Problem Statement -->
    <section class="problem-section">
      <h2 class="problem-section__title"><span class="icon">&#128220;</span> Problem Statement</h2>
      <div style="color:var(--text-secondary);line-height:1.8;"><p>{statement}</p></div>
    </section>

    <!-- 2. Logic & Core Concept -->
    <section class="problem-section">
      <h2 class="problem-section__title"><span class="icon">&#128218;</span> Logic & Core Concept</h2>
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
