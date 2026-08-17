# Flora AI — Design & Development Rules

**Project:** Flora AI  
**File:** `DESIGN.md`  
**Purpose:** Global design, structure, and development rules for all developers and AI coding agents.

---

# 1. IMPORTANT — READ THIS FIRST

Before starting ANY development task in the Flora AI project:

1. Read this `DESIGN.md` completely.
2. Inspect the existing project structure.
3. Inspect the files related to the assigned task.
4. Inspect existing pages/components before creating anything.
5. Create a short implementation plan.
6. Identify exactly which files need to be created or modified.
7. Implement only the assigned task.
8. Do not modify unrelated pages, components, styles, or functionality.
9. Test the implementation.
10. Report the files created and modified.

`DESIGN.md` is a project-level development contract.

Every developer and AI coding agent must follow it.

---

# 2. PROJECT PRINCIPLE

Flora AI is developed incrementally.

The project must not be rebuilt or redesigned whenever a new feature is added.

Existing functionality and design must be preserved unless a task explicitly requests a change.

The core principle is:

> Build the requested feature without unnecessarily changing anything that already works.

---

# 3. TECHNOLOGY

Flora AI uses:

* Python
* Django
* Django Templates
* HTML
* CSS
* JavaScript

Do NOT introduce React, Vue, Angular, or another frontend framework unless explicitly approved.

Use Django Template inheritance and reusable components where appropriate.

---

# 4. DESIGN SYSTEM

Flora AI should have one consistent visual language.

The design should communicate:

* Plant health
* Agriculture
* Artificial intelligence
* Trust
* Simplicity
* Modern technology

The overall interface should be:

* Clean
* Modern
* Professional
* Minimal
* Friendly
* Responsive
* Easy to understand

---

# 5. DESIGN CONSISTENCY RULE

Once a page has been approved, its design is considered STABLE.

Developers must NOT redesign an approved page while working on another feature.

For example:

If `landing.html` has already been approved:

A developer assigned to create:

* Login
* Registration
* Dashboard
* Profile
* Detection

must NOT modify the landing page design unless the task explicitly says:

> "Modify the landing page."

---

# 6. CRITICAL — NO UNAUTHORIZED DESIGN CHANGES

A developer must NOT change:

* Colors
* Typography
* Layout
* Spacing
* Buttons
* Navigation
* Footer
* Hero section
* Cards
* Images
* Animations
* Responsive behavior
* Existing page structure

of an unrelated page.

Example:

Task:
> Create Login and Registration pages.

Allowed:
```text
templates/pages/login.html
templates/pages/register.html
static/css/auth.css (or modular auth additions)
static/js/auth.js
```

Not automatically allowed:
```text
templates/pages/landing.html
static/css/landing.css
templates/base.html
```
unless modification of those files is genuinely required and approved.

---

# 7. BASE TEMPLATE RULE

`base.html` is a shared and high-impact file.

Because multiple pages may inherit from it, changing it can affect the entire application.

Therefore:

Before modifying `base.html`:

1. Inspect all pages that depend on it.
2. Determine why the modification is necessary.
3. Include the reason in the implementation plan.
4. Make the smallest possible change.
5. Test affected pages.

If `base.html` does not need to be changed:

DO NOT CHANGE IT.

---

# 8. GLOBAL CSS RULE

Global CSS files are shared resources.

Do not modify global CSS simply to make one page look correct.

Prefer page-specific or component-specific styling when appropriate.

Example:

If Login needs special styling:

Prefer:
```text
static/css/auth.css
```
instead of unnecessarily changing:
```text
static/css/base.css
```

---

# 9. EXISTING PAGE PROTECTION RULE

Before modifying any existing page, determine:

1. Is this page directly related to the assigned task?
2. Is modification actually required?
3. Will the modification affect another page?
4. Can the task be completed without modifying it?

If the answer to #4 is YES:

DO NOT MODIFY THE EXISTING PAGE.

---

# 10. FILE SCOPE RULE

Every task must have a defined file scope.

Before coding, the developer/agent must identify:

## Files to Create
List the new files required.

## Files to Modify
List the existing files that genuinely need changes.

## Files That Must NOT Be Modified
Identify important unrelated files/pages that should remain untouched.

Example:
```text
Task:
Create Login Page

Files to create:
- templates/pages/login.html
- static/css/auth.css

Files to modify:
- config/urls.py

Files that must not be modified:
- templates/pages/landing.html
- templates/pages/dashboard.html
```

