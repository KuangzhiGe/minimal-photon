<div class="news-ticker-container">
    <ul class="news-ticker">
        {% for item in site.data.news %}
        <li><strong>[{{ item.date }}]</strong>{{ item.content }}</li>
        {% endfor %}
    </ul>
</div>
