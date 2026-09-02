const TAGS = ["BIO", "HG", "LLM"];
const state = { papers: [], filter: "ALL", query: "" };

const list = document.querySelector("#publication-list");
const summary = document.querySelector("#result-summary");
const search = document.querySelector("#search-input");
const filters = [...document.querySelectorAll("[data-filter]")];

function escapeHtml(value) {
  const node = document.createElement("span");
  node.textContent = value;
  return node.innerHTML;
}

function link(label, url) {
  if (!url) return "";
  return `<a class="resource" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer">${label} ↗</a>`;
}

function paperCard(paper) {
  const title = paper.paper
    ? `<a href="${escapeHtml(paper.paper)}" target="_blank" rel="noopener noreferrer">${escapeHtml(paper.title)}</a>`
    : escapeHtml(paper.title);
  return `
    <article class="paper-card">
      <span class="paper-badge">${paper.tags.join("+")}</span>
      <h3>${title}</h3>
      <p class="authors">${escapeHtml(paper.authors)}</p>
      <div class="paper-meta">
        <span class="venue">${escapeHtml(paper.venue)}</span>
        <span class="status">${escapeHtml(paper.status)}</span>
        ${link("Paper", paper.paper)}
        ${link("Code", paper.code)}
      </div>
    </article>`;
}

function render() {
  const query = state.query.trim().toLocaleLowerCase();
  const visible = state.papers.filter((paper) => {
    const tagMatch = state.filter === "ALL" || paper.tags.includes(state.filter);
    const haystack = [paper.title, paper.acronym, paper.authors, paper.venue, paper.note, ...paper.tags].join(" ").toLocaleLowerCase();
    return tagMatch && (!query || haystack.includes(query));
  });

  summary.textContent = `Showing ${visible.length} of ${state.papers.length} papers`;
  if (!visible.length) {
    list.innerHTML = '<p class="empty">No publications match this filter.</p>';
    return;
  }

  const years = [...new Set(visible.map((paper) => paper.year))].sort((a, b) => b - a);
  list.innerHTML = years.map((year) => {
    const cards = visible.filter((paper) => paper.year === year).map(paperCard).join("");
    return `<section class="year-group" aria-labelledby="year-${year}"><h3 class="year-heading" id="year-${year}">${year}</h3><div class="paper-list">${cards}</div></section>`;
  }).join("");
}

function setFilter(tag) {
  state.filter = tag;
  filters.forEach((button) => {
    const active = button.dataset.filter === tag;
    button.classList.toggle("active", active);
    button.setAttribute("aria-pressed", String(active));
  });
  const url = new URL(window.location.href);
  tag === "ALL" ? url.searchParams.delete("tag") : url.searchParams.set("tag", tag);
  history.replaceState({}, "", url);
  render();
}

filters.forEach((button) => button.addEventListener("click", () => setFilter(button.dataset.filter)));
document.querySelectorAll("[data-topic]").forEach((button) => button.addEventListener("click", () => {
  setFilter(button.dataset.topic);
  document.querySelector("#publications").scrollIntoView({ behavior: "smooth" });
}));
search.addEventListener("input", () => {
  state.query = search.value;
  render();
});

fetch("./papers.json")
  .then((response) => {
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return response.json();
  })
  .then((data) => {
    state.papers = data.papers;
    TAGS.forEach((tag) => {
      const count = state.papers.filter((paper) => paper.tags.includes(tag)).length;
      document.querySelector(`#count-${tag}`).textContent = `${count} ${count === 1 ? "paper" : "papers"}`;
    });
    const requested = new URLSearchParams(window.location.search).get("tag");
    setFilter(TAGS.includes(requested) ? requested : "ALL");
  })
  .catch((error) => {
    summary.textContent = "Catalog could not be loaded.";
    list.innerHTML = `<p class="empty">Open this page through a local web server or GitHub Pages. (${escapeHtml(error.message)})</p>`;
  });
