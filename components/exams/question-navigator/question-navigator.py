<div
class="
grid
grid-cols-5
gap-2
"
>

{% for question in questions %}

<button
class="
h-10
w-10
rounded
border
"
>

{{ forloop.counter }}

</button>

{% endfor %}

</div>