# Flora AI — Master Project Context & Constitution

> **Tagline:** *"Detect. Understand. Treat."*  
> **Project Type:** AI-powered Plant Health and Disease Detection Platform  
> **Primary Purpose:** Flora AI enables users to provide plant/leaf images, identify possible diseases using an AI/ML model, and obtain actionable treatment and care recommendations.

---

## 1. Project Overview & Boundaries

- **Development Strategy:** Incremental, task-driven development.
- **Execution Flow:** `Foundation` → `UI` → `Backend` → `Database` → `AI/ML Integration` → `Advanced Features`.
- **Core Rule:** Build strictly what each development task specifies. Do not pre-emptively create pages, invent models, or add unrequested features.

```
Long-Term Vision (Implemented only when explicitly tasked):
├── Plant Disease Detection & Classification
├── Actionable Treatment Recommendations
├── Hyper-Local Weather Intelligence
├── Multilingual Accessibility
├── Voice-Driven AI & Offline/Edge Detection
└── Nutrient Deficiency & Community Disease Mapping
```

---

## 2. Technical Architecture

```
Frontend (Django Templates / Mobile-Responsive UI)
    ↓
Backend API (Django Views / API Endpoints)
    ↓
AI/ML Prediction Service (Independent Service Layer)
    ↓
Trained Plant Disease Model (Saved Weights / PyTorch / TensorFlow)
```

- **Frontend & Model Separation:** The web application and frontend templates will **never** contain CNN training logic.
- **AI/ML Lifecycle:** Model development, training, dataset processing, and validation are conducted separately (e.g., via Python / Jupyter notebooks). The web app interacts with the model only via an integrated prediction service interface.

---

## 3. Design System & Visual Identity

Flora AI adopts a **modern agricultural technology identity**: clean, professional, accessible, and nature-inspired.

### Centralized Design Tokens (`static/css/theme.css`)
- **Primary Color Palette:** Nature-inspired Emerald Green (`#10b981`, `#059669`, `#047857`)
- **Secondary Palette:** Tech Teal (`#14b8a6`, `#0d9488`)
- **Neutral & Dark Surfaces:** High-contrast, clean dark theme (`#091310`, `#101e19`, `#152721`)
- **Feedback Accents:**
  - Success: `#22c55e`
  - Warning: `#f59e0b`
  - Danger: `#ef4444`
  - Info: `#0ea5e9`
- **Typography:**
  - Headings: `Outfit`, sans-serif
  - Body: `Inter`, system-ui, -apple-system, sans-serif
- **Spatial Grid:** 4px baseline scale (`--space-1` to `--space-16`)
- **Shadows & Radii:** Rounded corners (`var(--radius-md)`, `var(--radius-lg)`), soft elevation blurs

### Reusable UI Foundation Components (`static/css/components.css` & `templates/components/`)
- **Buttons:** `.btn`, `.btn-primary`, `.btn-secondary`, `.btn-outline`, `.btn-ghost`, `.btn-sm`, `.btn-lg`
- **Form Controls:** `.form-group`, `.form-label`, `.form-input`, `.form-select`, `.dropzone`
- **Cards & Containers:** `.card`, `.card-header`, `.card-body`, `.card-footer`, `.container`, `.page-wrapper`
- **Feedback & Badges:** `.alert-*`, `.badge-*`, `.loader`, `.spinner`
- **Overlays:** Modal dialogues with accessible keyboard / backdrop dismissal (`FloraUI.Modal`)

---

## 4. Directory Structure

```
Flora_AI/
├── MASTER_CONTEXT.md        # Master project rules & architectural constitution
├── ARCHITECTURE.md          # Frontend/backend technical reference
├── README.md                # Quickstart and setup guide
├── manage.py                # Django CLI entrypoint
├── requirements.txt         # Project dependencies
├── .env.example             # Environment variable template
├── config/                  # Django project configuration
│   ├── settings.py          # Centralized settings
│   ├── urls.py              # Root URL routing
│   └── wsgi.py / asgi.py
├── static/                  # Static assets
│   ├── css/
│   │   ├── theme.css        # Central design tokens
│   │   ├── components.css   # Reusable component classes
│   │   └── base.css         # CSS reset and base rules
│   ├── js/
│   │   └── main.js          # Core JS foundation & FloraUI helpers
│   └── images/              # Static brand graphics and icons
├── templates/               # Django template inheritance tree
│   ├── base.html            # Master HTML layout
│   ├── includes/            # Shared partials (header.html, footer.html)
│   ├── components/          # Reusable component snippets (card, alert, modal, badge, loader)
│   └── pages/               # Feature pages (built per individual development task)
└── media/                   # User-uploaded leaf/plant images
```

---

## 5. Development & Task Execution Rules

When implementing any task:
1. **Read & Align:** Check requirements against this Master Context.
2. **Strict Scope:** Implement **only** the assigned page or feature. Do not generate unrequested pages or speculative backend services.
3. **Design Consistency:** Always reuse existing CSS classes, design tokens, and template components.
4. **Mobile Responsiveness:** Ensure all layouts look great on mobile devices (crucial for field photography).
5. **Accessibility:** Ensure high contrast, semantic HTML, and proper `aria` attributes.
6. **Report Clearly:** Document files created, modified, and any specific assumptions made.
