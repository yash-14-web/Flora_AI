# Flora AI — Agent Execution Guidelines & Contract

> **MANDATORY FOR ALL AI AGENTS:**  
> This file is automatically loaded into your session context. You **must** strictly enforce and adhere to all design, architecture, and workflow rules defined in [DESIGN.md](file:///c:/Data%20Science%20and%20Gen%20Ai%20projects/Flora_AI/DESIGN.md) and [MASTER_CONTEXT.md](file:///c:/Data%20Science%20and%20Gen%20Ai%20projects/Flora_AI/MASTER_CONTEXT.md).

---

## 1. Core Workflow for Every Task

Whenever the user or team assigns a task:
1. **Read & Inspect**:
   - Inspect [DESIGN.md](file:///c:/Data%20Science%20and%20Gen%20Ai%20projects/Flora_AI/DESIGN.md) and relevant existing templates/styles.
   - Never assume what exists—inspect the project structure first.
2. **Define Strict File Scope Before Coding**:
   - **Files to Create**: New files strictly necessary for the assigned task.
   - **Files to Modify**: Existing files that genuinely require updates.
   - **Files NOT to Modify**: Approved pages (e.g., `landing.html`, `login.html`), core styles, or unrelated components.
3. **Incremental Development & Minimum Change Principle**:
   - Build **only** what was requested.
   - Do NOT redesign approved pages or reorganize existing code.
   - Do NOT modify `base.html` or global CSS unless genuinely required and approved.
4. **Technology Stack & Boundaries**:
   - **Frontend**: Django Templates, HTML5, Vanilla CSS (`theme.css`, `components.css`, or dedicated page css), JavaScript.
   - **Backend**: Standard Django views, models, and forms.
   - **AI/ML Boundary**: CNN training code remains in Jupyter notebooks / Python ML pipelines. Django interacts with saved models via decoupled prediction services.
5. **Testing & Regression Check**:
   - Run `python manage.py check` and verify routing.
   - Ensure existing pages and navigation links remain visually and functionally intact.
6. **Task Completion Report**:
   - Summarize files created, files modified, files left untouched, testing results, and regression verification.

---

## 2. Stop & Ask Rules

**STOP and ask the user before proceeding if:**
- The requested page or component already exists.
- The task unexpectedly requires altering an approved page or high-impact shared file (`base.html`, `settings.py`).
- There is an architectural or requirement conflict.