---

# 11. MINIMUM CHANGE PRINCIPLE

Always make the smallest change required to complete the task.

Do not rewrite an entire file when a small modification is sufficient.

Do not reorganize unrelated code.

Do not refactor unrelated components.

Do not "clean up" unrelated files during another task.

If refactoring is required, create a separate task.

---

# 12. DO NOT OVERWRITE OTHER DEVELOPERS' WORK

Flora AI is a collaborative project.

Multiple developers may work on different features simultaneously.

Never assume that another developer's implementation should be replaced.

Before modifying an existing implementation:

* Inspect it.
* Understand it.
* Preserve it.
* Integrate with it when possible.

Never silently replace another developer's work.

---

# 13. TASK PLAN REQUIREMENT

Before implementation, provide a short plan.

The plan must contain:

### Objective
What will be implemented?

### Files to Create
Which new files are required?

### Files to Modify
Which existing files need modification?

### Files Not to Modify
Which existing pages/components must remain untouched?

### Implementation Steps
What will be done?

### Testing
How will the implementation be verified?

---

# 14. PLAN APPROVAL RULE

For tasks with significant architectural impact:

DO NOT immediately implement.

First provide the plan and identify the impact.

Examples:

* Changing `base.html`
* Changing global CSS
* Changing authentication architecture
* Changing database structure
* Reorganizing templates
* Replacing an existing component
* Introducing a new dependency

If the change may affect multiple existing features, STOP and request confirmation.

---

# 15. REUSE EXISTING COMPONENTS

Before creating a new component, check whether an equivalent component already exists.

Reuse:

* Navbar
* Footer
* Buttons
* Forms
* Cards
* Alerts
* Modals
* Layout components
* CSS variables
* Utility classes

Do not create duplicates unnecessarily.

---

# 16. DJANGO TEMPLATE RULES

Use:

* Template inheritance
* `{% extends %}`
* `{% block %}`
* `{% include %}`
* Django static files
* Django URL reversing

Avoid unnecessary duplication.

Example:
```text
base.html
    ↓
login.html
register.html
dashboard.html
```

Pages should inherit from the established base structure whenever appropriate.

---

# 17. RESPONSIVE DESIGN

Every new page must support:

* Desktop
* Tablet
* Mobile

Do not break the responsive behavior of existing pages.

Before modifying shared responsive CSS, inspect the impact on other pages.

---

# 18. COMPONENT NAMING

Use clear and consistent names.

Examples:
```text
login.html
register.html
dashboard.html
detection.html
result.html
history.html
profile.html
```

CSS:
```text
auth.css
dashboard.css
detection.css
```

JavaScript:
```text
auth.js
dashboard.js
detection.js
```

Avoid unclear names such as:
```text
new1.html
test.html
page2.html
final.html
final2.html
```

---

# 19. AUTHENTICATION UI RULE

Frontend developers may create:

* Login UI
* Registration UI
* Form validation UI
* Error states
* Loading states

Frontend developers must NOT independently invent authentication logic.

Backend authentication must be implemented using Django's backend/authentication system.

---

# 20. BACKEND BOUNDARY

Frontend developers must not modify backend logic unless the task explicitly requires integration.

Backend developers must not redesign frontend pages unless explicitly assigned.

When a task crosses both areas:

Clearly identify the dependency.

Example:
```text
Frontend:
Login UI complete.

Backend:
Authentication logic required.

Integration:
Connect Login form to Django authentication.
```

---

# 21. AI/CNN BOUNDARY

The CNN model is a separate AI/ML responsibility.

Do not place CNN training inside Django views.

The expected architecture is:

```text
Jupyter Notebook
      ↓
Dataset
      ↓
Training
      ↓
Evaluation
      ↓
Saved Model
      ↓
Django Prediction Service
      ↓
Django View
      ↓
Template
```

Do not invent model behavior if the trained model is not available.

---

# 22. FUTURE FEATURE RULE

Do not implement future features unless specifically assigned.

Examples:

* Weather intelligence
* Voice AI
* Offline AI
* Nutrient deficiency detection
* Fertilizer recommendations
* Community outbreak mapping
* Advanced analytics

The existence of a feature in the PRD does NOT mean it should automatically be implemented.

The assigned task controls the current scope.

---

# 23. STOP RULE — DUPLICATE

STOP if:

