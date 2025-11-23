<h2 id="publications" style="margin: 2px 0px -15px; display: flex; align-items: baseline;">
  Selected Publications
  <small style="font-size: 0.8rem; font-weight: 400; margin-left: 1em;">
    {% assign scholar_link = site.social | where: "platform", "Google Scholar" | first %}
    {% if scholar_link %}
    <a href="{{ scholar_link.url }}" target="_blank" rel="noopener">(Click for full list)</a>
    {% endif %}
  </small>
</h2>

<div class="publications">
<!--
  Filter buttons are optional. You can customize them here or remove them.
  To use them, ensure your publications in _data/publications.yml have the corresponding 'tags'.
-->
<!--
<div id="filters" class="filters">
  <button class="btn active" data-filter="*">All</button>
  <button class="btn" data-filter="World Model">World Model</button>
  <button class="btn" data-filter="Embodied AI">Embodied AI</button>
  <button class="btn" data-filter="Multimodal Learning">Multimodal Learning</button>
  </div>
-->
<ol class="bibliography">

{% for link in site.data.publications.main %}

<li data-tags="{{ link.tags | join: ', ' }}">
<div class="pub-row">
  <div class="col-sm-3 abbr" style="position: relative;padding-right: 15px;padding-left: 15px;">
  {% if link.image %}
  <a href="{% if link.page %}{{ link.page }}{% else %}{{ link.pdf }}{% endif %}" target="_blank" rel="noopener noreferrer">
    <img src="{{ link.image }}" class="teaser img-fluid z-depth-1" style="width=100;height=auto;">
  </a>
  {% if link.conference_short %}
  <abbr class="badge">{{ link.conference_short }}</abbr>
  {% endif %}
  {% endif %}
  </div>
  <div class="col-sm-9" style="position: relative;padding-right: 15px;padding-left: 20px;">
      <div class="title"><a href="{{ link.pdf }}">{{ link.title }}</a></div>
      <div class="author">{{ link.authors }}</div>
      <div class="periodical"><em>{{ link.conference }}</em>
      </div>
    <div class="links">
        {% if link.url %}
        <a href="{{ link.url }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;"><i class="fas fa-file-pdf"></i> PDF</a>
        {% endif %}
        {% if link.code %}
        <a href="{{ link.code }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;"><i class="fab fa-github"></i> Code</a>
        {% endif %}
        {% if link.page %}
        <a href="{{ link.page }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;"><i class="fas fa-globe"></i> Project Page</a>
        {% endif %}
        {% if link.bibtex %}
        <a href="{{ link.bibtex }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;"><i class="fas fa-quote-right"></i> BibTex</a>
        {% endif %}
      {% if link.notes %}
      <strong> <i style="color:#e74d3c">{{ link.notes }}</i></strong>
      {% endif %}
      {% if link.others %}
      {{ link.others }}
      {% endif %}
    </div>
  </div>
</div>
</li>
<br>

{% endfor %}

</ol>
</div>
