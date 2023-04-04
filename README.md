<h1>PASSWORD GENERATOR WEBSITE</h1>
  <p>A simple website to generate random password.</p>
<h2>Tools</h2>
  <p>
    <ul>
      <li>Python 3.10</li>
      <li>Django 4</li>
    </ul>
  </p>
<h2>Start</h2>
  <p>
    <ul>
      <li>Download the code</li>
      <li>Install requirements <code>pip install -r requirements.txt</code></li>
      <li>You need to generate your own SECRET_KEY using:
        <ol type="1">
          <li>Run the following command in the terminal of your Django project: <code>python manage.py shell</code></li>
          <li>Run the following command: <code>from django.core.management.utils import get_random_secret_key</code></li>
          <li>On the next line run the function to generate the secret key as follows:<code>print(get_random_secret_key())</code></li>
          <li>The Random secret key will be generated on the next line</li>
          <li>Insert generated secret key into <code>settigs.py</code>: <code>SECRET_KEY = 'django-insecure-{your_secret_key}'</code>
        </ol>
      <li>Start server using the following command in the terminal of your Django project: <code>python manage.py runserver</code>
    </ul>
  </p>
<hr>
<p>This code was written for educational purposes to learn Django framework.<br> 
  You can try it at <a href='mikefomin1.pythonanywhere.com' target='_blank'>mikefomin1.pythonanywhere.com</a>  