* The requested page already exists.
* The requested component already exists.
* The requested functionality already exists.
* A duplicate file would be created.
* A duplicate model/API/component would be created.

Report what already exists before continuing.

---

# 24. STOP RULE — UNEXPECTED CHANGES

STOP if completing the task appears to require changing an unrelated existing page.

Example:

Task:
> Create Register Page.

If the implementation unexpectedly requires changing:
```text
Landing Page
Dashboard
Detection Page
```

STOP.

Explain why the changes appear necessary.

Do not modify those pages without explicit approval.

---

# 25. STOP RULE — SHARED FILE

STOP before changing a high-impact shared file if the impact is unclear.

Examples:
```text
base.html
global.css / theme.css
common.js / main.js
settings.py
```

Inspect dependencies first.

If the change could affect multiple features and the correct approach is unclear:

STOP and ask for confirmation.

---

# 26. STOP RULE — ARCHITECTURAL CONFLICT

STOP if:

* Existing architecture conflicts with the task.
* Two implementations already exist.
* Requirements conflict.
* Another developer's work conflicts with the requested implementation.
* Database changes could be destructive.
* The correct implementation cannot be determined safely.

Do not guess.

---

# 27. STOP RULE — DO NOT "FIX" UNRELATED THINGS

If you notice an unrelated issue while implementing a task:

DO NOT automatically fix it.

Report it separately.

Example:
```text
During Login implementation, an unrelated issue was found in
the Landing Page navigation.

It was not modified because it is outside the current task scope.
```

---

# 28. DESIGN PRESERVATION TEST

After completing a task that creates a new page:

Verify that previously completed pages remain visually and functionally unchanged.

At minimum, verify:

* Landing page
* Existing navigation
* Existing footer
* Existing shared components
* Previously completed functionality

If an unrelated page changed unexpectedly:

Investigate before considering the task complete.

---

# 29. GIT SAFETY RULE

Developers must work in their assigned task branch.

Example:
```text
feature/frontend-login
```

Before starting:
```bash
git checkout develop
git pull origin develop
git checkout -b feature/frontend-login
```

Do not directly modify:
```text
main
```
or unrelated feature branches.

---

# 30. TASK COMPLETION REPORT

After implementation, report:

```text
TASK:
[Task ID and title]

STATUS:
Completed / Partially Completed / Blocked

PLAN:
[Short summary]

FILES CREATED:
[List]

FILES MODIFIED:
[List]

FILES NOT MODIFIED:
[List]

IMPLEMENTATION:
[What was implemented]

TESTING:
[What was tested]

REGRESSION CHECK:
[What existing pages/features were verified]

ISSUES:
[List]

NOTES:
[Any important information]
```

---

# 31. FINAL DEVELOPMENT RULE

The most important rule in Flora AI is:

> DO NOT CHANGE WHAT YOU WERE NOT ASKED TO CHANGE.

A new feature must be added to the existing system, not used as an excuse to redesign the existing system.

Before coding:

```text
READ
 ↓
INSPECT
 ↓
PLAN
 ↓
DEFINE FILE SCOPE
 ↓
IMPLEMENT
 ↓
TEST
 ↓
REGRESSION CHECK
 ↓
REPORT
```

If anything unexpected happens:

```text
STOP
 ↓
EXPLAIN
 ↓
WAIT FOR INSTRUCTION
```

---

# 32. TASK PROMPT TEMPLATE

Every Flora AI development task should follow this structure:

```text
TASK ID:
TASK TITLE:
TASK TYPE:
ASSIGNED TO:
PRIORITY:

DESCRIPTION:

REQUIREMENTS:

WHAT TO DO:

FILES TO CREATE:

FILES THAT MAY BE MODIFIED:

FILES / PAGES THAT MUST NOT BE MODIFIED:

DEPENDENCIES:

ACCEPTANCE CRITERIA:

OUT OF SCOPE:

TESTING REQUIREMENTS:

IMPORTANT:
Before implementation, read DESIGN.md.
Create an implementation plan first.
Follow all design and development rules.
Do not modify unrelated files or pages.
If unexpected changes or architectural conflicts are discovered, STOP and report them.
```

---

# 33. ABSOLUTE RULE

If a developer or AI agent is unsure whether a change is allowed:

**DO NOT MAKE THE CHANGE.**

Inspect the project.

Explain the situation.

Ask for clarification.

Protect existing functionality first.
