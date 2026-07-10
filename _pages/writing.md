---
layout: page
title: "Writing & Notes"
permalink: /writing/
---

<p>Occasional writing on machine learning and research, plus lecture notes from my MSc at the University of Tübingen.</p>

{% if site.writing.size > 0 %}
<h2>Posts</h2>
<ul class="news">
  {% assign posts = site.writing | sort: 'date' | reverse %}
  {% for post in posts %}
  <li>
    <span class="date">{{ post.date | date: '%b %Y' }}</span>
    <span class="body"><a href="{{ post.url | relative_url }}">{{ post.title }}</a>{% if post.summary %} — {{ post.summary }}{% endif %}</span>
  </li>
  {% endfor %}
</ul>
{% endif %}

<h2>From Medium</h2>
<ul class="news" id="medium-posts">
  <li><span class="body">Loading recent posts&hellip; <a href="https://ashishpapanai.medium.com/">Read on Medium &rarr;</a></span></li>
</ul>

<h2>Course Notes</h2>
<p>Notes I'm writing up as I go through the MSc Machine Learning program at Tübingen. More will be added each semester.</p>
<ul class="timeline">
  <!-- Add a note by dropping a markdown file in _writing/ (see README), or list one manually:
  <li>
    <div class="head"><span class="r"><a href="/writing/deep-learning/">Deep Learning</a></span><span class="when">WS 2025/26</span></div>
    <div class="org">Lecture notes &amp; summaries</div>
  </li>
  -->
  <li>
    <div class="head"><span class="r" style="color:var(--faint);font-weight:500">Coming soon</span></div>
    <div class="org">Notes on Deep Learning, Probabilistic &amp; Statistical ML, Science of ML Benchmarks, and Multimodal Systems.</div>
  </li>
</ul>

<script>
// Pull the latest Medium posts client-side (no build-time dependency).
(function () {
  var feed = 'https://ashishpapanai.medium.com/feed';
  var api = 'https://api.rss2json.com/v1/api.json?rss_url=' + encodeURIComponent(feed);
  var el = document.getElementById('medium-posts');
  if (!el) return;

  function fmt(d) {
    try {
      return new Date(d).toLocaleDateString('en-US', { month: 'short', year: 'numeric' });
    } catch (e) { return ''; }
  }

  fetch(api)
    .then(function (r) { return r.json(); })
    .then(function (data) {
      if (!data || data.status !== 'ok' || !data.items || !data.items.length) throw 0;
      el.innerHTML = data.items.slice(0, 6).map(function (p) {
        return '<li><span class="date">' + fmt(p.pubDate) + '</span>' +
          '<span class="body"><a href="' + p.link + '">' + p.title + '</a></span></li>';
      }).join('');
    })
    .catch(function () {
      el.innerHTML = '<li><span class="body">' +
        '<a href="https://ashishpapanai.medium.com/">Read my posts on Medium &rarr;</a></span></li>';
    });
})();
</script>
