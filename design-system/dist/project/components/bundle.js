/* @ds-bundle: {"format": 4, "namespace": "RG", "components": [{"name": "Button"}, {"name": "Header"}, {"name": "Footer"}, {"name": "Tabs"}, {"name": "Hero"}, {"name": "CTABand"}, {"name": "ContactSection"}, {"name": "SectionHeader"}, {"name": "ProjectCard"}, {"name": "ProcessSteps"}, {"name": "SpecList"}, {"name": "Card"}, {"name": "Badge"}, {"name": "Accordion"}, {"name": "FormField"}, {"name": "ChoiceControls"}, {"name": "Alert"}, {"name": "Toast"}, {"name": "Modal"}, {"name": "AdminShell"}, {"name": "DataTable"}, {"name": "MediaUploader"}, {"name": "StatCard"}]} */
/* Raf Geerts Betontrappen design system · behaviour for the interactive components.
   Plain script, no dependencies. Exposes window.RG.init(root) and runs it once on load.
   Every part is opt-in through data attributes or component classes, and init is safe to call twice. */
(function () {
  function each(root, sel, fn) {
    Array.prototype.forEach.call(root.querySelectorAll(sel), function (el) {
      if (el.dataset.rgReady) return;
      el.dataset.rgReady = "1";
      fn(el);
    });
  }

  // Header: .rg-header with a .rg-menu-btn opens the .rg-drawer; Escape closes it.
  function header(h) {
    var btn = h.querySelector(".rg-menu-btn");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var open = !h.hasAttribute("data-open");
      h.toggleAttribute("data-open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.setAttribute("aria-label", open ? "Menu sluiten" : "Menu openen");
    });
    h.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && h.hasAttribute("data-open")) { btn.click(); btn.focus(); }
    });
  }

  // Tabs: [data-rg-tabs] holding role="tab" buttons (aria-controls) and role="tabpanel" panels. Arrow keys move.
  function tabs(box) {
    var list = Array.prototype.slice.call(box.querySelectorAll('[role="tab"]'));
    function select(tab, focus) {
      list.forEach(function (t) {
        var on = t === tab;
        t.setAttribute("aria-selected", on ? "true" : "false");
        t.tabIndex = on ? 0 : -1;
        var panel = box.querySelector("#" + t.getAttribute("aria-controls"));
        if (panel) panel.hidden = !on;
      });
      if (focus) tab.focus();
    }
    list.forEach(function (tab, i) {
      tab.addEventListener("click", function () { select(tab, false); });
      tab.addEventListener("keydown", function (e) {
        var next = e.key === "ArrowRight" ? i + 1 : e.key === "ArrowLeft" ? i - 1 : e.key === "Home" ? 0 : e.key === "End" ? list.length - 1 : null;
        if (next === null) return;
        e.preventDefault();
        select(list[(next + list.length) % list.length], true);
      });
    });
  }

  // Filter tags: [data-rg-filter] holding .rg-tag buttons; one pressed at a time.
  function filter(box) {
    var tags = Array.prototype.slice.call(box.querySelectorAll(".rg-tag"));
    tags.forEach(function (t) {
      t.addEventListener("click", function () {
        tags.forEach(function (o) { o.setAttribute("aria-pressed", o === t ? "true" : "false"); });
        box.dispatchEvent(new CustomEvent("rg:filter", { bubbles: true, detail: { value: t.value || t.textContent.trim() } }));
      });
    });
  }

  // Forms: [data-rg-form] validates [required] fields on submit and swaps to its [data-rg-success] sibling.
  // Replace the success swap with the real endpoint when the site is built.
  function form(f) {
    f.setAttribute("novalidate", "");
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var first = null;
      Array.prototype.forEach.call(f.querySelectorAll("[required]"), function (input) {
        var field = input.closest(".rg-field");
        var bad = !input.checkValidity();
        if (field) field.classList.toggle("rg-field--error", bad);
        input.setAttribute("aria-invalid", bad ? "true" : "false");
        if (bad && !first) first = input;
      });
      if (first) { first.focus(); return; }
      var btn = f.querySelector('[type="submit"]');
      if (btn) { btn.classList.add("is-loading"); btn.setAttribute("aria-busy", "true"); }
      setTimeout(function () {
        var done = f.parentElement.querySelector("[data-rg-success]");
        if (btn) { btn.classList.remove("is-loading"); btn.removeAttribute("aria-busy"); }
        if (done) { f.hidden = true; done.hidden = false; done.focus(); }
      }, 700);
    });
    f.addEventListener("input", function (e) {
      var field = e.target.closest && e.target.closest(".rg-field--error");
      if (field && e.target.checkValidity()) { field.classList.remove("rg-field--error"); e.target.setAttribute("aria-invalid", "false"); }
    });
  }

  // Drop zone: .rg-drop highlights while a file is dragged over it.
  function drop(z) {
    ["dragenter", "dragover"].forEach(function (n) { z.addEventListener(n, function () { z.classList.add("is-over"); }); });
    ["dragleave", "drop"].forEach(function (n) { z.addEventListener(n, function () { z.classList.remove("is-over"); }); });
  }

  // Table selection: [data-rg-table] with a header checkbox [data-rg-all] and row checkboxes.
  function table(box) {
    var all = box.querySelector("[data-rg-all]");
    var rows = Array.prototype.slice.call(box.querySelectorAll("tbody input[type=checkbox]"));
    var bar = box.querySelector(".rg-toolbar");
    var count = box.querySelector("[data-rg-count]");
    function sync() {
      var n = rows.filter(function (r) { return r.checked; }).length;
      rows.forEach(function (r) { var tr = r.closest("tr"); if (tr) tr.setAttribute("aria-selected", r.checked ? "true" : "false"); });
      if (all) { all.checked = n === rows.length && n > 0; all.indeterminate = n > 0 && n < rows.length; }
      if (bar) bar.toggleAttribute("data-selected", n > 0);
      if (count) count.textContent = n === 1 ? "1 geselecteerd" : n + " geselecteerd";
    }
    if (all) all.addEventListener("change", function () { rows.forEach(function (r) { r.checked = all.checked; }); sync(); });
    rows.forEach(function (r) { r.addEventListener("change", sync); });
    sync();
  }

  // Dismiss: any [data-rg-dismiss] button removes its closest .rg-toast or .rg-alert.
  function dismiss(btn) {
    btn.addEventListener("click", function () {
      var el = btn.closest(".rg-toast, .rg-alert");
      if (el) el.remove();
    });
  }

  // Modal: [data-rg-open="id"] opens <dialog id>, [data-rg-close] closes it. Focus returns to the opener.
  function opener(btn) {
    btn.addEventListener("click", function () {
      var d = document.getElementById(btn.getAttribute("data-rg-open"));
      if (d && d.showModal) { d.showModal(); d.addEventListener("close", function () { btn.focus(); }, { once: true }); }
    });
  }
  function closer(btn) {
    btn.addEventListener("click", function () { var d = btn.closest("dialog"); if (d) d.close(btn.value || ""); });
  }

  // CMS: .rg-cms with .rg-cms__burger toggles the off-canvas sidebar; [data-rg-theme-toggle] flips light/dark.
  function cms(shell) {
    var b = shell.querySelector(".rg-cms__burger");
    if (b) b.addEventListener("click", function () {
      var open = !shell.hasAttribute("data-open");
      shell.toggleAttribute("data-open", open);
      b.setAttribute("aria-expanded", open ? "true" : "false");
    });
    shell.addEventListener("keydown", function (e) { if (e.key === "Escape" && shell.hasAttribute("data-open") && b) b.click(); });
  }
  function themeToggle(btn) {
    btn.addEventListener("click", function () {
      var target = btn.closest("[data-theme]") || document.documentElement;
      var next = target.getAttribute("data-theme") === "dark" ? "light" : "dark";
      target.setAttribute("data-theme", next);
      btn.setAttribute("aria-pressed", next === "dark" ? "true" : "false");
      try { localStorage.setItem("rg-cms-theme", next); } catch (e) { /* storage unavailable */ }
    });
  }

  function init(root) {
    root = root || document;
    each(root, ".rg-header", header);
    each(root, "[data-rg-tabs]", tabs);
    each(root, "[data-rg-filter]", filter);
    each(root, "[data-rg-form]", form);
    each(root, ".rg-drop", drop);
    each(root, "[data-rg-table]", table);
    each(root, "[data-rg-dismiss]", dismiss);
    each(root, "[data-rg-open]", opener);
    each(root, "[data-rg-close]", closer);
    each(root, ".rg-cms", cms);
    each(root, "[data-rg-theme-toggle]", themeToggle);
  }

  window.RG = { init: init, version: "1.0.0" };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { init(document); });
  else init(document);
})();
