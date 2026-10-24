document.documentElement.classList.add("js");

// Mobile menu
const burger = document.querySelector(".burger");
const links = document.getElementById("links");
if (burger) {
  burger.addEventListener("click", () => {
    const open = links.classList.toggle("open");
    burger.setAttribute("aria-expanded", open);
  });
}

// Light that follows the pointer across glass surfaces
document.addEventListener("pointermove", (e) => {
  const g = e.target.closest && e.target.closest(".glass");
  if (!g) return;
  const r = g.getBoundingClientRect();
  g.style.setProperty("--mx", e.clientX - r.left + "px");
  g.style.setProperty("--my", e.clientY - r.top + "px");
});

// Gentle tilt on cards (skipped when reduced motion is on)
if (!matchMedia("(prefers-reduced-motion: reduce)").matches) {
  document.querySelectorAll("[data-tilt]").forEach((el) => {
    el.addEventListener("pointermove", (e) => {
      const r = el.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width - 0.5;
      const y = (e.clientY - r.top) / r.height - 0.5;
      el.style.transform = `perspective(900px) rotateY(${x * 6}deg) rotateX(${-y * 6}deg) translateY(-4px)`;
    });
    el.addEventListener("pointerleave", () => (el.style.transform = ""));
  });
}

// Reveal sections below the fold
const io = new IntersectionObserver((entries) => {
  entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
}, { threshold: 0.12 });
document.querySelectorAll("main .wrap:not(.hero):not(.page-head)").forEach((s) => { s.classList.add("reveal"); io.observe(s); });

// Hero: simulated sensor readout
const temp = document.getElementById("temp");
if (temp) {
  const spark = document.getElementById("spark");
  const moist = document.getElementById("moist"), moistv = document.getElementById("moistv");
  const pump = document.getElementById("pump"), pumpv = document.getElementById("pumpv");
  let t = 27.4, m = 62, hist = Array.from({ length: 30 }, () => t);
  const draw = () => {
    const lo = Math.min(...hist) - 0.3, hi = Math.max(...hist) + 0.3;
    spark.setAttribute("points", hist.map((v, i) => `${(i / (hist.length - 1)) * 200},${48 - ((v - lo) / (hi - lo)) * 44}`).join(" "));
  };
  const tick = () => {
    t = Math.min(34, Math.max(22, t + (Math.random() - 0.5) * 0.8));
    m = Math.min(90, Math.max(30, m + (pump.classList.contains("on") ? 5 : -2.5) + (Math.random() - 0.5)));
    if (m < 40) pump.classList.add("on"); else if (m > 72) pump.classList.remove("on");
    hist.push(t); hist.shift();
    temp.textContent = t.toFixed(1);
    moist.style.width = m + "%"; moistv.textContent = Math.round(m) + "%";
    pumpv.textContent = pump.classList.contains("on") ? "On" : "Off";
    draw();
  };
  draw(); setInterval(tick, 1400);
}
