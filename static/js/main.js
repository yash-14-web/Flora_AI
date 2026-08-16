/**
 * Flora AI - Main Frontend JavaScript Foundation
 * Provides accessible UI component interactions, modal handling, image preview utilities,
 * and Django CSRF-safe API fetch helper.
 */

document.addEventListener('DOMContentLoaded', () => {
  FloraUI.init();
});

const FloraUI = {
  init() {
    this.initModals();
    this.initAlerts();
    this.initMobileNav();
  },

  /**
   * Helper to retrieve Django CSRF token from cookies
   */
  getCsrfToken() {
    const name = 'csrftoken';
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  },

  /**
   * Wrapper for fetch requests with automatic CSRF token inclusion
   */
  async fetchAPI(url, options = {}) {
    const defaultHeaders = {
      'X-CSRFToken': this.getCsrfToken() || '',
    };

    if (!(options.body instanceof FormData)) {
      defaultHeaders['Content-Type'] = 'application/json';
    }

    const mergedOptions = {
      ...options,
      headers: {
        ...defaultHeaders,
        ...options.headers,
      },
    };

    try {
      const response = await fetch(url, mergedOptions);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.error('FloraAI API Fetch Error:', error);
      throw error;
    }
  },

  /**
   * Accessible Modal Window Manager
   */
  initModals() {
    document.addEventListener('click', (e) => {
      const trigger = e.target.closest('[data-modal-target]');
      if (trigger) {
        const targetId = trigger.getAttribute('data-modal-target');
        this.openModal(targetId);
      }

      const closeBtn = e.target.closest('[data-modal-close]');
      if (closeBtn) {
        const modal = closeBtn.closest('.modal-backdrop');
        if (modal) {
          this.closeModal(modal.id);
        }
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        const openModal = document.querySelector('.modal-backdrop.is-open');
        if (openModal) {
          this.closeModal(openModal.id);
        }
      }
    });
  },

  openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
      modal.classList.add('is-open');
      modal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }
  },

  closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
      modal.classList.remove('is-open');
      modal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
  },

  /**
   * Alert Dismissal Manager
   */
  initAlerts() {
    document.addEventListener('click', (e) => {
      const closeBtn = e.target.closest('.alert-close');
      if (closeBtn) {
        const alert = closeBtn.closest('.alert');
        if (alert) {
          alert.style.opacity = '0';
          setTimeout(() => alert.remove(), 250);
        }
      }
    });
  },

  /**
   * Mobile Navigation Toggle
   */
  initMobileNav() {
    const toggle = document.querySelector('.navbar-mobile-toggle');
    const nav = document.querySelector('.navbar-nav');
    if (toggle && nav) {
      toggle.addEventListener('click', () => {
        const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
        toggle.setAttribute('aria-expanded', !isExpanded);
        nav.classList.toggle('is-visible');
      });
    }
  },

  /**
   * Client-side Image Preview Utility for Plant Upload Forms
   */
  setupImagePreview(inputElement, previewContainer, callback = null) {
    if (!inputElement || !previewContainer) return;

    inputElement.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (file && file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = (event) => {
          previewContainer.innerHTML = `<img src="${event.target.result}" alt="Plant Leaf Preview" class="img-preview" />`;
          if (typeof callback === 'function') callback(file);
        };
        reader.readAsDataURL(file);
      }
    });
  }
};
