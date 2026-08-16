# Flora AI — Architecture & Design System Reference

## Overview
Flora AI is an AI-powered plant health platform designed to identify plant diseases from leaf images and provide actionable treatment recommendations.

This document serves as the technical reference for the frontend and UI architecture built using **Django Templates**, **CSS3 Custom Properties**, and modular **JavaScript**.

---

## 1. High-Level Architecture

```
User Browser
    ↓
Django Templates (base.html + page templates + reusable components)
    ↓
Django Views / URLs
    ↓
Backend Service / Database / AI Prediction Service
    ↓
Django Response Context
```

---

## 2. Directory Structure

```
Flora_AI/
├── config/                  # Django project configuration
│   ├── settings.py          # Centralized settings (STATICFILES_DIRS, TEMPLATES, MEDIA)
│   ├── urls.py              # Root URL routing
│   └── wsgi.py / asgi.py
├── static/                  # Static assets
│   ├── css/
│   │   ├── theme.css        # Design tokens (colors, typography, spacing, shadows)
│   │   └── components.css   # Reusable UI component styles (btn, card, form, alert)
│   ├── js/
│   │   └── main.js          # FloraUI helpers, accessible modal, alerts, CSRF fetch API
│   └── images/              # Logos and static visual assets
├── templates/               # Django template inheritance root
│   ├── base.html            # Master layout shell
│   ├── includes/            # Shared structural includes (header.html, footer.html)
│   ├── components/          # Reusable UI component templates (alert, badge, card, modal, loader)
│   └── pages/               # Feature-specific page templates (populated per development task)
├── media/                   # Uploaded plant images directory
├── .env.example             # Environment configuration template
├── ARCHITECTURE.md          # Technical reference document
└── README.md                # Developer quickstart and setup guide
```

---

## 3. Design System Standards

### Nature-Inspired Emerald & Tech Palette
- **Primary Accent**: Emerald Green (`--color-primary-500: #10b981`, `--color-primary-600: #059669`)
- **Secondary Accent**: Tech Teal (`--color-secondary-500: #14b8a6`)
- **Body & Surfaces**: Dark tech theme (`--bg-body: #091310`, `--bg-surface: #101e19`, `--bg-card: #152721`)
- **Typography**: Google Fonts Inter (Body text) and Outfit (Headings)

### Reusable UI Components
All future pages must reuse established components:
- **Buttons**: `.btn`, `.btn-primary`, `.btn-secondary`, `.btn-outline`, `.btn-ghost`
- **Forms**: `.form-group`, `.form-label`, `.form-input`, `.form-select`, `.dropzone`
- **Cards**: `.card`, `.card-header`, `.card-body`, `.card-footer`
- **Badges**: `.badge-primary`, `.badge-success`, `.badge-warning`, `.badge-danger`, `.badge-info`
- **Alerts**: `.alert-success`, `.alert-warning`, `.alert-danger`, `.alert-info`

---

## 4. Frontend & Backend Boundary Guidelines

1. **Independent Frontend Layer**: Do not hardcode CNN model prediction logic into the frontend. Use dynamic Django template context variables.
2. **CSRF Safety**: All JavaScript fetch calls to backend APIs must pass the Django CSRF token (`FloraUI.fetchAPI(url, options)`).
3. **Task-Based Incremental Building**: Pages are built strictly when assigned through individual tasks.
