import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS before </style>
css_injection = """
        /* Model Answer Drawer & Toggle Button */
        .ans-toggle-btn {
            align-self: flex-start;
            background: rgba(99, 102, 241, 0.12);
            border: 1px solid rgba(99, 102, 241, 0.35);
            color: #c7d2fe;
            font-size: 0.82rem;
            font-weight: 700;
            padding: 6px 14px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin-top: 6px;
        }

        .ans-toggle-btn:hover {
            background: var(--primary);
            color: #ffffff;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.35);
        }

        .ans-toggle-btn.active {
            background: rgba(239, 68, 68, 0.2);
            border-color: rgba(239, 68, 68, 0.5);
            color: #fca5a5;
        }

        .ans-drawer {
            display: none;
            margin-top: 12px;
            padding: 16px 20px;
            background: #0d1322;
            border: 1px solid var(--border);
            border-left: 3px solid var(--accent);
            border-radius: 10px;
            font-size: 0.92rem;
            line-height: 1.6;
            color: #cbd5e1;
            animation: fadeIn 0.2s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .ans-drawer pre {
            background: #060911;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            padding: 12px 16px;
            font-family: 'Fira Code', monospace;
            font-size: 0.85rem;
            overflow-x: auto;
            margin: 10px 0;
            color: #38bdf8;
        }

        .ans-drawer table {
            width: 100%;
            border-collapse: collapse;
            margin: 12px 0;
            font-size: 0.88rem;
        }

        .ans-drawer th, .ans-drawer td {
            border: 1px solid var(--border);
            padding: 8px 12px;
            text-align: left;
        }

        .ans-drawer th {
            background: rgba(99, 102, 241, 0.15);
            color: #a5b4fc;
        }

        .ans-drawer ul, .ans-drawer ol {
            margin-left: 20px;
            margin-bottom: 10px;
        }

        .ans-drawer li {
            margin-bottom: 6px;
        }

        /* Unit Notes View Styles */
        .notes-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
        }

        .notes-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 18px;
            padding-bottom: 14px;
            border-bottom: 1px solid var(--border);
        }

        .notes-link-btn {
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.35);
            color: #34d399;
            text-decoration: none;
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 0.84rem;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
        }

        .notes-link-btn:hover {
            background: var(--success);
            color: #ffffff;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.35);
        }
    </style>
"""

content = content.replace("    </style>", css_injection, 1)

# 2. Add button in view-switch-tabs
old_switch = """                <button class="view-btn" id="btn-mode-syllabus" onclick="switchMode('syllabus')">
                    📖 Complete Official Syllabus
                </button>
            </div>"""

new_switch = """                <button class="view-btn" id="btn-mode-syllabus" onclick="switchMode('syllabus')">
                    📖 Complete Official Syllabus
                </button>
                <button class="view-btn" id="btn-mode-notes" onclick="switchMode('notes')">
                    ⚡ 8+ Marks Unit Notes
                </button>
            </div>"""

content = content.replace(old_switch, new_switch, 1)

# 3. Update updateModeUI()
old_mode_ui = """        function updateModeUI() {
            const qBtn = document.getElementById('btn-mode-questions');
            const sBtn = document.getElementById('btn-mode-syllabus');
            if (qBtn) qBtn.classList.toggle('active', currentMode === 'questions');
            if (sBtn) sBtn.classList.toggle('active', currentMode === 'syllabus');
        }"""

new_mode_ui = """        function updateModeUI() {
            const qBtn = document.getElementById('btn-mode-questions');
            const sBtn = document.getElementById('btn-mode-syllabus');
            const nBtn = document.getElementById('btn-mode-notes');
            if (qBtn) qBtn.classList.toggle('active', currentMode === 'questions');
            if (sBtn) sBtn.classList.toggle('active', currentMode === 'syllabus');
            if (nBtn) nBtn.classList.toggle('active', currentMode === 'notes');
        }"""

content = content.replace(old_mode_ui, new_mode_ui, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html base structure updated successfully!")

