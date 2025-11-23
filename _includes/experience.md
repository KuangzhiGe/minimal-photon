<h2 id="experience">Experience</h2>

<div class="experience">
  <ol class="experience-list">
    {% for item in site.data.experience.main %}
    <li class="experience-item">
      <div class="experience-logo">
        <img src="{{ item.image }}" alt="{{ item.title }}" class="logo-img">
      </div>
      <div class="experience-details">
        <div class="title">{{ item.title }}</div>
        <ul>
          <li>{{ item.details }}</li>
        </ul>
      </div>
    </li>
    {% endfor %}
  </ol>
</div>