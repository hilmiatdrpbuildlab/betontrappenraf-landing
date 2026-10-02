/* Betontrappen Raf Geerts · landing page behaviour.
   rg.js (design system) already handles the mobile drawer, the filter tags and the form validation.
   This file adds the scrolling header, the active nav link, the gallery filter and the photo viewer. */
(function () {
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---------- Header: transparent over the hero, white bar after scrolling ----------
  var header = document.querySelector(".site-header");
  var hero = document.querySelector(".hero");
  var logo = header.querySelector(".rg-header__logo img");

  function setScrolled(on) {
    if (header.classList.contains("is-scrolled") === on) return;
    header.classList.toggle("is-scrolled", on);
    header.setAttribute("data-theme", on ? "light" : "dark");
    logo.src = on ? logo.dataset.logoLight : logo.dataset.logoDark;
  }
  function onScroll() { setScrolled(window.scrollY > hero.offsetHeight - 120); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Close the mobile drawer after choosing a link
  header.querySelectorAll(".rg-drawer a").forEach(function (a) {
    a.addEventListener("click", function () {
      if (header.hasAttribute("data-open")) header.querySelector(".rg-menu-btn").click();
    });
  });

  // ---------- Active nav link for the section in view ----------
  var navLinks = Array.prototype.slice.call(header.querySelectorAll(".rg-nav a"));
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var id = "#" + entry.target.id;
        navLinks.forEach(function (a) {
          if (a.getAttribute("href") === id) a.setAttribute("aria-current", "true");
          else a.removeAttribute("aria-current");
        });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    ["top", "over-raf", "aanbod", "werkwijze", "realisaties", "contact"].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) io.observe(el);
    });
  }

  // ---------- Gallery filter ----------
  var filterBox = document.querySelector(".gallery__filters");
  var cards = Array.prototype.slice.call(document.querySelectorAll(".gallery .rg-project"));
  var status = document.querySelector("[data-gallery-status]");

  // Counts per category in the filter tags
  filterBox.querySelectorAll("[data-count]").forEach(function (el) {
    var cat = el.getAttribute("data-count");
    el.textContent = cat === "alle" ? cards.length : cards.filter(function (c) { return c.dataset.category === cat; }).length;
  });

  function applyFilter(value) {
    var shown = 0;
    cards.forEach(function (card) {
      var match = value === "alle" || card.dataset.category === value;
      var wasHidden = card.hidden;
      card.hidden = !match;
      if (match) {
        shown++;
        if (wasHidden && !reduceMotion) {
          card.classList.remove("is-entering");
          void card.offsetWidth; // restart the animation
          card.classList.add("is-entering");
        }
      }
    });
    status.textContent = shown === 1 ? "1 realisatie getoond" : shown + " realisaties getoond";
  }
  filterBox.addEventListener("rg:filter", function (e) { applyFilter(e.detail.value); });

  // Hero stair types jump to the gallery, filtered
  document.querySelectorAll("[data-filter-link]").forEach(function (link) {
    link.addEventListener("click", function () {
      var tag = filterBox.querySelector('.rg-tag[value="' + link.dataset.filterLink + '"]');
      if (tag) tag.click();
    });
  });

  // ---------- Photo viewer ----------
  var lb = document.querySelector(".lightbox");
  var lbImg = lb.querySelector("[data-lb-img]");
  var lbTitle = lb.querySelector("[data-lb-title]");
  var lbBadge = lb.querySelector("[data-lb-badge]");
  var lbCount = lb.querySelector("[data-lb-count]");
  var current = 0;
  var visible = [];
  var opener = null;

  function pad(n) { return n < 10 ? "0" + n : String(n); }

  function show(i) {
    current = (i + visible.length) % visible.length;
    var card = visible[current];
    var img = card.querySelector(".rg-project__media img");
    lbImg.src = img.currentSrc || img.src;
    lbImg.alt = img.alt;
    lbTitle.textContent = card.querySelector(".rg-project__title a").textContent;
    lbBadge.textContent = card.querySelector(".rg-badge").textContent;
    lbCount.textContent = pad(current + 1) + " / " + pad(visible.length);
    // Hide the arrows when there is only one photo in the filtered set
    lb.querySelectorAll(".lightbox__nav").forEach(function (b) { b.hidden = visible.length < 2; });
  }

  function open(card, trigger) {
    if (!lb.showModal) return false;
    visible = cards.filter(function (c) { return !c.hidden; });
    opener = trigger;
    show(visible.indexOf(card));
    lb.showModal();
    document.documentElement.style.overflow = "hidden";
    return true;
  }

  cards.forEach(function (card) {
    var link = card.querySelector("[data-lightbox]");
    link.addEventListener("click", function (e) {
      if (open(card, link)) e.preventDefault();
    });
  });

  lb.querySelector("[data-lb-prev]").addEventListener("click", function () { show(current - 1); });
  lb.querySelector("[data-lb-next]").addEventListener("click", function () { show(current + 1); });
  lb.querySelector("[data-lb-close]").addEventListener("click", function () { lb.close(); });
  lb.addEventListener("keydown", function (e) {
    if (e.key === "ArrowLeft") { e.preventDefault(); show(current - 1); }
    if (e.key === "ArrowRight") { e.preventDefault(); show(current + 1); }
  });
  // Click outside the photo closes the viewer
  lb.addEventListener("click", function (e) {
    if (e.target === lb || e.target.classList.contains("lightbox__stage")) lb.close();
  });
  // Swipe on touch screens
  var touchX = null;
  lb.addEventListener("touchstart", function (e) { touchX = e.touches[0].clientX; }, { passive: true });
  lb.addEventListener("touchend", function (e) {
    if (touchX === null) return;
    var dx = e.changedTouches[0].clientX - touchX;
    if (Math.abs(dx) > 50) show(current + (dx < 0 ? 1 : -1));
    touchX = null;
  });
  lb.addEventListener("close", function () {
    document.documentElement.style.overflow = "";
    if (opener) opener.focus();
  });

  // ---------- Form: show the chosen file names in the drop zone ----------
  var fileInput = document.getElementById("cs-plan");
  var dropLabel = document.querySelector("[data-drop-label]");
  var dropDefault = dropLabel.innerHTML;
  fileInput.addEventListener("change", function () {
    var n = fileInput.files.length;
    if (!n) { dropLabel.innerHTML = dropDefault; return; }
    dropLabel.textContent = n === 1 ? fileInput.files[0].name : n + " bestanden gekozen";
  });

  // ---------- Footer year ----------
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = new Date().getFullYear();
})();
