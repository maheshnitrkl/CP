import os

problems = [
    { "id": "m11-p1", "title": "Binary Tree Preorder Traversal", "difficulty": "Easy", "leetcode": "https://leetcode.com/problems/binary-tree-preorder-traversal/description/", "statement": "Given the root of a binary tree, return the preorder traversal of its nodes' values." },
    { "id": "m11-p2", "title": "Binary Tree Inorder Traversal", "difficulty": "Easy", "leetcode": "https://leetcode.com/problems/binary-tree-inorder-traversal/description/", "statement": "Given the root of a binary tree, return the inorder traversal of its nodes' values." },
    { "id": "m11-p3", "title": "Binary Tree Postorder Traversal", "difficulty": "Easy", "leetcode": "https://leetcode.com/problems/binary-tree-postorder-traversal/description/", "statement": "Given the root of a binary tree, return the postorder traversal of its nodes' values." },
    { "id": "m11-p4", "title": "Maximum Depth of Binary Tree", "difficulty": "Easy", "leetcode": "https://leetcode.com/problems/maximum-depth-of-binary-tree/description/", "statement": "Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node." },
    { "id": "m11-p5", "title": "Diameter of Binary Tree", "difficulty": "Easy", "leetcode": "https://leetcode.com/problems/diameter-of-binary-tree/description/", "statement": "Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root." },
    { "id": "m11-p6", "title": "Binary Tree Right Side View", "difficulty": "Medium", "leetcode": "https://leetcode.com/problems/binary-tree-right-side-view/description/", "statement": "Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom." },
    { "id": "m11-p7", "title": "Path Sum", "difficulty": "Easy", "leetcode": "https://leetcode.com/problems/path-sum/description/", "statement": "Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum." }
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
  <nav class="navbar" id="navbar"><div class="navbar__inner"><a href="../index.html" class="navbar__brand"><span class="navbar__brand-icon">&#x26A1;</span><span>CP-II Lab</span></a><div class="navbar__nav"><a href="../modules/module-11-trees.html" class="navbar__link">&#8592; Back to Module 11: Trees</a></div><div class="navbar__actions"><button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme"></button></div></div></nav>

  <main class="problem-page">
    <header class="problem-header">
      <div class="breadcrumb"><a href="../index.html">Home</a><span class="breadcrumb__sep">&#8250;</span><a href="../modules/module-11-trees.html">Module 11: Trees</a><span class="breadcrumb__sep">&#8250;</span><span class="breadcrumb__current">{title}</span></div>
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
